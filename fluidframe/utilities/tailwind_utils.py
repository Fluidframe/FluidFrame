import os
import subprocess
import importlib.util
from fluidframe.utils import get_lib_path
from fluidframe.config import FLUIDFRAME_BUILD_DIR


def tailwind_build(args={}):
    """
    Builds the Tailwind CSS stylesheets for the FluidFrame project.

    This function changes the current working directory to the FluidFrame build directory
    and runs the Tailwind CSS build command using the `subprocess.run` function.
    The input CSS file is specified as 'input.css' and the output CSS file is specified as
    'dist/output.css'. If the FluidFrame build directory does not exist, an error message is
    printed and the function returns without building the stylesheets.

    Parameters:
        None

    Returns:
        None

    Raises:
        subprocess.CalledProcessError: If there is an error during the Tailwind CSS build process.
        KeyboardInterrupt: If the build process is interrupted by the user.

    """
    fluidframe_dir = os.path.join(os.getcwd(), FLUIDFRAME_BUILD_DIR)
    if not os.path.exists(fluidframe_dir):
        print(f"Error: FluidFrame's package directory {FLUIDFRAME_BUILD_DIR} not found. Please run 'fluidframe init <project_name>' first.")
        return

    os.chdir(fluidframe_dir)
    try:
        subprocess.run(['npx', 'tailwindcss', '-i', 'input.css', '-o', 'dist/output.css'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error on Tailwind build process: {e}")
    except KeyboardInterrupt:
        print("Tailwind build process stopped.")
    os.chdir(os.getcwd())

def get_package_path():
    """Get the absolute path to the installed FluidFrame package."""
    spec = importlib.util.find_spec("fluidframe")
    if spec is None:
        raise ImportError("FluidFrame package not found")
    return os.path.dirname(spec.origin)

def generate_tailwind_config(fluidframe_dir):
    """
    Generates a Tailwind configuration file for a FluidFrame project.

    Parameters:
    fluidframe_dir (str): The directory path of the FluidFrame project.

    Returns:
    None

    The function generates a tailwind.config.js file in the specified FluidFrame project directory.
    It includes the library files and user project files in the content section of the configuration.
    """
    package_path = get_lib_path()
    
    library_files = [
        os.path.join(package_path, "components", "**", "*.py"),
        os.path.join(package_path, "public", "**", "*.js"),
        os.path.join(package_path, "core", "**", "*.py"),
        os.path.join(package_path, "templates", "**", "*.html"),
    ]

    config_content = f"""
module.exports = {{
  content: [
    // Library files
{''.join([f"    '{f}',\n" for f in library_files])}
    // User project files
    '../src/**/*.{{html,py}}'
  ],
  theme: {{
    extend: {{}},
  }},
  plugins: [],
}}
"""

    config_path = os.path.join(fluidframe_dir, 'tailwind.config.js')
    with open(config_path, 'w') as f:
        f.write(config_content)

    print(f"Generated tailwind.config.js at {config_path}")