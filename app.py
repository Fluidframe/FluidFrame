import uvicorn, random
from typing import Optional
from build import tailwind_watch
from fluidframe.core.components import Root
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect, WebSocketState
from fluidframe.core import div, head, body, html, button, script, link, span
from fluidframe.components.stateless.text_components import Text, Header, SubHeader, Title, Code


tailwind_watch()


contacts = [
    {"name": "Agent A"},
    {"name": "Agent B"},
    {"name": "Agent C"},
]


class FluidFrame():
    def  __init__(self, title: str) -> None:
        self.pages = []
        self.root = Root(title=title)
    
    def text(self, body: str, help: Optional[str]=None) -> Text:
        text = Text(parent=self.root, body=body, help=help)
        self.root.add_child(text)
        return text

    def title(self, body: str, help: Optional[str]=None) -> Title:
        title = Title(parent=self.root, body=body, help=help)
        self.root.add_child(title)
        return title

    def header(self, body: str, help: Optional[str]=None) -> Header:
        header = Header(parent=self.root, body=body, help=help)
        self.root.add_child(header)
        return header
    
    def subheader(self, body: str, help: Optional[str]=None) -> SubHeader:
        subheader = SubHeader(parent=self.root, body=body, help=help)
        self.root.add_child(subheader)
        return subheader
    
    def code(self, body: str, language: Optional[str]=None) -> Code:
        cd = Code(parent=self.root, body=body, language=language)
        self.root.add_child(cd)
        return cd
    

async def sample(request):
    ff = FluidFrame(title="Sample page")
    
    ff.title(body="Title")
    ff.title(body="Title with tool tip", help="message")

    ff.header(body="Header")
    ff.header(body="Header with tooltip", help="message")

    ff.subheader(body="Subheader")
    ff.subheader(body="Subheader with tooltip", help="message")

    ff.text(body="This is a sample text 1")
    ff.text(body="This is a a second sample text 2 with a tool tip", help="haaha... the tool tip is working")

    ff.code(body="""import numpy as np
import fluidframe as ff

def myfunc():
    return ff.header("This is a fluidframe header").render()""", language="python")

    return HTMLResponse(ff.root.render())
    

async def homepage(request):
    content = html(
            head(
                script(src="modules/htmx.org/dist/htmx.min.js"),
                link(href="lib_static/css/dist/output.css", rel="stylesheet"),
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
        Route('/', sample),
        Route('/home', homepage),
        Route('/more-content', more_content),
        Route('/tooltip-content', tooltip),
        WebSocketRoute('/ws', hot_reload_socket),
    ]
)

app.mount('/modules', StaticFiles(directory='node_modules'), name='modules')
app.mount('/lib_static', StaticFiles(directory='fluidframe/static'), name='lib_static')

if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.2', port=8000, reload=True)