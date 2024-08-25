import os
from pathlib import Path
from typing import Optional

def get_lib_path(relative_path: Optional[str]=None) -> str:
    base_path = Path(__file__).resolve().parent
    if relative_path is None:
        return str(base_path)
    else:
        # Normalize the relative path to avoid issues with leading separators
        relative_path = relative_path.lstrip("/\\")
        
        # Create a Path object for the relative path
        relative_path_obj = Path(relative_path)
        
        # Combine the base path and relative path
        full_path = base_path / relative_path_obj
        
        # Return the path with the appropriate slash for the current OS
        return str(full_path.as_posix() if os.name != 'nt' else full_path)
