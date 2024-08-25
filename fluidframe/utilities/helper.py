import json
import hashlib, re
from uuid import uuid4
from typing import List
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from fluidframe.utils import get_lib_path
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.tasklists import tasklists_plugin
from mdit_py_plugins.front_matter import front_matter_plugin



MARKDOWNER = None

def markdown_to_html(markdown_text: str) -> str:
    global MARKDOWNER
    if MARKDOWNER is None:
        MARKDOWNER = MarkdownIt('commonmark', {'linkify': True, 'break': True, 'html': True})
        MARKDOWNER = MARKDOWNER.use(footnote_plugin).use(front_matter_plugin).use(anchors_plugin).use(tasklists_plugin).enable('table')
    return MARKDOWNER.render(markdown_text)

def prettify(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    html_string = soup.prettify()
    lines = html_string.split('\n')
    html_string = '\n'.join(' ' * (len(line) - len(line.lstrip())) * 2 + line.lstrip() for line in lines)
    return re.sub(r'\n\s*\n', '\n\n', html_string)

def save_as_html(file_path, html_string):
    html_string=prettify(html_string)
    file_path=get_lib_path(file_path)
    with open(file_path, 'w') as file:
        file.write(html_string)
    print(f"HTML content saved to {file_path}")

def generate_id(key: str) -> str:
    if key != "root":
        _key = f"{key}-{str(uuid4())[:4]}"
        hash_object = hashlib.sha1(_key .encode())
        hash_code = hash_object.hexdigest()[:6]
        return f"{key}-{hash_code}"
    return "root"
    
    
class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = DotDict(value)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError(f"'DotDict' object has no attribute '{key}'") from e

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as e:
            raise AttributeError(f"'DotDict' object has no attribute '{key}'") from e

    def __dir__(self):
        return self.keys()

    @classmethod
    def from_dict(cls, data: dict):
        if not isinstance(data, dict):
            return data
        return cls({key: cls.from_dict(value) if isinstance(value, dict) else value for key, value in data.items()})

    @classmethod
    def from_json(cls, data: str):
        return DotDict().from_dict(json.loads(data))
   
   

if __name__=="__main__":
    # Example usage:
    data = {
        "name": "Alice",
        "age": 30,
        "address": {
            "city": "Wonderland",
            "postal_code": "12345"
        },
        "preferences": {
            "color": "blue",
            "food": "pizza"
        }
    }
    
    dot_data = DotDict.from_dict(data)

    print(dot_data.name)  # Alice
    print(dot_data.address.city)  # Wonderland
    dot_data.address.city = "New Wonderland"
    print(dot_data.address.city)  # New Wonderland
