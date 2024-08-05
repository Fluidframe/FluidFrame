from uuid import uuid4
from jinja2 import Template
from abc import ABC, abstractmethod
from starlette.routing import Route
from typing import Optional, Any, Callable
from typing import List, Optional, Union, Tuple
from starlette.templating import Jinja2Templates
from fluidframe.components.base_components import (
    StatelessComponent, Component, Root
)
from fluidframe.utilities.tags import div, p, h1, h2, h4
# from fluidframe.scripts.utils import add_tooltip



class Text(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return div(
            div(
                p(self.body, cls="text-sm text-gray-900 dark: text-white"), 
                cls="inline-block"
            ), id=self.id, cls="relative"
        )
        

class Title(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return div(
            div(
                h1(self.body, cls="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"),
                cls="inline-block",
            ), id=self.id, cls="relative",
        )
                
 
class Header(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return div(
            div(
                h2(self.body, cls="text-4xl text-gray-900 font-bold dark:text-white") ,
                cls="inline-block"
            ), id=self.id, cls="relative",
        )
    
    
class SubHeader(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return div(
            div(
                h4(self.body, cls="text-2xl text-gray-900 font-bold dark:text-white"),
                cls="inline-block",
            ), id=self.id, cls="relative",
        )
  
  
class Image(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], image: str, caption: Optional[str]=None, width: Optional[int]=None, use_column_width: Optional[str]=None, output_format: Optional[str]=None) -> None:
        super().__init__(parent)
        self.image = image
        self.width = width
        self.caption = caption
        self.output_format = output_format
        self.use_column_width = use_column_width
        
    def render(self) -> str:
        pass
                 

class Markdown(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Latex(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Code(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass


class Audio(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Video(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Diagram(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    
