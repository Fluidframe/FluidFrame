import hashlib, re
import string, json
from typing import List
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
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
    with open(file_path, 'w') as file:
        file.write(html_string)
    print(f"HTML content saved to {file_path}")


class FixedLengthIDGenerator:
    def __init__(self, fixed_length=16):
        self.generated_ids = set()
        self.fixed_length = fixed_length
        self.base_chars = string.ascii_lowercase + string.digits

    def base_encode(self, number, base_chars, length):
        base = len(base_chars)
        encoded = []
        while number and len(encoded) < length:
            number, rem = divmod(number, base)
            encoded.append(base_chars[rem])
        while len(encoded) < length:
            encoded.append(base_chars[0])
        return ''.join(reversed(encoded))

    def generate_fixed_length_code(self, name):
        hash_object = hashlib.sha1(name.encode())
        hash_code = int(hash_object.hexdigest(), 16)
        return self.base_encode(hash_code, self.base_chars, self.fixed_length)
    
    def generate_unique_id(self, component_path: List[str]):
        path_string = '/'.join(component_path)
        base_id = self.generate_fixed_length_code(path_string)
        unique_id = base_id
        extra_index = 0
        while unique_id in self.generated_ids:
            extra_code = self.base_encode(extra_index, self.base_chars, 1)
            unique_id = f"{base_id[:-1]}{extra_code}"
            extra_index += 1
        
        self.generated_ids.add(unique_id)
        return unique_id
    


class UniqueIDGenerator:
    def __init__(self):
        self.generated_ids = set()
        self.base_chars = string.ascii_lowercase + string.digits

    def base_encode(self, number, base_chars):
        if number == 0:
            return base_chars[0]
        base = len(base_chars)
        encoded = []
        while number:
            number, rem = divmod(number, base)
            encoded.append(base_chars[rem])
        return ''.join(reversed(encoded))
    
    def generate_base_code(self, name, length=4):
        hash_object = hashlib.sha1(name.encode())
        hash_code = int(hash_object.hexdigest(), 16)
        return self.base_encode(hash_code, self.base_chars)[:length]
    
    def generate_unique_id(self, component_path):
        if len(component_path)==1:
            unique_id=component_path[0]
        else:
            base_codes = [self.generate_base_code(name) for name in component_path]
            base_id = '-'.join(base_codes)
            unique_id = f'{base_id}-{component_path[-1]}'
        extra_index = 0
        while unique_id in self.generated_ids:
            extra_code = self.base_encode(extra_index, self.base_chars)
            unique_id = f"{base_id}-{extra_code}"
            extra_index += 1
        self.generated_ids.add(unique_id)
        return unique_id
    
    
    
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
    # Example usage
    generator = UniqueIDGenerator()
    path1 = ["root", "column1", "button1"]
    path2 = ["root", "column1", "button2"]
    path3 = ["root", "column1", "button1"]  # Intentional conflict with path1

    id1 = generator.generate_unique_id(path1)
    id2 = generator.generate_unique_id(path2)
    id3 = generator.generate_unique_id(path3)  # Should handle conflict

    print(id1)  # Example output: "kthv-oqd2-pqdf"
    print(id2)  # Example output: "kthv-oqd2-pqde"
    print(id3)  # Example output: "kthv-oqd2-pqdf-0" or similar

    ##########################################################################

    # Example usage
    generator = FixedLengthIDGenerator(fixed_length=12)
    path1 = ["root", "column1", "button1"]
    path2 = ["root", "column1", "button2"]
    path3 = ["root", "column1", "button1"]  # Intentional conflict with path1

    id1 = generator.generate_unique_id(path1)
    id2 = generator.generate_unique_id(path2)
    id3 = generator.generate_unique_id(path3)  # Should handle conflict

    print(id1)  # Example output: "zshc0mgszl"
    print(id2)  # Example output: "9e6rifu6h0"
    print(id3)  # Example output: "zshc0mgsza" or similar
    
    ##########################################################################
    
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
