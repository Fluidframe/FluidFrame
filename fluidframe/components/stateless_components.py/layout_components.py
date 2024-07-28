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



class Column(LayoutComponent):
    def __init__(self, key: Optional[str] = None, children: List[Component] = None) -> None:
        super().__init__(key)
        self.children = children or []