import random
from pathlib import Path
from typing import Optional
from fluidframe.utils import get_lib_path
from fluidframe.core.fluidframe import Root
from fluidframe.config import MODULES_DIR, PUBLIC_DIR
from fluidframe.utilities.tailwind_utils import tailwind_build
from fluidframe.core import div, head, body, button, script, link, span
from robyn import Robyn, serve_file, html, WebSocket, WebSocketConnector, jsonify
from fluidframe.components.text_components import Text, Header, SubHeader, Title, Code, Markdown


tailwind_build()

app = Robyn(__file__)


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
    
    return html(ff.root.render())
    
    
socket = WebSocket(app, "/ws")
@socket.on("connect")
async def hot_reload_socket():
    return jsonify({"data": "Hello, client!"})

@socket.on("close")
async def hot_reload_socket():
    return 'Client connection closed'

@socket.on("message")
async def message(ws: WebSocketConnector):
    print(ws.query_params)
    return jsonify({"data": "Hello, client!"})


app.add_route("GET", "/", sample)

lib_dir = get_lib_path()
fluidpack_dir = Path(__file__).resolve().parent / "fluidpack"

app.add_directory('/style', str(fluidpack_dir), 'style')
app.add_directory(f'/{PUBLIC_DIR}', str(lib_dir / "public"))
app.add_directory(f'/{MODULES_DIR}', str(lib_dir / "node_modules"))


@app.get("/get_file")
async def serve(request):
    return serve_file("../fluidframe/public/assets/fluidframe-logo.webp", "image.webp")


app.start(port=8080)