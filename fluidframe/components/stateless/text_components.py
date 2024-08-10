from html import escape
from typing import Optional, Union
from fluidframe.core.components import StatelessComponent, Component, Root
from fluidframe.core import div, p, h1, h2, h4, pre, code, span, button, span, img
from fluidframe.utilities import add_tooltip, copy_code, requires, show_tooltip, hide_tooltip



class Text(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help 
        self.scripts=["lib_static/tooltip.js"]
        
    def render(self) -> str:
        if self.help:
            return div(
                requires(self.scripts),
                p(self.body, cls="text-sm text-gray-900 dark: text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 mx-5 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative", onmouseenter=show_tooltip(self.id), onmouseleave=hide_tooltip(self.id)
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
        self.scripts=["lib_static/tooltip.js"]
        
    def render(self) -> str:
        if self.help:
            return div(
                requires(self.scripts),
                h1(self.body, cls="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 mx-5 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative", onmouseenter=show_tooltip(self.id), onmouseleave=hide_tooltip(self.id)
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
        self.scripts=["lib_static/tooltip.js"]
        
    def render(self) -> str:
        if self.help:
            return div(
                requires(self.scripts),
                h2(self.body, cls="text-4xl text-gray-900 font-bold dark:text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 mx-5 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative", onmouseenter=show_tooltip(self.id), onmouseleave=hide_tooltip(self.id)
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
        self.scripts=["lib_static/tooltip.js"]
        
    def render(self) -> str:
        if self.help:
            return div(
                requires(self.scripts),
                h4(self.body, cls="text-2xl text-gray-900 font-bold dark:text-white"),
                add_tooltip(self.id, self.help, cls="invisible opacity-0 absolute z-10 mx-5 px-3 py-2 text-sm font-medium text-white bg-gray-900 rounded-lg shadow-sm transition-opacity duration-500"),
                id=self.id, cls="relative", onmouseenter=show_tooltip(self.id), onmouseleave=hide_tooltip(self.id)
            )
           
        return div(
            h4(self.body, cls="text-2xl text-gray-900 font-bold dark:text-white"),
            id=self.id, cls="relative"
        )
        

class Code(StatelessComponent):
    def __init__(self, parent: Union[Component, Root], body: str, language: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.clipboard_image = "lib_static/assets/clipboard.svg"
        self.language = "" if language is None else language.lower()
        self.styles = ["modules/prismjs/plugins/line-numbers/prism-line-numbers.css", "modules/prismjs/themes/prism-okaidia.min.css"]
        self.scripts = ["lib_static/copy_code.js", "modules/prismjs/prism.js", "modules/prismjs/plugins/line-numbers/prism-line-numbers.min.js", f"modules/prismjs/components/prism-{language}.min.js"]
        
    def render(self) -> str:
        return div(id=self.id, cls="max-w-2xl text-gray-400 m-4", i=[
            requires(self.scripts, self.styles),
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
                            img(src=self.clipboard_image, cls="filter invert-[30%] brightness-[10%]"), span(pre("Copy"), cls="text-sm pl-2"), 
                        ])
                    ]),
                    pre(code(escape(self.body), cls=f"line-numbers language-{self.language}")),
                    cls="bg-[#1c1a19] rounded-lg"
                )
            )
        ])
                 

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
