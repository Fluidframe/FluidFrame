import os
from typing import List

__version__ = "0.0.1"

TITLE = "FluidFrame"

FLUIDFRAME_SCRIPTS_DIR = "src"
FLUIDFRAME_BUILD_DIR = "fluidpack"

PUBLIC_DIR = "lib_static"
MODULES_DIR = "lib_modules"

STYLES = [
    "style/dist/output.css"
]

SCRIPTS = [
    # f"{MODULES_DIR}/prismjs/prism.js",
    f"{MODULES_DIR}/htmx.org/dist/htmx.min.js",
    f"{PUBLIC_DIR}/scripts/dependency_manager.js",
]

HOT_RELOAD_SCRIPT = f"{PUBLIC_DIR}/scripts/hot_reload.js"


