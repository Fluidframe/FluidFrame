from typing import Optional
from fluidframe.core import span, div

def add_tooltip(id: str, message: str, cls: str) -> str:
    return span(message, cls=f"{cls} tooltip-content", tooltip_target=f"#{id}")

def copy_code(id: str) -> str:
    return f"copyCodeToClipboard('{id}')"