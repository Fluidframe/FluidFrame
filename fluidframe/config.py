import os
from pathlib import Path
from typing import Optional

__version__ = "0.1.0"

TITLE = "FluidFrame"


PUBLIC_DIR = "lib_static"
MODULES_DIR = "lib_modules"


STYLES = [
    "style/dist/output.css"
]


FLUIDFRAME_SRC_DIR = "src"
FLUIDFRAME_BUILD_DIR = "fluidbuild"


SCRIPTS = [
    f"{MODULES_DIR}/htmx.org/dist/htmx.min.js",
    f"{PUBLIC_DIR}/scripts/dependency_manager.js",
]


HOT_RELOAD_SCRIPT = f"{PUBLIC_DIR}/scripts/hot_reload.js"





def get_lib_path(relative_path: Optional[str]=None) -> str:
    base_path = Path(__file__).resolve().parent
    if relative_path is not None:
        relative_path = relative_path.lstrip("/\\")                        # Normalize the relative path to avoid issues with leading separators
        relative_path_obj = Path(relative_path)                            # Create a Path object for the relative path
        full_path = base_path / relative_path_obj                          # Combine the base path and relative path
        return str(full_path.as_posix() if os.name != 'nt' else full_path) # Return the path with the appropriate slash for the current OS
    return str(base_path)
