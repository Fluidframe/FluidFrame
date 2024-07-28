from uuid import uuid4
from jinja2 import Template
from abc import ABC, abstractmethod
from starlette.routing import Route
from typing import List, Optional, Union
from typing import Optional, Any, Callable
from starlette.templating import Jinja2Templates
from fluidframe.components.base_components import (
    StatelessComponent, Component, RootComponent
)

class Text(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        self.root_component.css_framework
        
    def render(self) -> str:
        template = Template("""<span id="{{ id }}" > {{ text }} </span>""")
        return template.render({"text": self.body, 'id': self.id})
    
