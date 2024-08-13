import os
from typing import List

__version__ = "0.0.1"

TITLE = "FluidFrame"

FLUIDFRAME_SCRIPTS_DIR = "src"
FLUIDFRAME_BUILD_DIR = "fluidpack"

NODE_MODULE = "modules"
STATIC = "lib_static"

STYLES = [
    "style/dist/output.css"
]

SCRIPTS = [
    "modules/htmx.org/dist/htmx.min.js",
    "lib_static/dependency_manager.js",
]

HOT_RELOAD_SCRIPT = "lib_static/hot_reload.js"