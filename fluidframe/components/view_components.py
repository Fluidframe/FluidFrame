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


TEMPLATE_FILE= "view_components.html" 


class Text(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return self.template.module.text_component(
            id=self.id,
            body=self.body,
            help=self.help,
            tooltip_id=f"tooltip-{self.id}",
        )
        

class Title(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        """
        Args:
            parent (Component|RootComponent): The parent or root component object.
            body (str): The text to be displayed as the title.
            help (Optional[str], optional): If provided a message it will be shown as a tooltip message when hovered over the component.
        """
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return self.template.module.title_component(
            id=self.id,
            body=self.body,
            help=self.help,
            tooltip_id=f"tooltip-{self.id}",
        )
                
 
class Header(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return self.template.module.header_component(
            id=self.id,
            body=self.body,
            help=self.help,
            tooltip_id=f"tooltip-{self.id}",
        )
    
    
class SubHeader(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        return self.template.module.subheader_component(
            id=self.id,
            body=self.body,
            help=self.help,
            tooltip_id=f"tooltip-{self.id}",
        )
  
  
class Image(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], image: str, caption: Optional[str]=None, width: Optional[int]=None, use_column_width: Optional[str]=None, output_format: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.image = image
        self.width = width
        self.caption = caption
        self.output_format = output_format
        self.use_column_width = use_column_width
        
    def render(self) -> str:
        pass
                 

class Markdown(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Latex(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Code(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass


class Audio(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Video(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Diagram(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent, TEMPLATE_FILE)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    
