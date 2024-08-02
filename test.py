import re
from pprint import pprint
from typing import Optional
from fluidframe.base import Page
from fluidframe.utils import prettify, save_as_html
from fluidframe.components.view_components import Text, Header, SubHeader, Title
from fluidframe.components.layout_components import Column
from fluidframe.components.base_components import RootComponent



class FluidFrame():
    def  __init__(self, title: str) -> None:
        self.pages = []
        self.page = Page(title)
        self.root_component = RootComponent()
    
    def text(self, body: str, help: Optional[str]=None, inline: Optional[bool]=None) -> Text:
        text = Text(parent=self.root_component, body=body, help=help, inline=inline)
        self.page.add_child(text)
        return text

    def title(self, body: str, help: Optional[str]=None) -> Title:
        title = Title(parent=self.root_component, body=body, help=help)
        self.page.add_child(title)
        return title

    def header(self, body: str, help: Optional[str]=None) -> Header:
        header = Header(parent=self.root_component, body=body, help=help)
        self.page.add_child(header)
        return header
    
    def subheader(self, body: str, help: Optional[str]=None) -> SubHeader:
        subheader = SubHeader(parent=self.root_component, body=body, help=help)
        self.page.add_child(subheader)
        return subheader
    
        
        
ff = FluidFrame(title="Sample page")

ff.title("Title")
ff.title("Title with tool tip", "message")

ff.header("Header")
ff.header("Header with tooltip", "message")

ff.subheader("Subheader")
ff.subheader("Subheader with tooltip", "message")

ff.text("This is a sample text 1")
ff.text("This is a a second sample text 2 with a tool tip", "haaha... the tool tip is working")

html = ff.page.render()



html = prettify(html)
save_as_html("./tests/index.html", html)

