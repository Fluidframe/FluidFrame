from typing import Union, Any, Callable
from fluidframe.core.components import StatefulComponent, Component, Root


class Button(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
class DownloadButton(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass
    
class FileUploader(StatefulComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, on_change: Callable[..., Any] | None = None, **kwargs) -> None:
        super().__init__(parent, key, on_change, **kwargs)
        
    def render(self) -> str:
        pass