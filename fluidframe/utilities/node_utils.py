import shutil, os
import subprocess, json
from pathlib import Path
from fluidframe.config import FLUIDFRAME_BUILD_DIR, FLUIDFRAME_SCRIPTS_DIR
from fluidframe.utilities.tailwind_utils import generate_tailwind_config


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

def init_project(args):
    """
    Initializes a FluidFrame project with the given project name.

    Args:
        args (object): An object containing the project name.

    Returns:
        None

    Initializes the project directory structure, copies required files, updates package.json,
    generates tailwind.config.js, creates input.css, installs dependencies, and builds initial CSS.
    """
    project_name = args.project_name
    current_dir = os.getcwd()
    src_dir = os.path.join(current_dir, FLUIDFRAME_SCRIPTS_DIR)
    fluidframe_dir = os.path.join(current_dir, FLUIDFRAME_BUILD_DIR)
    utilities_dir = os.path.join(os.path.dirname(__file__), '..', 'utilities')

    print(f"Initializing FluidFrame project: {project_name}")

    # Create fluidframe directory if it doesn't exist
    if not os.path.exists(fluidframe_dir):
        os.makedirs(fluidframe_dir)
        
    # Create src directory if it doesn't exist
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)

    # Copy package.json and package-lock.json from utilities
    shutil.copy(os.path.join(utilities_dir, 'package.json'), fluidframe_dir)
    shutil.copy(os.path.join(utilities_dir, 'package-lock.json'), fluidframe_dir)

    # Update package.json with project name
    package_json_path = os.path.join(fluidframe_dir, 'package.json')
    with open(package_json_path, 'r') as f:
        package_data = json.load(f)
    
    package_data['name'] = project_name
    
    with open(package_json_path, 'w') as f:
        json.dump(package_data, f, indent=2)

    # Generate tailwind.config.js
    generate_tailwind_config(fluidframe_dir)

    # Create input.css
    input_css_path = os.path.join(fluidframe_dir, 'input.css')
    with open(input_css_path, 'w') as f:
        f.write('@tailwind base;\n@tailwind components;\n@tailwind utilities;\n')

    # Change to fluidframe directory
    os.chdir(fluidframe_dir)

    # Install dependencies
    try:
        subprocess.run(['npm', 'install'], check=True)
        print("Successfully installed dependencies")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        return

    # Run initial Tailwind build
    try:
        subprocess.run(['npx', 'tailwindcss', '-i', 'input.css', '-o', 'dist/output.css'], check=True)
        print("Successfully built initial CSS")
    except subprocess.CalledProcessError as e:
        print(f"Error building initial CSS: {e}")

    print(f"FluidFrame project '{project_name}' initialized successfully.")
    print("To build css with tailwind, run:")
    print(f"fluidframe build_tailwind")

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

    try:
        subprocess.run(['npm', 'install', package_name], check=True)
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")
        
    os.chdir(os.getcwd())