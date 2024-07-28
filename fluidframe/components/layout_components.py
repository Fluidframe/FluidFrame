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
    
    def _parse_size(self, size: Union[str, float]) -> str:
        return f"{int(size * 100)}%" if isinstance(size, float) else size
    
    def _get_width_class(self) -> str:
        if self.width.endswith('%'):
            percentage = int(self.width[:-1])
            return f"w-{int(percentage / 100 * 12)}/12"
        return f"w-{self.width}"
    
    def _get_height_class(self) -> str:
        if self.height.endswith('%'):
            return f"h-{self.height[:-1]}"
        return f"h-{self.height}"
    
    def _get_vertical_alignment_class(self) -> str:
        alignment_map = {
            "top": "items-start",
            "bottom": "items-end",
            "center": "items-center",
        }
        return alignment_map.get(self.vertical_alignment, "items-start")
    
    def render(self) -> str:
        template = Template("""
        <div id="{{ id }}" class="flex flex-col {{ width_class }} {{ height_class }} {{ vertical_alignment_class }}">
            {% for child in children %}
            {{ child }}
            {% endfor %}
        </div>
        """)
        return template.render({
            "id": self.id,
            "width_class": self._get_width_class(),
            "height_class": self._get_height_class(),
            "children": [child.render() for child in self.children],
            "vertical_alignment_class": self._get_vertical_alignment_class(),
        })
    