from typing import Optional, Union, List
from fluidframe.core import div, p, h1, h2, h4
from fluidframe.components.stateless.utils import with_tooltip
from fluidframe.components.stateless.text_components import Text
from fluidframe.core.components import StatelessComponent, Component, Root


class Column(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], width: Union[str, float], height: Union[str, float], vertical_alignment: str="top") -> None:
        super().__init__(parent, None)
        self.width = width
        self.height = height
        self.vertical_alignment = vertical_alignment

    def render(self) -> str:
        pass
    
    
class Container(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, **kwargs) -> None:
        super().__init__(parent, key, **kwargs)
        
    def render(self) -> str:
        pass


class Empty(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, **kwargs) -> None:
        super().__init__(parent, key, **kwargs)
        
    def render(self) -> str:
        return div(id=self.id)
        

class NavBar(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], key: str | None = None, **kwargs) -> None:
        super().__init__(parent, key, **kwargs)
    
    def render(self) -> str:
        pass