import subprocess
from pathlib import Path
from setuptools import Extension
from Cython.Build import cythonize
from fluidframe.utilities.tailwind_utils import generate_local_tailwind_config


def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    process.wait()
    
def tailwind_watch():
    build_tailwind(Path.cwd(), Path(__file__).parent)

def build_tailwind(project_root, library_root):
    config_path = project_root / "tailwind.config.js"
    input_path = library_root / "fluidframe" / "static" / "input.css"
    output_path = library_root / "fluidframe" / "static" / "dist" / "output.css"
    run_command(f"npx tailwindcss -c {config_path} -i {input_path} -o {output_path}", cwd=project_root)

def build_cython(library_root):
    extensions = [
        Extension(
            "fluidframe.core.tags.tags",
            [str(library_root / "fluidframe" / "core" / "tags" / "tags.pyx")],
            extra_compile_args=["-O3"], extra_link_args=["-O3"]
        )
    ]
    return cythonize(extensions, language_level="3")

if __name__ == "__main__":
    project_root = Path.cwd()
    library_root = Path(__file__).parent
    # setup_node_environment(library_root)
    generate_local_tailwind_config(project_root, library_root)
    build_tailwind(project_root, library_root)
    build_cython(library_root)

