from fluidframe.core import Component
from typing import Union, Callable, Any, Optional


class Image(Component):
    def __init__(self, image: str, caption: Optional[str]=None, width: Optional[int]=None, use_column_width: Optional[str]=None, output_format: Optional[str]=None) -> None:
        super().__init__()
        self.image = image
        self.width = width
        self.caption = caption
        self.output_format = output_format
        self.use_column_width = use_column_width
        
    def render(self) -> str:
        pass
    

class Audio(Component):
    def __init__(self, body: str, help: Optional[str]=None) -> None:
        super().__init__()
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Video(Component):
    def __init__(self, body: str, help: Optional[str]=None) -> None:
        super().__init__()
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass