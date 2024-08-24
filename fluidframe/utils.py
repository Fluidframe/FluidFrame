from pathlib import Path
from typing import Optional

def get_lib_path(relative_path: Optional[str]=None) -> str:
    if relative_path is None:
        return str(Path(__file__).resolve().parent)
    else:
        return str(Path(__file__).resolve().parent / relative_path)