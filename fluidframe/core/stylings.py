from abc import ABC, abstractmethod
from fluidframe.utilities.helper import DotDict
from typing import List, Dict, Union, Optional, Tuple



class StyleConfig(DotDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

DEFAULT_STYLING = {
    "font_size": {
        "sm": "text-sm",
        "lg": "text-lg",
        "md": "text-base",
        "xl": "text-xl",
        "2xl": "text-2xl",
    },
    "font_weight": {
        "thin": "font-thin",
        "normal": "font-normal",
        "medium": "font-medium",
        "bold": "font-bold",
        "extrabold": "font-extrabold",
    }
}
    