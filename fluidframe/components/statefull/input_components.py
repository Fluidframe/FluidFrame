from typing import Union, Callable, Any
from fluidframe.core.components import StatefulComponent, Component, Root


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

class ColorPicker(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
