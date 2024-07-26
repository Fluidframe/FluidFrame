from uuid import uuid4
from jinja2 import Template
from typing import List, Optional
from abc import ABC, abstractmethod
from starlette.routing import Route
from contextlib import contextmanager
from typing import Optional, Any, Callable
from starlette.templating import Jinja2Templates


def get_id():
    return str(uuid4())[-8:]

def get_route(parent_route: Optional[str]="/"):
    return f"{parent_route}/{get_id()}"


class Component(ABC):
    def __init__(self, name: Optional[str] = None, key: Optional[str] = None) -> None:
        self.id = get_id()
        self.state: dict = {}
        self.route = get_route()
        self.key = key or self.id
        self.css_backend: Optional[str] = None
        self.name = name or self.__class__.__name__.lower()

    @abstractmethod
    def render(self) -> str:
        pass

    def set_state(self, new_state: dict):
        self.state.update(new_state)

    def get_state(self, key: str, default: Any = None) -> Any:
        return self.state.get(key, default)
    
    
class StatelessComponent(Component):
    """For simple display components that don't need to manage state.

    - text
    - markdown
    - latex
    - title
    - header
    - subheader
    - caption
    - code
    - image
    - audio
    - video
    - diagram
    """
    def __init__(self, key: Optional[str] = None, content: Any = None) -> None:
        super().__init__(key)
        self.content = content


class StatefulComponent(Component):
    """For components that need to manage and update their own state.
    
    - text_input
    - number_input
    - slider
    - select_box
    - multiselect
    - checkbox
    - radio
    - date_input
    - time_input
    - file_uploader
    - color_picker
    """
    def __init__(self, key: Optional[str] = None, initial_state: dict = None) -> None:
        super().__init__(key)
        self.state = initial_state or {}

    @abstractmethod
    def handle_update(self, new_data: Any) -> None:
        pass


class InteractiveComponent(StatefulComponent):
    """For components that respond to user interactions and potentially trigger callbacks.

    - button
    - download_button
    - form
    - progress
    - spinner
    - status
    """
    def __init__(self, key: Optional[str] = None, initial_state: dict = None, on_change: Optional[Callable] = None) -> None:
        super().__init__(key, initial_state)
        self.on_change = on_change

    @abstractmethod
    def handle_interaction(self, data: Any) -> None:
        pass


class LayoutComponent(StatelessComponent):
    """For components that can contain other components.

    - sidebar
    - columns
    - expander
    - container
    - empty
    """
    def __init__(self, key: Optional[str] = None, children: List[Component] = None) -> None:
        super().__init__(key)
        self.children = children or []
        
    def __enter__(self):
        pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def add_child(self, child: Component):
        self.children.append(child)
        
    def get_childrens(self):
        return self.children

    def render(self) -> str:
        return ''.join(child.render() for child in self.children)
    
    
'''
class MyClass:
    _instances = []

    def __init__(self, name=None):
        self.name = name
        MyClass._instances.append(self)

    @classmethod
    def get_instances(cls):
        return cls._instances

    def __enter__(self):
        # Clear the list of instances at the start of the context
        MyClass._instances = []
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # At the end of the context, you can decide whether to clear the instances or keep them
        pass

    def write(self):
        instance = MyClass(name="write")
        return instance

    def text(self):
        instance = MyClass(name="text")
        return instance
'''