import os
import subprocess
import importlib.util
from fluidframe.config import get_lib_path
from fluidframe.config import FLUIDFRAME_BUILD_DIR


def bundle_scripts(args={}):
    fluidframe_dir = os.path.join(os.getcwd(), FLUIDFRAME_BUILD_DIR)
    if not os.path.exists(fluidframe_dir):
        # print(f"Error: FluidFrame's package directory {FLUIDFRAME_BUILD_DIR} not found. Please run 'fluidframe init <project_name>' first.")
        return
    
    os.chdir(fluidframe_dir)
    try:
        npx_command = 'npx.cmd' if os.name == 'nt' else 'npx'
        subprocess.run([npx_command, 'bundle', '--input', args.input, '--output', args.output], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error on script bundling process: {e}")
    except KeyboardInterrupt:
        print("Rollup bundling process stopped.")
    os.chdir(os.getcwd())