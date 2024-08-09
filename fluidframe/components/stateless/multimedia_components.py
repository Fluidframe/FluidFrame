from typing import Optional, Union
from fluidframe.utilities import add_tooltip
from fluidframe.core import div, p, h1, h2, h4
from fluidframe.core.components import StatelessComponent, Component, Root


class Image(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], image: str, caption: Optional[str]=None, width: Optional[int]=None, use_column_width: Optional[str]=None, output_format: Optional[str]=None) -> None:
        super().__init__(parent)
        self.image = image
        self.width = width
        self.caption = caption
        self.output_format = output_format
        self.use_column_width = use_column_width
        
    def render(self) -> str:
        pass
    

class Audio(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Video(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass