import re
from jinja2 import Template
from typing import List, Optional
from starlette.routing import Route
from fluidframe.utils import UniqueIDGenerator
from fluidframe.components.base_components import Component
from starlette.templating import Jinja2Templates

    

class Page:
    def __init__(self, title: str) -> None:
        self.title = title
        self.scripts = [
            "https://cdn.tailwindcss.com",
            "https://unpkg.com/htmx.org@1.7.0",
            "https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.js",
        ]
        self.links = [
            "https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist/flowbite.min.css"
        ]
        self.children: List[Component] = []
        
    def _clean_(self, text):
        # pattern = r'(\s*\n\s*){2,}'
        # cleaned_text = re.sub(pattern, '\n', text)
        # return cleaned_text.strip()
        
        # pattern = r'(\s*\n\s*)+'
        # def repl(match):
        #     return "\n" + match.group().replace('\n', '')
        # cleaned_text = re.sub(pattern, repl, text)
        # cleaned_text = cleaned_text.rstrip('\n')
        # return cleaned_text
        
        def repl(match):
            # Split the match by newlines
            parts = match.group().split('\n')
            longest_whitespace = max(parts, key=lambda x: len(x.strip('\r')))
            return '\n' + longest_whitespace
        pattern = r'(\s*\n\s*)+'
        cleaned_text = re.sub(pattern, repl, text)
        cleaned_text = cleaned_text.rstrip('\n')
        return cleaned_text
        
    def add_child(self, child: Component):
        self.children.append(child)
        
    def add_children(self, children: List[Component]):
        self.children.extend(children)
        
    def render(self) -> str:
        template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title> 
    
    {% for link in links %}
    <link src="{{ link }}">
    {% endfor %}
    
    {% for script in scripts %}
    <script src="{{ script }}"></script>
    {% endfor %}
</head>
<body class="bg-white dark:bg-gray-900">
    <div id="root" class="relative">
        {% for child in children %}
        {{ child }}
        {% endfor %}
    </div>
</body>""")
        html = template.render({
            "title": self.title, 
            "links": self.links,
            "scripts": self.scripts,
            "children": [child.render() for child in self.children],
        })
        return self._clean_(html)
   
   
