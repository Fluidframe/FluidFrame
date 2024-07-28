from abc import ABC, abstractmethod
from typing import List, Dict, Union, Optional, Tuple

        
        
class Style(ABC):
    def __init__(self, theme: Optional[str] = None, css_framework: str = "tailwind") -> None:
        self.theme = "dark" if theme is None else theme
        self.css_framework = css_framework
        