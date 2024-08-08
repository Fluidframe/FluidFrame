import uvicorn
from typing import Optional
from build import build_tailwind
from starlette.routing import Route
from fluidframe.core.components import Root
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from fluidframe.core import div, head, body, html, button, script, link
from fluidframe.components.stateless.text_components import Text, Header, SubHeader, Title, Code

contacts = [
    {"name": "Agent A"},
    {"name": "Agent B"},
    {"name": "Agent C"},
]
build_tailwind()

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
                script(src="libs/htmx.org/dist/htmx.min.js"),
                link(href="static/css/dist/output.css", rel="stylesheet"),
            ),
            body(
                div(
                    button("Load More", hx_get="/more-content", hx_target="#section1, #section2", hx_swap="outerHTML transition:true", cls="dark:bg-green-700"),
                    div("Initial content for section 1", id="section1"),
                    div("Initial content for section 2", id="section2")
                ),
                cls="dark:bg-gray-700 bg-white dark:text-white flex justify-content h-full w-full"
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
        Route('/', sample),
        Route('/home', homepage),
        Route('/more-content', more_content),
    ]
)

app.mount('/libs', StaticFiles(directory='node_modules'), name='libs')
app.mount('/static', StaticFiles(directory='fluidframe/static'), name='static')

if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)