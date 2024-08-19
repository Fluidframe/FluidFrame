import uvicorn, random
from pathlib import Path
from typing import Optional
from fluidframe import get_lib_path
from fluidframe.core.components import Root
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect
from fluidframe.config import MODULES_DIR, PUBLIC_DIR
from fluidframe.utilities.helper import save_as_html
from fluidframe.utilities.tailwind_utils import tailwind_build
from fluidframe.core import div, head, body, html, button, script, link, span
from fluidframe.components.stateless.text_components import Text, Header, SubHeader, Title, Code, Markdown


tailwind_build()


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
    
    def markdown(self, body: str, help: Optional[str]=None) -> Markdown:
        md = Markdown(parent=self.root, body=body, help=help)
        self.root.add_child(md)
        return md
    

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
    return ff.header("This is a fluidframe header").render()
""", language="python")
    
    ff.markdown("""# Title 1
## Title 2
### Title 3

- list 1
* list 2
- list 3

>> Highlighetd

```python
def show_code():
    return "code_shown"
```
""")
    
    save_as_html("index.html", ff.root.render())

    return HTMLResponse(ff.root.render())
    

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
        WebSocketRoute('/ws', hot_reload_socket),
    ]
)

lib_dir = get_lib_path()
fluidpack_dir = Path(__file__).resolve().parent / "fluidpack"

app.mount(f'/{PUBLIC_DIR}', StaticFiles(directory=str(lib_dir / "public")), name=PUBLIC_DIR)
app.mount(f'/{MODULES_DIR}', StaticFiles(directory=str(lib_dir / "node_modules")), name=MODULES_DIR)
app.mount('/style', StaticFiles(directory=str(fluidpack_dir)), name='style')

# Do `fluidframe init myproject` first
if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.1', port=8000, reload=True)
