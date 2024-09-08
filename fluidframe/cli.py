import argparse
from fluidframe.utilities.package_manager import generate_source_map, get_node_manager


node_manager = get_node_manager()


def main():
    parser = argparse.ArgumentParser(description='FluidFrame CLI')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Init project command
    init_parser = subparsers.add_parser('init', help='Initialize a new project')
    init_parser.add_argument('project_name', type=str, help='The name of the project')

    # Install package command
    install_parser = subparsers.add_parser('install', help='Install a Node.js package')
    install_parser.add_argument('package_name', type=str, help='The name of the package to install')

    # Uninstall package command
    uninstall_parser = subparsers.add_parser('uninstall', help='Uninstall a Node.js package')
    uninstall_parser.add_argument('package_name', type=str, help='The name of the package to uninstall')

    # Update packages command (optional if you want a package update feature)
    update_parser = subparsers.add_parser('update', help='Update Node.js packages')

    # Tailwind build command
    tailwind_parser = subparsers.add_parser('build-css', help='Build Tailwind CSS')
    
    # Bundle command
    bundle_parser = subparsers.add_parser('bundle', help='Bundle JavaScript using Rollup')
    bundle_parser.add_argument('--input', type=str, default='src', help='Input directory for bundling (default: src)')
    bundle_parser.add_argument('--output', type=str, default='fluidbuild/dist', help='Output directory for bundling (default: fluidbuild/dist)')

    # Map directory command
    map_parser = subparsers.add_parser('map', help='Generate source map for a directory')
    map_parser.add_argument('folder_path', type=str, help='The folder path to map')

    args = parser.parse_args()
    
    if args.command == 'init':
        # Initialize project
        node_manager.init_project(args.project_name)

    elif args.command == 'install':
        # Install package
        node_manager.install(args.package_name)

    elif args.command == 'uninstall':
        # Uninstall package
        node_manager.uninstall(args.package_name)

    elif args.command == 'update':
        # Update packages
        node_manager.update()  # Here, you can define logic to update packages if needed.

    elif args.command == 'build-css':
        # Tailwind build
        node_manager.tailwind_build()

    elif args.command == 'bundle':
        # Bundle JavaScript files
        node_manager.bundle_package(args.input, args.output)

    elif args.command == 'map':
        # Generate source map
        node_manager.map_directory(args.folder_path)
    

if __name__ == '__main__':
    main()