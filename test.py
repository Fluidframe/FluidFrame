from typing import Optional
from fluidframe.base import Page
from fluidframe.styling.tailwind import TailwindStyle
from fluidframe.components.view_components import Text
from fluidframe.components.layout_components import Column
from fluidframe.components.base_components import RootComponent



class FluidFrame():
    def  __init__(self, title: str,  css_framework) -> None:
        self.pages = []
        self.page = Page(title)
        self.css_framework = css_framework
        self.root_component = RootComponent(self.css_framework)
    
    def text(self, body: str, help: Optional[str]=None) -> Text:
        text = Text(parent=self.root_component, body=body, help=help)
        self.page.add_child(text)
        return text
        
        
css_framework = TailwindStyle()
ff = FluidFrame(title="Sample page", css_framework=css_framework)

text = ff.text("This is a sample text")
ff.text("This is a a second sample text")

print(ff.page.render())

print(text.path)
