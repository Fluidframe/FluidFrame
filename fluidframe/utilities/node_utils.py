import re, ast
import subprocess, json
from pathlib import Path

def run_command(command, cwd=None):
    try:
        subprocess.run(command, check=True, shell=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
        print(f"Command: {e.cmd}")

def setup_node_environment(library_root):
    """Set up Node environment and install packages in the library folder."""
    run_command("poetry run nodeenv -p", cwd=library_root)
    run_command("npm install", cwd=library_root)

def check_node_installed():
    """Check if Node.js is installed."""
    try:
        subprocess.run(['node', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return True

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

def install_package(package_name, project_root):
    """Install a Node.js package in the project's node_modules."""
    if package_name:
        run_command(f"npm install {package_name}", cwd=project_root)
        print(f"Successfully installed {package_name} in the project's node_modules.")
    else:
        run_command("npm install", cwd=project_root)
        print("Successfully installed all dependencies in the project's node_modules.")

def uninstall_package(package_name, project_root):
    """Uninstall a Node.js package from the project's node_modules."""
    run_command(f"npm uninstall {package_name}", cwd=project_root)
    print(f"Successfully uninstalled {package_name} from the project's node_modules.")

def update_package(package_name, project_root):
    """Update a Node.js package in the project's node_modules."""
    if package_name:
        run_command(f"npm update {package_name}", cwd=project_root)
        print(f"Successfully updated {package_name} in the project's node_modules.")
    else:
        run_command("npm update", cwd=project_root)
        print("Successfully updated all packages in the project's node_modules.")

def run_npm_script(script_name, project_root):
    """Run an npm script from the project's package.json."""
    run_command(f"npm run {script_name}", cwd=project_root)
    print(f"Finished running npm script: {script_name}")


