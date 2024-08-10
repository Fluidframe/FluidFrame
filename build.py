import subprocess
from pathlib import Path
from fluidframe.utilities.tailwind_utils import generate_local_tailwind_config
from fluidframe.utilities.node_utils import check_node_installed, install_node

def run_command(command, cwd=None):
    process = subprocess.Popen(command, shell=True, cwd=cwd)
    process.wait()
    
def tailwind_watch():
    build_tailwind(Path.cwd(), Path(__file__).parent)

def build_tailwind(project_root, library_root):
    config_path = project_root / "tailwind.config.js"
    input_path = library_root / "fluidframe" / "static" / "input.css"
    output_path = library_root / "fluidframe" / "static" / "dist" / "output.css"
    run_command(f"npx tailwindcss -c {config_path} -i {input_path} -o {output_path}")

def build_cython(library_root):
    run_command(f"python {library_root / 'setup.py'} build_ext --inplace", cwd=library_root)

if __name__ == "__main__":
    project_root = Path.cwd()
    library_root = Path(__file__).parent
    
    if not check_node_installed():
        install_node()
    generate_local_tailwind_config(project_root, library_root)
    build_tailwind(project_root, library_root)
    build_cython(library_root)

