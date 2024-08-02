from uuid import uuid4
from jinja2 import Template
from abc import ABC, abstractmethod
from starlette.routing import Route
from typing import List, Optional, Union
from typing import Optional, Any, Callable
from starlette.templating import Jinja2Templates
from fluidframe.components.base_components import (
    LayoutComponent, Component, RootComponent
)
from fluidframe.components.view_components import Text



class Column(LayoutComponent):
    def __init__(self, parent: Union['Component', RootComponent], width: Union[str, float], height: Union[str, float], vertical_alignment: str="top", children: List[Component] = None) -> None:
        super().__init__(parent, None, children)
        self.width = width
        self.height = height
        self.vertical_alignment = vertical_alignment
    
    def text(self, body: str, help: Optional[str]=None) -> Text:
        text = Text(parent=self, body=body, help=help)
        self.add_child(text)
        return text

    def render(self) -> str:
        template = Template("""
        <div id="{{ id }}" class="{{ style_class }}">
            {% for child in children %}
            {{ child }}
            {% endfor %}
        </div>
        """)
        return template.render({
            "id": self.id,
            "style_class": "",
            "children": [child.render() for child in self.children],
        })
    
    
class Container(LayoutComponent):
    def __init__(self, parent: Component | RootComponent, key: str | None = None, children: List[Component] = None, **kwargs) -> None:
        super().__init__(parent, key, children, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class SideBar(LayoutComponent):
    def __init__(self, parent: Component | RootComponent, key: str | None = None, children: List[Component] = None, **kwargs) -> None:
        super().__init__(parent, key, children, **kwargs)
    
    def render(self) -> str:
        pass
    

class Expander(LayoutComponent):
    def __init__(self, parent: Component | RootComponent, key: str | None = None, children: List[Component] = None, **kwargs) -> None:
        super().__init__(parent, key, children, **kwargs)
        
    def render(self) -> str:
        pass


class Empty(LayoutComponent):
    def __init__(self, parent: Component | RootComponent, key: str | None = None, children: List[Component] = None, **kwargs) -> None:
        super().__init__(parent, key, children, **kwargs)
        
    def render(self) -> str:
        return Template("""<div id="{{ id }}"></div""").render(id=self.id)
        

class NavBar(LayoutComponent):
    def __init__(self, parent: Component | RootComponent, key: str | None = None, children: List[Component] = None, **kwargs) -> None:
        super().__init__(parent, key, children, **kwargs)
    
    def render(self) -> str:
        pass