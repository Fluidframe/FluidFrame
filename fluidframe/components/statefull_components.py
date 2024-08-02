from uuid import uuid4
from jinja2 import Template
from abc import ABC, abstractmethod
from starlette.routing import Route
from typing import List, Optional, Union
from typing import Optional, Any, Callable
from starlette.templating import Jinja2Templates
from fluidframe.components.base_components import (
    StatefulComponent, Component, Root
)
from fluidframe.components.view_components import Text


class Button(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    

class TextInput(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    

class TextArea(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    

class Slider(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class SelectBox(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class MultiSelectBox(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class CheckBox(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class Radio(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class DateInput(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class TimeInput(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class FileUploader(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class ColorPicker(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class DownloadButton(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass


class Progress(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
    
class Spinner(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    

class Status(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    

class Form(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass