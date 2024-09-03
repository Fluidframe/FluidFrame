import argparse
from fluidframe.utilities.tailwind_utils import tailwind_build
from fluidframe.utilities.node_utils import init_project, install
from fluidframe.utilities.package_manager import generate_source_map

def map_command(args):
    generate_source_map(root_path=args.folder_path)

def main():
    parser = argparse.ArgumentParser(description='FluidFrame CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize FluidFrame')
    init_parser.add_argument('project_name', help='Name of the project to initialize')
    init_parser.set_defaults(func=init_project)

    # Install command
    install_parser = subparsers.add_parser('install', help='Install a Node.js package')
    install_parser.add_argument('package_name', help='Name of the package to install')
    install_parser.set_defaults(func=install)
    
    # Tailwind build command
    watch_parser = subparsers.add_parser('tailwind_build', help='Start Tailwind CSS build process')
    watch_parser.set_defaults(func=tailwind_build)

    # Map command
    map_parser = subparsers.add_parser('map', help='Generate a pythonic class based path map')
    map_parser.add_argument('folder_path', help='Path to the folder to map')
    map_parser.set_defaults(func=map_command)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()