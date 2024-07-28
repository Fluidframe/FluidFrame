from jinja2 import Template
from typing import List, Optional
from starlette.routing import Route
from fluidframe.utils import UniqueIDGenerator
from components.base_components import Component
from starlette.templating import Jinja2Templates

    

class Page:
    def __init__(self, title: str) -> None:
        self.title = title
        self.scripts = [
            "https://cdn.tailwindcss.com",
            "https://unpkg.com/htmx.org@1.7.0",
            "https://cdn.jsdelivr.net/npm/markdown-it/dist/markdown-it.min.js",
        ]
        self.childrens: List[Component] = []
        
    def add_child(self, child: Component):
        self.childrens.append(child)
        
    def add_childrens(self, childrens: List[Component]):
        self.childrens.extend(childrens)
        
    def render(self) -> str:
        html_template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    {% for script in scripts %}
    <script src="{{ script }}"></script>
    {% endfor %}
</head>
<body>
    <div id="root">
        {% for child in childrens %}
        {{ child }}
        {% endfor %}
    </div>
</body>""")
        return html_template.render({
            "title": self.title, 
            "scripts": self.scripts,
            "childrens": [child.render() for child in self.childrens],
        })
   
   
