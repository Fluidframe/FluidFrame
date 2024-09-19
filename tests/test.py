import uvicorn
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

count = 0


HTMX_VANILA = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vanilla HTMX Counter</title>
    <script src="https://unpkg.com/htmx.org@1.9.6"></script>
</head>
<body>
    <h1>Vanilla HTMX Counter</h1>
    <div id="count">[[count]]</div>
    <button hx-post="/increment" hx-target="#count">Increment</button>
    <button hx-post="/decrement" hx-target="#count">Decrement</button>
</body>
</html>"""

HTMX_SOCKET = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket HTMX-like Counter</title>
</head>
<body>
    <h1>WebSocket HTMX-like Counter</h1>
    <div id="count">[[count]]</div>
    <button ws-send="increment" ws-target="#count">Increment</button>
    <button ws-send="decrement" ws-target="#count">Decrement</button>

    <script>
        const socket = new WebSocket('ws://localhost:8000/ws');
        
        socket.onmessage = function(event) {
            const targetId = this.activeTarget;
            if (targetId) {
                document.querySelector(targetId).outerHTML = event.data;
            }
        };

        document.body.addEventListener('click', function(event) {
            const target = event.target;
            if (target.hasAttribute('ws-send')) {
                const message = target.getAttribute('ws-send');
                const wsTarget = target.getAttribute('ws-target');
                socket.activeTarget = wsTarget;
                socket.send(message);
            }
        });
    </script>
</body>
</html>"""



@app.get("/")
async def root():
    return {"message": "Counter App"}

@app.get("/test-vanilla-htmx", response_class=HTMLResponse)
async def test_vanilla_htmx(request: Request):
    return HTMLResponse(HTMX_VANILA.replace("[[count]]", str(count)))

@app.post("/increment")
async def increment():
    global count
    count += 1
    return f'<div id="count">{count}</div>'

@app.post("/decrement")
async def decrement():
    global count
    count -= 1
    return f'<div id="count">{count}</div>'

@app.get("/test-new-htmx", response_class=HTMLResponse)
async def test_new_htmx(request: Request):
    return HTMLResponse(HTMX_SOCKET.replace("[[count]]", str(count)))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global count
    while True:
        data = await websocket.receive_text()
        if data == "increment":
            count += 1
        elif data == "decrement":
            count -= 1
        await websocket.send_text(f'<div id="count">{count}</div>')
        
        
if __name__ == '__main__':
    uvicorn.run("test:app", host="127.0.0.1", port=8000)
