from fluidframe.styling.base_stylings import Style
from typing import List, Dict, Union, Optional, Tuple



class BootstrapStyle(Style):
    def __init__(self, theme: str | None = None) -> None:
        super().__init__(theme, "bootstrap")
   

