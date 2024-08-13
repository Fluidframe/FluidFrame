import keyword, json, os, re
from typing import Dict, Any, List, Optional


class SourceMapGenerator:
    
    def __init__(self):
        pass

    def generate(self, root_path: str = 'node_modules', output_json: Optional[str] = None, output_py: Optional[str] = None, include_file_types: List[str] = ['.js', '.css']):
        json_data = self.analyze_and_simplify_directory(root_path, include_file_types)
        
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
        if os.path.exists(output_json):
            raise FileExistsError(f"The file {output_json} already exists. Please provide a different name.")
        if os.path.exists(output_py):
            raise FileExistsError(f"The file {output_py} already exists. Please provide a different name.")
        
        self.write_json(json_data, output_json)
        self.generate_python_mapping(json_data, output_py)
        
    def analyze_and_simplify_directory(self, root_path: str, include_file_types: List[str]) -> Dict[str, Any]:
        raw_data = self._analyze_directory(root_path, include_file_types)
        return self._simplify_structure(raw_data)

    def _analyze_directory(self, root_path: str, include_file_types: List[str]) -> Dict[str, Any]:
        result = {}
        for root, _, files in os.walk(root_path):
            current = result
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

        return result

    def _simplify_structure(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if isinstance(data, dict):
            if len(data) == 1 and not isinstance(next(iter(data.values())), dict):
                return next(iter(data.values()))
            simplified = {k: self._simplify_structure(v) for k, v in data.items() if v}  # Skip empty values
            return {k: v for k, v in simplified.items() if v}  # Remove empty dictionaries
        return data

    def write_json(self, data: Dict[str, Any], output_json: str):
        with open(output_json, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"JSON mapping written to {output_json}")

    def generate_python_mapping(self, data: Dict[str, Any], output_py: str):
        bundle_map_content = self._generate_bundle_map(data)
        with open(output_py, "w") as f:
            f.write(bundle_map_content)
        print(f"Python mapping written to {output_py}")

    def _generate_bundle_map(self, data: Dict[str, Any]) -> str:
        bundle_map_lines = []
        main_class_lines = ["\n\nclass Bundle:\n"]
        
        for key, value in data.items():
            key = self._replace_strings(key)
            if isinstance(value, dict):
                class_name = key
                bundle_map_lines.append(self._generate_class(class_name, value))
                main_class_lines.append(f"    {class_name}=_{class_name}()\n")
            else:
                main_class_lines.append(f'    {key}: str = "{value}"\n')
        
        main_class_lines.append("\n\njs_bundle = Bundle()")
        return ''.join(bundle_map_lines + main_class_lines)

    def _generate_class(self, name: str, data: Dict[str, Any], indent: str = "") -> str:
        class_lines = [f"\n{indent}class _{name}:\n"]
        for key, value in data.items():
            key = self._replace_strings(key)
            if isinstance(value, dict):
                if value:  # Only generate subclass if the dictionary is not empty
                    sub_class_name = f"{name}_{key}"
                    class_lines.append(self._generate_class(sub_class_name, value, indent + "    "))
                    class_lines.append(f"{indent}    {key} = _{sub_class_name}()\n")
            else:
                class_lines.append(f'{indent}    {key}: str = "{value}"\n')
        
        if len(class_lines) == 1:  # If no attributes were added, add a pass statement
            class_lines.append(f"{indent}    pass\n")
        
        return ''.join(class_lines)

    @staticmethod
    def _replace_strings(text: str) -> str:
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


if __name__ == "__main__":
    generator = SourceMapGenerator()

    # Use default paths
    # generator.generate()

    # # Or specify custom paths
    generator.generate(
        root_path='node_modules', 
        include_file_types=['.js', '.css']
    )