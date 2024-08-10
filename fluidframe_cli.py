import argparse
from pathlib import Path
from fluidframe.utilities.node_utils import init_project

def main():
    parser = argparse.ArgumentParser(description='FluidFrame Project Management')
    parser.add_argument('--init', action='store_true', help='Initialize a new FluidFrame project')
    args = parser.parse_args()
    
    # Assume the user is running this script from their project directory
    project_root = Path.cwd()
    
    # The path to the FluidFrame library root (adjust as needed)
    library_root = Path(__file__).parent
    
    if args.init:
        init_project(project_root, library_root)
        print(f"FluidFrame project initialized in {project_root}")
    else:
        print("No action specified. Use --init to initialize a new FluidFrame project.")

if __name__ == "__main__":
    main()