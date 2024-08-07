from typing import Optional, Union
from fluidframe.core import div, p, h1, h2, h4
from fluidframe.components.stateless.utils import with_tooltip
from fluidframe.core.components import StatelessComponent, Component, Root



class Text(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                with_tooltip(
                    p(self.body, cls="text-sm text-gray-900 dark: text-white"),
                    message=self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"
                ), id=self.id, cls="relative"
            )
        return div(
            div(
                p(self.body, cls="text-sm text-gray-900 dark: text-white"), 
                cls="inline-block"
            ), id=self.id, cls="relative"
        )
        

class Title(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                with_tooltip(
                    h1(self.body, cls="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"),
                    message=self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"
                ), id=self.id, cls="relative"
            )
        return div(
            div(
                h1(self.body, cls="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"),
                cls="inline-block",
            ), id=self.id, cls="relative",
        )
                
 
class Header(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                with_tooltip(
                    h2(self.body, cls="text-4xl text-gray-900 font-bold dark:text-white"),
                    message=self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"
                ), id=self.id, cls="relative"
            )
        return div(
            div(
                h2(self.body, cls="text-4xl text-gray-900 font-bold dark:text-white"),
                cls="inline-block"
            ), id=self.id, cls="relative",
        )
    
    
class SubHeader(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                with_tooltip(
                    h4(self.body, cls="text-2xl text-gray-900 font-bold dark:text-white"),
                    message=self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"
                ), id=self.id, cls="relative"
            )
        return div(
            div(
                h4(self.body, cls="text-2xl text-gray-900 font-bold dark:text-white"),
                cls="inline-block",
            ), id=self.id, cls="relative",
        )
                 

class Markdown(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Latex(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Code(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Diagram(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass