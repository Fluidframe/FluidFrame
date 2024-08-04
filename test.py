import re
from pprint import pprint
from typing import Optional
from fluidframe.utils import prettify, save_as_html
from fluidframe.components.base_components import Root
from fluidframe.components.view_components import Text, Header, SubHeader, Title
from fluidframe.components.layout_components import Column



'''
class FluidFrame():
    def  __init__(self, title: str) -> None:
        self.pages = []
        self.root = Root(template_dir="fluidframe/templates", template_path="root.html", title=title)
    
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
    
        
        
        
ff = FluidFrame(title="Sample page")

ff.title(body="Title")
ff.title(body="Title with tool tip", help="message")

ff.header(body="Header")
ff.header(body="Header with tooltip", help="message")

ff.subheader(body="Subheader")
ff.subheader(body="Subheader with tooltip", help="message")

ff.text(body="This is a sample text 1")
ff.text(body="This is a a second sample text 2 with a tool tip", help="haaha... the tool tip is working")

html = ff.root.render()




html = prettify(html)
save_as_html("./tests/index.html", html)
'''

from fluidframe.tags import div, img, p, h1, html, a

content = div(cls="container", id="container_id", body=[
    h1(cls="heading", body="This is a heading"),
    img(src="https://example.com/image.png", alt="An example image", cls="image"),
    p(body="This is a paragraph with a "),
    div(body="This is a sample div with a text")
])

content = prettify(content)
print(content)

print(50*"=")

content = html(body=[
    div(cls="container-new", id="container_id", body=[
        h1(cls="heading", body="This is a heading"),
        img(src="https://example.com/image.png", alt="An example image", cls="image"),
        a(cls="link", href="reference-link", body="this is the body")
    ]),
])

content = prettify(content)
print(content)
