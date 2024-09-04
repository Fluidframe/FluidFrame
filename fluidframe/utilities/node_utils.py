import os
import subprocess, json
from fluidframe.utilities.package_manager import generate_source_map
from fluidframe.config import FLUIDFRAME_BUILD_DIR, FLUIDFRAME_SRC_DIR
from fluidframe.utilities.tailwind_utils import generate_tailwind_config
from fluidframe.utilities.boilerplate import generate_fluidframe_boilerplate, generate_fluidframe_component_boilerplate


def check_node_installed():
    """Check if Node.js is installed."""
    try:
        subprocess.run(['node', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return True

def install_node():
    # TODO: Add automatic installation of nodejs
    """Install Node.js based on the operating system."""
    print("Node.js not found. Please install Node.js from `https://nodejs.org/en/download/package-manager`")
    print("You may need to manually download and install Node.js.")

def create_fresh_package_json(project_name, fluidframe_dir):
    """Create a fresh package.json file for the user's project."""
    package_json = {
        "name": project_name,
        "version": "1.0.0",
        "description": f"A FluidFrame project named {project_name}",
        "main": "index.js",
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "keywords": [],
        "author": "",
        "license": "ISC",
        "dependencies": {}
    }
    
    package_json_path = os.path.join(fluidframe_dir, 'package.json')
    with open(package_json_path, 'w') as f:
        json.dump(package_json, f, indent=2)

def init_project(args):
    """
    Initializes a FluidFrame project with the given project name.

    Args:
        args (object): An object containing the project name.

    Returns:
        None

    Initializes the project directory structure, creates package.json,
    generates tailwind.config.js, creates input.css, installs dependencies, and builds initial CSS.
    """
    project_name = args.project_name
    current_dir = os.getcwd()
    
    src_dir = os.path.join(current_dir, FLUIDFRAME_SRC_DIR)
    fluidframe_dir = os.path.join(current_dir, FLUIDFRAME_BUILD_DIR)

    print(f"Initializing FluidFrame project: {project_name}")

    # Create fluidbuil directory if it doesn't exist
    os.makedirs(fluidframe_dir, exist_ok=True)
        
    # Create src directory if it doesn't exist
    os.makedirs(src_dir, exist_ok=True)
    
    
    # Create fluidframe boilerplate file
    generate_fluidframe_boilerplate(src_dir)
    generate_fluidframe_component_boilerplate(src_dir)

    # Create fresh package.json for the user's project
    create_fresh_package_json(project_name, fluidframe_dir)

    # Create input.css
    input_css_path = os.path.join(fluidframe_dir, 'input.css')
    with open(input_css_path, 'w') as f:
        f.write('@tailwind base;\n@tailwind components;\n@tailwind utilities;\n')
        
    # Generate tailwind.config.js
    generate_tailwind_config(fluidframe_dir)

    # Change to fluidframe directory
    os.chdir(fluidframe_dir)

    # Install dependencies
    npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
    try:
        subprocess.run([npm_command, 'install'], check=True)
        print("Successfully installed dependencies")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return

    # Run initial Tailwind build
    npx_command = 'npx.cmd' if os.name == 'nt' else 'npx'
    try:
        subprocess.run([npx_command, 'tailwindcss', '-i', 'input.css', '-o', 'dist/output.css'], check=True)
        print("Successfully built initial CSS")
    except subprocess.CalledProcessError as e:
        print(f"Error building initial CSS: {e}")

    print(f"FluidFrame project '{project_name}' initialized successfully.")
    print("To build css with tailwind, run:")
    print(f"fluidframe build_tailwind")
    generate_source_map(fluidframe_dir)

    # Change back to original directory
    os.chdir(current_dir)

def install(args):
    """
    Installs a Node.js package in the FluidFrame project.

    Args:
        args (object): An object containing the package name to be installed.

    Returns:
        None

    Installs the specified Node.js package in the FluidFrame project directory.
    If the FluidFrame directory does not exist, it prints an error message and returns.
    """
    package_name = args.package_name
    fluidframe_dir = os.path.join(os.getcwd(), FLUIDFRAME_BUILD_DIR)

    if not os.path.exists(fluidframe_dir):
        print(f"Error: FluidFrame's package directory `{FLUIDFRAME_BUILD_DIR}` not found. Please run 'fluidframe init <project_name>' first.")
        return

    os.chdir(fluidframe_dir)

    print(f"Installing Node.js package: {package_name}")

    npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
    try:
        subprocess.run([npm_command, 'install', package_name], check=True)
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")
        
    generate_source_map(fluidframe_dir)
    
    os.chdir(os.getcwd())
    
def uninstall(args):
    """
    Uninstalls a Node.js package in the FluidFrame project.

    Args:
        args (object): An object containing the package name to be uninstalled.

    Returns:
        None

    Uninstalls the specified Node.js package in the FluidFrame project directory.
    If the FluidFrame directory does not exist, it prints an error message and returns.
    """
    package_name = args.package_name
    fluidframe_dir = os.path.join(os.getcwd(), FLUIDFRAME_BUILD_DIR)

    if not os.path.exists(fluidframe_dir):
        print(f"Error: FluidFrame's package directory `{FLUIDFRAME_BUILD_DIR}` not found. Please run 'fluidframe init <project_name>' first.")
        return

    os.chdir(fluidframe_dir)

    print(f"Uninstalling Node.js package: {package_name}")

    npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
    try:
        subprocess.run([npm_command, 'uninstall', package_name], check=True)
        print(f"Successfully uninstalled {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error uninstalling {package_name}: {e}")
        
    generate_source_map(fluidframe_dir)
    
    os.chdir(os.getcwd())