
all=[
    'i', 'a', 'b', 'p', 's', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'dd', 'dl', 'dt', 'em', 'li', 'rp', 'rt', 'ol', 'ul', 'td', 'th', 'tr', 'var', 'nav', 'sub', 'sup', 'svg', 'ins',
    'kbd', 'dfn', 'div', 'del_', 'map_', 'ruby', 'samp', 'slot', 'span', 'html', 'form', 'head', 'abbr', 'main', 'mark', 'math', 'menu', 'body', 'cite', 'code', 'data', 'time_', 'aside',
    'audio', 'style', 'table', 'tbody', 'video', 'small', 'label', 'meter', 'tfoot', 'thead', 'title', 'hgroup', 'select', 'strong', 'legend', 'option', 'output', 'button', 'canvas', 'dialog',
    'figure', 'footer', 'header', 'iframe', 'object_', 'section', 'summary', 'caption', 'address', 'article', 'details', 'fieldset', 'colgroup', 'datalist', 'template', 'textarea', 'noscript',
    'optgroup', 'figcaption', 'blockquote'
]

all_self_closing=[
    'hr', 'br', 'img', 'col', 'wbr', 'area', 'base', 'link', 'meta', 'track', 'embed', 'input_', 'source', 'script', 'menuitem'
]

all_doc = [
f'''
def {tag}(*args, **kwargs) -> str: 
    """**Generate an HTML <{tag}> element.**

    The arguments to this function will be used as the content and attributes of the
    HTML element. Positional arguments will be converted to strings and used as the
    content of the element. Keyword arguments will be used as the attributes of the
    element.

    For example, `{tag}('Hello, world!', id='{tag}-id', cls='greeting-class')` will generate
    an HTML element like `<{tag} id="{tag}-id" class="greeting-class">Hello, world!</{tag}>`.

    **Returns:**
    
        str: The generated HTML element.
    """
    ...
    
'''
for tag in all
]

all_doc_closing = [
f'''
def {tag}(*args, **kwargs) -> str: 
    """**Generate an HTML <{tag}/> element.**

    The arguments to this function will be used as the attributes of the
    HTML element. Keyword arguments will be used as the attributes of the
    element.

    For example, `{tag}( id='{tag}-id', cls='specific-class')` will generate
    an HTML element like `<{tag} id="{tag}-id" class="specific-class"/>`.

    **Returns:**
    
        str: The generated HTML element.
    """
    ...
    
'''
for tag in all_self_closing
]

code = f'''from typing import Callable

def create_element(tag: str, closing_tag: bool = True) -> Callable: 
    """
    Create a function that generates an HTML element with the given tag name.

    When the returned function is called with arguments, it will generate an HTML
    element with the given tag name, using the arguments as the content and attributes
    of the element.

    **Args:**
        - `tag` (str): The name of the HTML tag that the returned function will generate.
        - `closing_tag` (bool, optional): Whether the HTML tag has a closing tag. Defaults to True.

    **Returns:**
        Callable: A function that generates an HTML element with the given tag name.
    """
    ...
    
########
# Tags #
########
{''.join(all_doc)}


#############
# Void Tags #
#############
{''.join(all_doc_closing)}
'''

with open("tags_cython.pyi", 'w') as file:
    file.write(code)