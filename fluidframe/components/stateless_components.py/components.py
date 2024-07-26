from uuid import uuid4
from jinja2 import Template
from typing import List, Optional
from abc import ABC, abstractmethod
from starlette.routing import Route
from typing import Optional, Any, Callable
from starlette.templating import Jinja2Templates
from fluidframe.components.base_components import (
    LayoutComponent, StatelessComponent, Component
)

class Text(StatelessComponent):
    def __init__(self, text: str, key: Optional[str] = None) -> None:
        super().__init__(key=key, content=text)
        
    def render(self) -> str:
        template = Template("""<div> {{ text }} </div>""")
        return template.render({"text": self.content})
    
class Column(LayoutComponent):
    def __init__(self, key: Optional[str] = None, children: List[Component] = None) -> None:
        super().__init__(key)
        self.children = children or []