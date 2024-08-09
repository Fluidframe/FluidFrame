import argparse
from pathlib import Path
from fluidframe.utilities.node_utils import install_package, uninstall_package, update_package, init_project, run_npm_script

def main():
    parser = argparse.ArgumentParser(description='FluidFrame CLI')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize a new FluidFrame project')

    # Install command
    install_parser = subparsers.add_parser('install', help='Install a package')
    install_parser.add_argument('package', nargs='?', help='Package to install (optional)')

    # Uninstall command
    uninstall_parser = subparsers.add_parser('uninstall', help='Uninstall a package')
    uninstall_parser.add_argument('package', help='Package to uninstall')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a package')
    update_parser.add_argument('package', nargs='?', help='Package to update (optional)')

    # Run command
    run_parser = subparsers.add_parser('run', help='Run an npm script')
    run_parser.add_argument('script', help='Script to run')

    args = parser.parse_args()
    
    library_root = Path(__file__).parent.parent
    project_root = Path.cwd()

    if args.command == 'init':
        init_project(project_root, library_root)
    elif args.command == 'install':
        install_package(args.package, project_root)
    elif args.command == 'uninstall':
        uninstall_package(args.package, project_root)
    elif args.command == 'update':
        update_package(args.package, project_root)
    elif args.command == 'run':
        run_npm_script(args.script, project_root)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()