import json
from typing import Optional, List
from fluidframe.core import span, script

def add_tooltip(id: str, message: str, cls: str) -> str:
    return ''.join([span(message, cls=f"{cls} tooltip-content", tooltip_target=f"#{id}"), script(f"FluidFrameTooltip.init(document.getElementById('{id}'));")])

def copy_code(id: str) -> str:
    return ''.join(["copyCodeToClipboard('", id, "');"])

def highlight_code(id: str, language: Optional[str]=None, theme: Optional[str]="github-dark", show_line_number: bool=False) -> str:
    pass

def requires(scripts: Optional[List[str]]=None, styles: Optional[List[str]]=None) -> str:
    styles = [] if styles is None else styles
    scripts = [] if scripts is None else scripts
    return script(''.join(["loadDependencies({", "scripts:", json.dumps(scripts), ", styles:", json.dumps(styles), "});"]))