import json
from typing import Optional, List
from fluidframe.core import span, script

def add_tooltip(id: str, message: str, cls: str) -> str:
    return span(message, id=f"tooltip-{id}", cls=f"{cls}") # , script(f"FluidFrameTooltip.init(document.getElementById('{id}'));")])

def show_tooltip(id: str) -> str:
    return f"showTooltip('{id}', 'tooltip-{id}')"
    
def hide_tooltip(id: str) -> str:
    return f"hideTooltip('tooltip-{id}')"

def copy_code(id: str) -> str:
    return f"copyCodeToClipboard('{id}');"

def highlight_code(id: str, language: Optional[str]=None, theme: Optional[str]="github-dark", show_line_number: bool=False) -> str:
    pass