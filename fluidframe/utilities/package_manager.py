from typing import Dict, Any, List, Optional
import keyword, json, os, re, subprocess, platform, sys
from fluidframe.utilities.boilerplate import generate_app_boilerplate, generate_component_boilerplate
from fluidframe.config import PUBLIC_DIR, get_lib_path, FLUIDFRAME_PROJECT_DIR, FLUIDFRAME_PACKAGE_DIR
import posixpath 


def url_for_public(file_path: str) -> str:
    return f"{PUBLIC_DIR}/{file_path}"


PACKAGE_MAPPER = None
def generate_source_map(root_path: str = 'node_modules', output_json: Optional[str] = None, output_py: Optional[str] = None, include_file_types: List[str] = [".js", ".html", ".css", ".svg", ".webp", ".jpeg", ".jpg", ".png"], ignore_exists:bool=True):
    global PACKAGE_MAPPER
    if PACKAGE_MAPPER is None:
        PACKAGE_MAPPER = PackageMapper()
    PACKAGE_MAPPER.generate_source_map(root_path, output_json, output_py, include_file_types, ignore_exists)


NODE_MANAGER = None
def get_node_manager():
    global NODE_MANAGER
    if NODE_MANAGER is None:
        NODE_MANAGER = NodeManager(
            package_folder=FLUIDFRAME_PACKAGE_DIR, 
            project_folder=FLUIDFRAME_PROJECT_DIR,
        )
    return NODE_MANAGER


class PackageMapper:
    def _simplify_structure(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(data, dict):
            if len(data) == 1 and not isinstance(next(iter(data.values())), dict):
                return next(iter(data.values()))
            simplified = {k: self._simplify_structure(v) for k, v in data.items() if v}  # Skip empty values
            return {k: v for k, v in simplified.items() if v}  # Remove empty dictionaries
        return data
    
    def _replace_strings(self, text: str) -> str:
        text = re.sub(r'[^a-zA-Z0-9]', '_', text)
        if text[0].isdigit():
            text = f"n_{text}"
        text = re.sub(r'_+', '_', text)
        text = text.strip('_')
        if keyword.iskeyword(text):
            text = f"v_{text}"
        if not text or not text.isidentifier():
            text = f"{text}_"
        return text
    
    def _generate_class(self, name: str, data: Dict[str, Any], indent: str = "") -> str:
        class_lines = ["\n" + f"{indent}class _{name}:" + "\n"]
        for key, value in data.items():
            key = self._replace_strings(key)
            if isinstance(value, dict):
                if value:  # Only generate subclass if the dictionary is not empty
                    class_lines.extend([
                        self._generate_class(f"{name}_{key}", value, f"{indent}    "),
                        f"{indent}    {key} = _{name}_{key}()" + "\n"
                    ])
            else:
                class_lines.append(f'{indent}    {key}: str = "{value}"' + '\n')
            
        if len(class_lines) == 1:  # If no attributes were added, add a pass statement
            class_lines.append(f"{indent}    pass" + "\n")
            
        return ''.join(class_lines)
    
    def _analyze_and_simplify_directory(self, root_path: str, include_file_types: List[str]) -> Dict[str, Any]:
        raw_data = {}
        for root, _, files in os.walk(root_path):
            current = raw_data
            path_parts = os.path.relpath(root, root_path).split(os.sep)
                
            for part in path_parts:
                if part == '.':
                    continue
                current = current.setdefault(part, {})
                
            for file in files:
                if any(file.endswith(ext) for ext in include_file_types):
                    file_path = os.path.join(os.path.relpath(root, root_path), file)
                    file_path = file_path.replace('\\', '/')  # Ensure forward slashes for consistency
                    current[file] = file_path
        return self._simplify_structure(raw_data)
    
    def _generate_python_mapping(self, data: Dict[str, Any], output_py: str):
        bundle_map_lines = []
        main_class_lines = ["\n\nclass Bundle:\n"]
            
        for key, value in data.items():
            key = self._replace_strings(key)
            if isinstance(value, dict):
                class_name = key
                bundle_map_lines.append(self._generate_class(class_name, value))
                main_class_lines.append(f"    {class_name}=_{class_name}()" + "\n")
            else:
                main_class_lines.append(f'    {key}: str = "{value}"' + "\n")
            
        main_class_lines.append("\n\njs_bundle = Bundle()")

        bundle_map_content = ''.join(bundle_map_lines + main_class_lines)
        with open(output_py, "w") as f:
            f.write(bundle_map_content)
        print(f"Python mapping written to {output_py}")

    def generate_source_map(self, root_path: str = 'node_modules', output_json: Optional[str] = None, output_py: Optional[str] = None, include_file_types: List[str]|None = None, ignore_exists:bool=True):
        if include_file_types is None:
            include_file_types = [".js", ".html", ".css", ".svg", ".webp", ".jpeg", ".jpg", ".png"]
        json_data = self._analyze_and_simplify_directory(root_path, include_file_types)
            
        # Generate default output paths if not provided
        if output_json is None or output_py is None:
            base_name = os.path.basename(root_path)
            parent_dir = os.path.dirname(root_path)
                
            base_name = self._replace_strings(base_name)
        if output_json is None:
            output_json = os.path.join(parent_dir, f"{base_name}.json")
        if output_py is None:
            output_py = os.path.join(parent_dir, f"{base_name}.py")
            
        # Check if files already exist
        if not ignore_exists:
            if os.path.exists(output_json):
                raise FileExistsError(f"The file {output_json} already exists. Please provide a different name.")
            if os.path.exists(output_py):
                raise FileExistsError(f"The file {output_py} already exists. Please provide a different name.")
            
        self._generate_python_mapping(json_data, output_py)
   
 
class NodeManager:
    def __init__(self, package_folder: str, project_folder: str) -> None:
        self.working_dir = os.getcwd()
        self.project_folder_name = project_folder
        self.package_folder = os.path.join(self.working_dir, package_folder)
        self.project_folder = os.path.join(self.working_dir, project_folder)
    
    def check_node_installed(self) -> bool:
        try:
            subprocess.run(['node', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
        return True
    
    def install_node(self) -> None:
        system = platform.system().lower()
        if system == "windows":
            print("Please download and install Node.js from https://nodejs.org/")
        elif system == "darwin":
            print("To install Node.js on macOS, we recommend using Homebrew:")
            print("1. Install Homebrew: /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            print("2. Install Node.js: brew install node")
        elif system == "linux":
            print("To install Node.js on Linux, use your distribution's package manager.")
            print("For Ubuntu/Debian: sudo apt update && sudo apt install nodejs npm")
            print("For Fedora: sudo dnf install nodejs")
        else:
            print("Please install Node.js manually from https://nodejs.org/")
        sys.exit(1)
            
    def init_project(self, project_name: str) -> None:
        os.makedirs(self.package_folder, exist_ok=True)
        os.makedirs(self.project_folder, exist_ok=True)

        self.create_package_json(project_name)
        self.create_tailwind_config()
        self.create_rollup_config()
        self.tailwind_build()
        self.update()
        
        generate_source_map(root_path=self.package_folder)
        generate_app_boilerplate(self.project_folder)
        generate_component_boilerplate(self.project_folder)
        
        print(f"Project '{project_name}' initialized successfully.") 
 
    def create_package_json(self, package_name: str) -> None:
        package_json = get_lib_path("utilities/package.json")
        with open(package_json, 'r') as f:
            package_json = f.read()
        package_json = json.loads(package_json)
        package_json['name'] = package_name
        save_path = os.path.join(self.package_folder, 'package.json')
        with open(save_path, 'w') as f:
            json.dump(package_json, f, indent=2)
            
    def create_rollup_config(self) -> None:
        rollup_config = get_lib_path("utilities/rollup.config.js")
        with open(rollup_config, 'r') as f:
            rollup_config = f.read()
        save_path = os.path.join(self.package_folder, 'rollup.config.js')
        with open(save_path, 'w') as f:
            f.write(rollup_config)
            
    def create_tailwind_config(self) -> None:
        with open(os.path.join(self.package_folder, 'input.css'), 'w') as f:
            f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;\n")
        
        package_path = get_lib_path()
        library_files = [
            posixpath.join(package_path, "components", "**", "*.py"),
            posixpath.join(package_path, "public", "**", "*.js"),
            posixpath.join(package_path, "core", "**", "*.py"),
        ]
        
        # Convert Windows paths to POSIX format
        library_files = [path.replace(os.sep, '/') for path in library_files]

        config_content = f"""
module.exports = {{
  content: [
    // Library files
{os.linesep.join(f"    '{file}'," for file in library_files)}
    // User project files
    '../src/**/*.{{html,py}}'
  ],
  theme: {{
    extend: {{}},
  }},
  plugins: [],
}}
"""     
        tailwind_config_path = os.path.join(self.package_folder, 'tailwind.config.js')
        with open(tailwind_config_path, 'w') as f:
            f.write(config_content)
        
        generate_source_map(root_path=self.package_folder)
        
        print("Generated `tailwind.config.js` and `input.css` has been created")
    
    def install(self, package_name: str) -> None:
        if not self.check_node_installed():
            self.install_node()

        print(f"Installing Node.js package: {package_name}")
        npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
        try:
            subprocess.run([npm_command, 'install', package_name], cwd=self.package_folder, check=True)
            print(f"Successfully installed {package_name}")
            generate_source_map(root_path=self.package_folder)
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package_name}: {e}")
    
    def uninstall(self, package_name: str) -> None:
        if not self.check_node_installed():
            self.install_node()

        print(f"Uninstalling Node.js package: {package_name}")
        npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
        try:
            subprocess.run([npm_command, 'uninstall', package_name], cwd=self.package_folder, check=True)
            print(f"Successfully uninstalled {package_name}")
            generate_source_map(root_path=self.package_folder)
        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling {package_name}: {e}")
    
    def update(self) -> None:
        if not self.check_node_installed():
            self.install_node()

        print("Updating Node.js packages...")
        npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
        try:
            subprocess.run([npm_command, 'update'], cwd=self.package_folder, check=True)
            print("Packages updated successfully.")
            generate_source_map(root_path=self.package_folder)
        except subprocess.CalledProcessError as e:
            print(f"Error updating packages: {e}")
    
    def tailwind_build(self) -> None:
        try:
            npx_command = 'npx.cmd' if os.name == 'nt' else 'npx'
            subprocess.run([npx_command, 'tailwindcss', '-i', 'input.css', '-o', 'dist/output.css'], cwd=self.package_folder, check=True)
            generate_source_map(root_path=self.package_folder)
        except subprocess.CalledProcessError as e:
            print(f"Error on Tailwind build process: {e}")
        except KeyboardInterrupt:
            print("Tailwind build process has been stopped.")
            
    def bundle_package(self, input_dir: str, output_dir: str) -> None:
        abs_input_dir = os.path.abspath(os.path.join(self.working_dir, input_dir))
        abs_output_dir = os.path.abspath(os.path.join(self.working_dir, output_dir))
        
        print(f"Bundling files from {abs_input_dir} to {abs_output_dir}")
        
        npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
        try:
            subprocess.run(
                [npm_command, 'run', 'bundle', '--', f'--input={abs_input_dir}', f'--output={abs_output_dir}'], 
                cwd=self.package_folder,
                check=True
            )
            print(f"Successfully bundled files from {abs_input_dir} to {abs_output_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error on Bundling process: {e}")
        except KeyboardInterrupt:
            print("Rollup bundle process has been stopped.")
    
    def map_directory(self, folder_path: str) -> None:
        generate_source_map(root_path=folder_path)
    

