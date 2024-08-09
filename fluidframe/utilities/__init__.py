from typing import Optional, List
from fluidframe.core import span, script

def add_tooltip(id: str, message: str, cls: str) -> str:
    return span(message, cls=f"{cls} tooltip-content", tooltip_target=f"#{id}")

def copy_code(id: str) -> str:
    return f"copyCodeToClipboard('{id}')"

def highlight_code(id: str, language: Optional[str]=None) -> str:
    if language:
        return script(f"highlightCodeSnippets('{id}', 'code-{language}');")
    return script(f"highlightCodeSnippets('{id}');")

def require_scripts(src: List[str]|str) -> List[str]|str:
    if isinstance(src, str):
        return script(f"checkAndLoadScript('{src}');")
    return script(''.join([f"checkAndLoadScript('{s}'); " for s in src]))

def require_styles(href: List[str]|str) -> List[str]|str:
    if isinstance(href, str):
        return script(f"checkAndLoadStyle('{href}');")
    return script(''.join([f"checkAndLoadStyle('{ref}'); " for ref in href]))