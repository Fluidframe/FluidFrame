import re
from pprint import pprint
from typing import Optional
from fluidframe.core.components import Root
from fluidframe.utils import prettify, save_as_html
from fluidframe.components.stateless.layout_components import Column
from fluidframe.components.stateless.text_components import Text, Header, SubHeader, Title, Code
from fluidframe.core import div, a, img, h1, p, html, hr, head, header, title, body, script, meta, link


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
        

if __name__=="__main__":
    ff = FluidFrame(title="Sample page")

    ff.title(body="Title")
    ff.title(body="Title with tool tip", help="message")

    ff.header(body="Header")
    ff.header(body="Header with tooltip", help="message")

    ff.subheader(body="Subheader")
    ff.subheader(body="Subheader with tooltip", help="message")

    ff.text(body="This is a sample text 1")
    ff.text(body="This is a a second sample text 2 with a tool tip", help="haaha... the tool tip is working")

    content = ff.root.render()
    content = prettify(content)
    save_as_html("./tests/index.html", content)
    # print(content)
    
'''
    content = div(content=[
        h1("This is a heading", cls="heading"),
        img(src="https://example.com/image.png", alt="An example image", cls="image"),
        p("This is a paragraph with a "),
        div("This is a sample div with a text")],
        cls="container", id="container_id"
    )

    content = prettify(content)
    print(content)

    print(50*"=")


    content = html(
        div(
            h1("This is a heading", cls="heading"),
            img(src="https://example.com/image.png", alt="An example image", cls="image"),
            a("this is the body", cls="link", href="reference-link"),
            cls="container-new", id="container_id",
        )
    )
    content = prettify(content)
    print(content)
'''