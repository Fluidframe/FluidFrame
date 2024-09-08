import json, os
import hashlib, re
from uuid import uuid4
from bs4 import BeautifulSoup
from fluidframe.config import get_lib_path
from fluidframe.public import js_bundle as public_files


page_404 = None

def get_404_page():
    global page_404
    if page_404 is None:
        with open(get_lib_path(os.path.join("public", public_files.n_404_html)), 'r') as f:
            page_404 = f.read()
    return page_404

def prettify(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    html_string = soup.prettify()
    lines = html_string.split('\n')
    html_string = '\n'.join(' ' * (len(line) - len(line.lstrip())) * 2 + line.lstrip() for line in lines)
    return re.sub(r'\n\s*\n', '\n\n', html_string)

def check_if_html(text: str) -> bool:
    html_pattern = r'<[a-z]+(?:\s+[a-z-]+(?:=(?:"[^"]*"|\'[^\']*\'))?)*\s*(?:/>|>[^<]*</[a-z]+>|>(?:(?!<[a-z]+).)*</[a-z]+>)'
    if re.search(html_pattern, text, re.IGNORECASE | re.DOTALL):
        return True
    else:
        return False
    
def remove_outer_div(html_string: str):
    # Regex to match the outermost div tag and extract its contents
    pattern = r'^<div[^>]*>(.*)</div>$'
    if match := re.match(pattern, html_string, re.DOTALL):
        return match[1].strip()
    return html_string
    
def update_outer_div(html: str, attributes: dict):
    new_string = []
    for k, v in attributes.items():
        new_string.append(f'{k}="{v}"')
    input_string = ' '.join(new_string)
    tag_split = html.split(">", maxsplit=1)
    return f"{tag_split[0]} {input_string}>{''.join(tag_split[1:])}"

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
