from uuid import uuid4
from jinja2 import Template
from abc import ABC, abstractmethod
from starlette.routing import Route
from typing import Optional, Any, Callable
from typing import List, Optional, Union, Tuple
from starlette.templating import Jinja2Templates
from fluidframe.components.base_components import (
    StatelessComponent, Component, RootComponent
)

class Text(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None, inline:Optional[bool]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        self.inline = inline
        
    def render(self) -> str:
        template = Template("""
        <div class="relative">
            <div id="{{ id }}" class="inline-block">
                <p class="text-sm text-gray-900 dark:text-white" {% if help %} data-tooltip-target="{{ tooltip_id }}" {% endif %}> {{ body }} </p>
                {% if help %}
                <div id="{{ tooltip_id }}" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
                    {{ help }}
                    <div class="tooltip-arrow" data-popper-arrow></div>
                </div>
                {% endif %}
            </div>
        </div>""")
        return template.render({
            'id': self.id,
            "body": self.body,
            "help": self.help,
            "inline": self.inline,
            "tooltip_id": f"{self.id}-tooltip",
        })
        

class Title(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        """
        Args:
            parent (Component|RootComponent): The parent or root component object.
            body (str): The text to be displayed as the title.
            help (Optional[str], optional): If provided a message it will be shown as a tooltip message when hovered over the component.
        """
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        template = Template("""
        <div class="relative">
            <div id="{{ id }}" class="inline-block">
                <h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white" {% if help %} data-tooltip-target="{{ tooltip_id }}" {% endif %}> {{ body }} </h1>
                {% if help %}
                <div id="{{ tooltip_id }}" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
                    {{ help }}
                    <div class="tooltip-arrow" data-popper-arrow></div>
                </div>
                {% endif %}
            </div>
        </div>""")
        return template.render({
            'id': self.id,
            "body": self.body,
            "help": self.help,
            "tooltip_id": f"{self.id}-tooltip",
        })
                
 
class Header(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        template = Template("""
        <div class="relative">
            <div id="{{ id }}" class="inline-block">
                <h2 class="text-4xl text-gray-900 font-bold dark:text-white" {% if help %} data-tooltip-target="{{ tooltip_id }}" {% endif %}> {{ body }}</h2>
                {% if help %}
                <div id="{{ tooltip_id }}" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
                    {{ help }}
                    <div class="tooltip-arrow" data-popper-arrow></div>
                </div>
                {% endif %}
            </div>
        </div>""")
        return template.render({
            'id': self.id,
            "body": self.body,
            "help": self.help,
            "tooltip_id": f"{self.id}-tooltip",
        })
    
    
class SubHeader(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        template = Template("""
        <div class="relative">
            <div id="{{ id }}" class="inline-block">
                <h4 class="text-2xl text-gray-900 font-bold dark:text-white" {% if help %} data-tooltip-target="{{ tooltip_id }}" {% endif %}> {{ body }}</h4>
                {% if help %}
                <div id="{{ tooltip_id }}" role="tooltip" class="absolute z-10 invisible inline-block px-3 py-2 text-sm font-medium text-white transition-opacity duration-300 bg-gray-900 rounded-lg shadow-sm opacity-0 tooltip dark:bg-gray-700">
                    {{ help }}
                    <div class="tooltip-arrow" data-popper-arrow></div>
                </div>
                {% endif %}
            </div>
        </div>""")
        return template.render({
            'id': self.id,
            "body": self.body,
            "help": self.help,
            "tooltip_id": f"{self.id}-tooltip",
        })
  
  
class Image(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], image: str, caption: Optional[str]=None, width: Optional[int]=None, use_column_width: Optional[str]=None, output_format: Optional[str]=None) -> None:
        super().__init__(parent)
        self.image = image
        self.width = width
        self.caption = caption
        self.output_format = output_format
        self.use_column_width = use_column_width
        
    def render(self) -> str:
        pass
                 

class Markdown(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Latex(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Code(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass


class Audio(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Video(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    

class Diagram(StatelessComponent):
    def __init__(self, parent: Union['Component', RootComponent], body: str, help: Optional[str]=None) -> None:
        super().__init__(parent)
        self.body = body
        self.help = help
        
    def render(self) -> str:
        pass
    
