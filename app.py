import uvicorn, random
from pathlib import Path
from typing import Optional
from fluidframe.core.components import Root
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect
from fluidframe.config import MODULES_DIR, PUBLIC_DIR
from fluidframe.utilities.tailwind_utils import tailwind_build
from fluidframe.core import div, head, body, html, button, script, link, span
from fluidframe.components.stateless.text_components import Text, Header, SubHeader, Title, Code


tailwind_build()
script_dir = Path(__file__).resolve().parent


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
    return ff.header("This is a fluidframe header").render()
""", language="python")
    ff.text("""<h1>Hi this is a title</h1>
<p>I just wanted to write this</p>
<pre><code class="language-python">print("this as a code block")</code></pre>

<p>and</p>
<pre><code class="language-python">def hello_world():
    print("Hello, World!")</code></pre>

<h1>h1</h1>
<h2>h2</h2>
<h3>h3</h3>
<h4>h4</h4>
<h5>h5</h5>
<h6>h6</h6>
<ul>
<li>item 1</li>
<li>
<ul>
<li>item 2<li>
<li>item 3</li>
<li>item 4 </li>
</ul>
</li>
</ul>

""")
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

app.mount(f'/{PUBLIC_DIR}', StaticFiles(directory=str(script_dir / "fluidframe/public")), name=PUBLIC_DIR)
app.mount(f'/{MODULES_DIR}', StaticFiles(directory=str(script_dir / "fluidframe/node_modules")), name=MODULES_DIR)
app.mount('/style', StaticFiles(directory=str(script_dir / "fluidpack")), name='style')

# Do `fluidframe init myproject` first
if __name__ == '__main__':
    uvicorn.run("app:app", host='127.0.0.2', port=8000, reload=True)
