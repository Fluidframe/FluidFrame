import shutil
import subprocess, json
from pathlib import Path

def run_command(command, cwd=None):
    try:
        subprocess.run(command, check=True, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
        print(f"Command: {e.cmd}")
        
def is_command_available(command):
    """Check if a command is available in the PATH."""
    return shutil.which(command) is not None

# def setup_node_environment(library_root):
#     """Set up Node environment and install packages in the library folder."""
#     if is_command_available('nodeenv'):
#         print("Setting up Node environment using nodeenv...")
#         run_command("poetry run nodeenv -p", cwd=library_root)
#     else:
#         print("nodeenv not found. Skipping nodeenv setup.")

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

def init_project(project_root, library_root):
    """Initialize a new FluidFrame project."""
    # Create a new package.json in the project directory
    run_command("npm init -y", cwd=project_root)
     
    # Read the library's package.json
    with open(library_root / 'package.json', 'r') as f:
        library_package = json.load(f)
    
    # Read the project's package.json
    with open(project_root / 'package.json', 'r') as f:
        project_package = json.load(f)
    
    # Merge the dependencies
    project_package['dependencies'] = {
        **project_package.get('dependencies', {}),
        **library_package.get('dependencies', {})
    }
    
    # Write the updated package.json back to the project directory
    with open(project_root / 'package.json', 'w') as f:
        json.dump(project_package, f, indent=2)
    
    # Install the dependencies in the project directory
    run_command("npm install", cwd=project_root)
    
    print(f"Initialized a new FluidFrame project in {project_root}")