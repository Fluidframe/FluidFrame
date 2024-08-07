import uvicorn
from build import build_tailwind
from starlette.routing import Route
from starlette.routing import Mount
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fluidframe.core import div, head, body, html, button, script, link

contacts = [
    {"name": "Agent A"},
    {"name": "Agent B"},
    {"name": "Agent C"},
]

async def homepage(request):
    content = html(
            head(
                script(src="libs/htmx.org/dist/htmx.min.js"),
                link(href="static/css/dist/output.css", rel="stylesheet"),
            ),
            body(
                div(
                    button("Load More", hx_get="/more-content", hx_target="#section1, #section2", hx_swap="outerHTML", cls="dark:bg-green-700"),
                    div("Initial content for section 1", id="section1"),
                    div("Initial content for section 2", id="section2")
                ),
                cls="dark:bg-gray-700 bg-white dark:text-white flex justify-content"
            )
        )

    return HTMLResponse(content)
    

async def more_content(request):
    content=(
        div("Initial content for section 1", id="section1"),
        div("Initial content for section 2", id="section2")
    )
    return HTMLResponse(''.join(content))
    

app = Starlette(
    debug=True, 
    routes=[
        Route('/', homepage),
        Route('/more-content', more_content),
    ]
)

app.mount('/libs', StaticFiles(directory='node_modules'), name='libs')
app.mount('/static', StaticFiles(directory='fluidframe/static'), name='static')

if __name__ == '__main__':
    build_tailwind()
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)