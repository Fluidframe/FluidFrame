from typing import Optional, Union
from fluidframe.core import div, p, h1, h2, h4, pre, code, span, button, span, img
from fluidframe.components.stateless.utils import add_tooltip, copy_code
from fluidframe.core.components import StatelessComponent, Component, Root



class Text(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                p(self.body, cls="text-sm text-gray-900 dark: text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative"
            )
           
        return div(
            p(self.body, cls="text-sm text-gray-900 dark: text-white"), 
            id=self.id, cls="relative"
        )
        

class Title(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                h1(self.body, cls="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative"
            )
           
        return div(
            h1(self.body, cls="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"),
            id=self.id, cls="relative"
        )
                
 
class Header(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                h2(self.body, cls="text-4xl text-gray-900 font-bold dark:text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative"
            )
           
        return div(
            h2(self.body, cls="text-4xl text-gray-900 font-bold dark:text-white"),
            id=self.id, cls="relative"
        )
    
    
class SubHeader(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        if self.help:
            return div(
                h4(self.body, cls="text-2xl text-gray-900 font-bold dark:text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative"
            )
           
        return div(
            h4(self.body, cls="text-2xl text-gray-900 font-bold dark:text-white"),
            id=self.id, cls="relative"
        )
        

class Code(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, language: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.language = "" if language is None else language
        
    def render(self) -> str:
        return div(id=self.id, cls="my-5 mx-auto max-w-2xl text-gray-400", i=
            div(cls="rounded-lg shadow-lg", i=
                div(
                    div(cls="flex items-center justify-between p-2 pb-1", i=[
                        span(cls="text-sm text-gray-400 flex justify-content items-center", i=[
                            div(cls="bg-red-500 rounded-full w-2.5 h-2.5 mr-1"),
                            div(cls="bg-yellow-500 rounded-full w-2.5 h-2.5 mr-1"),
                            div(cls="bg-green-500 rounded-full w-2.5 h-2.5 mr-2"),
                            pre(self.language),
                        ]),
                        button(cls="flex items-center text-gray-400 hover:text-white focus:outline-none", onclick=copy_code(self.id), i=[
                            img(src="static/assets/copy_logo.svg", cls="filter invert-[30%] brightness-[10%]"), span(pre("Copy"), cls="text-sm pl-2"), 
                        ])
                    ]),
                    pre(code(self.body, cls=f"language-{self.language}")),
                    cls="bg-[#1c1a19] rounded-lg"
                )
            )
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
    

class Diagram(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass