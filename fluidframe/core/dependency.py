import json
from typing import Optional, List
from fluidframe.core import script

def requires(scripts: Optional[List[str]|str]=None, styles: Optional[List[str]|str]=None) -> str:
    if styles is None:
        styles = []
    elif isinstance(styles, str):
        styles = [styles]
    if scripts is None:
        scripts = []
    elif isinstance(scripts, str):
        scripts = [scripts]
    return script(f"loadDependencies({{scripts: {json.dumps(scripts)}, styles: {json.dumps(styles)}}});")

def set_dependancies(scripts: Optional[List[str]|str]=None, styles: Optional[List[str]|str]=None) -> str:
    if styles is None:
        styles = []
    elif isinstance(styles, str):
        styles = [styles]
    if scripts is None:
        scripts = []
    elif isinstance(scripts, str):
        scripts = [scripts]
    return json.dumps({"scripts": scripts, "styles": styles})
