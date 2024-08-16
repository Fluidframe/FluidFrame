import uvicorn, random
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect
from fluidframe.core import div, head, body, html, button, script, link, span


contacts = [
    {"name": "Agent A"},
    {"name": "Agent B"},
    {"name": "Agent C"},
]

async def homepage(request):
    content = html(
            head(
                script(src="https://cdnjs.cloudflare.com/ajax/libs/htmx/2.0.2/htmx.min.js"),
                link(href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css", rel="stylesheet"),
                """
                <style>
                    .tooltip {
                        display: none; /* Hide by default */
                        position: absolute;
                        background-color: #333;
                        color: #fff;
                        padding: 5px;
                        border-radius: 5px;
                        white-space: nowrap;
                        z-index: 10;
                    }
                    .hover-div {
                        display: inline-block;
                        padding: 20px;
                        background-color: #f0f0f0;
                        border: 1px solid #ccc;
                    }
                </style>
                """
            ),
            body(
                div(
                    button("Load More", hx_get="/more-content", hx_target="#section1, #section2", hx_swap="outerHTML transition:true", cls="dark:bg-green-700"),
                    div("Initial content for section 1", id="section1"),
                    div("Initial content for section 2", id="section2"),
                    span(id="tooltip", cls="tooltip"),
                    cls="hover-div", hx_get="/tooltip-content", hx_trigger="mouseenter", hx_target="#tooltip", hx_swap="innerHTML",
                ),
                """
                <script>
                    const hoverDiv = document.querySelector('.hover-div');
                    const tooltip = document.getElementById('tooltip');

                    hoverDiv.addEventListener('mouseenter', () => {
                        tooltip.style.display = 'inline-block';
                    });

                    hoverDiv.addEventListener('mouseleave', () => {
                        tooltip.style.display = 'none';
                    });

                    hoverDiv.addEventListener('mousemove', (e) => {
                        tooltip.style.left = e.pageX + 10 + 'px';
                        tooltip.style.top = e.pageY + 10 + 'px';
                    });
                </script>
                """,
                cls="dark:bg-gray-700 bg-white dark:text-white flex justify-content h-full w-full"
            )
        )

    return HTMLResponse(content)

async def tooltip(request):
    return HTMLResponse(f"This is the tooltip with random content dynamically from server! {random.randrange(0, 1000)}")

async def more_content(request):
    content=(
        div("Initial content for section 1", id="section1"),
        div("Initial content for section 2", id="section2")
    )
    return HTMLResponse(''.join(content))
    

async def hot_reload_socket(websocket):
    await websocket.accept()
    try:
        await websocket.send_text('Hello, client!')
    except WebSocketDisconnect:
        print('Client connection closed')    


app = Starlette(
    debug=True, 
    routes=[
        Route('/', homepage),
        Route('/more-content', more_content),
        Route('/tooltip-content', tooltip),
        WebSocketRoute('/ws', hot_reload_socket),
    ]
)

if __name__ == '__main__':
    uvicorn.run("htmx_test:app", host='127.0.0.1', port=8000, reload=True)