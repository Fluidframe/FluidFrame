import json
from typing import Optional, List
from fluidframe.core import script

def requires(scripts: Optional[List[str]]=None, styles: Optional[List[str]]=None) -> str:
    styles = [] if styles is None else styles
    scripts = [] if scripts is None else scripts
    return script(f"loadDependencies({{scripts: {json.dumps(scripts)}, styles: {json.dumps(styles)}}});")
