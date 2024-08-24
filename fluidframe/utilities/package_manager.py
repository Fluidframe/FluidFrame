import keyword, json, os, re
from typing import Dict, Any, List, Optional
from fluidframe.config import MODULES_DIR, PUBLIC_DIR


def generate_source_map(root_path: str = 'node_modules', output_json: Optional[str] = None, output_py: Optional[str] = None, include_file_types: List[str] = [".js", ".html", ".css", ".svg", ".webp", ".jpeg", ".jpg", ".png"], ignore_exists:bool=True):
    """
    Generates a source map for a directory.

    Args:
        root_path: The directory path to generate the source map for.
        output_json: The path to write the JSON source map to.
        output_py: The path to write the Python source map to.
        include_file_types: A list of file types to include in the source map.
        ignore_exists: A bool flag to ignore existing files and rewrite it.

    Raises:
        FileExistsError: If either the JSON or Python source map file already exists.
    """
    json_data = analyze_and_simplify_directory(root_path, include_file_types)
        
    # Generate default output paths if not provided
    if output_json is None or output_py is None:
        base_name = os.path.basename(root_path)
        parent_dir = os.path.dirname(root_path)
            
        base_name = replace_strings(base_name)
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
        
    # write_json(json_data, output_json)
    generate_python_mapping(json_data, output_py)
        
def analyze_and_simplify_directory(root_path: str, include_file_types: List[str]) -> Dict[str, Any]:
    """
    Analyzes and simplifies a directory structure.

    Args:
        root_path (str): The path to the root directory.
        include_file_types (List[str]): A list of file types to include in the analysis.

    Returns:
        Dict[str, Any]: A simplified dictionary representation of the directory structure.
    """
    raw_data = analyze_directory(root_path, include_file_types)
    return simplify_structure(raw_data)

def analyze_directory(root_path: str, include_file_types: List[str]) -> Dict[str, Any]:
    """
    Analyzes and simplifies a directory structure by walking through the directory and its subdirectories,
    and creating a dictionary representation of the directory structure with file paths.

    Args:
        root_path (str): The path to the root directory.
        include_file_types (List[str]): A list of file types to include in the analysis.

    Returns:
        Dict[str, Any]: A simplified dictionary representation of the directory structure, where the keys are the
        directory paths and the values are dictionaries of file names and their corresponding paths.

    Example:
        >>> analyze_directory('/path/to/directory', ['.txt', '.csv'])
        {
            'path': {
                'to': {
                    'directory': {
                        'file1.txt': '/path/to/directory/file1.txt',
                        'file2.txt': '/path/to/directory/file2.txt',
                        'subdir': {
                            'file3.txt': '/path/to/directory/subdir/file3.txt',
                            'file4.csv': '/path/to/directory/subdir/file4.csv'
                        }
                    }
                }
            }
        }
    """
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

def simplify_structure(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively simplifies a nested dictionary structure by removing empty dictionaries and collapsing single-item dictionaries.

    Args:
        data (Dict[str, Any]): The dictionary to simplify.

    Returns:
        Dict[str, Any]: The simplified dictionary structure.
    """
    if isinstance(data, dict):
        if len(data) == 1 and not isinstance(next(iter(data.values())), dict):
            return next(iter(data.values()))
        simplified = {k: simplify_structure(v) for k, v in data.items() if v}  # Skip empty values
        return {k: v for k, v in simplified.items() if v}  # Remove empty dictionaries
    return data

def write_json(data: Dict[str, Any], output_json: str):
    """
    Writes the given data to a JSON file at the specified output path.

    Args:
        data (Dict[str, Any]): The data to write to the JSON file.
        output_json (str): The path to the output JSON file.

    Returns:
        None

    Prints:
        A message indicating the path where the JSON mapping was written.
    """
    with open(output_json, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"JSON mapping written to {output_json}")

def generate_python_mapping(data: Dict[str, Any], output_py: str):
    """
    Generates a Python mapping file based on the provided data and writes it to the specified output path.

    Args:
        data (Dict[str, Any]): The data to be used for generating the Python mapping.
        output_py (str): The path where the Python mapping file will be written.

    Returns:
        None

    Prints:
        A message indicating the path where the Python mapping was written.
    """
    bundle_map_content = generate_bundle_map(data)
    with open(output_py, "w") as f:
        f.write(bundle_map_content)
    print(f"Python mapping written to {output_py}")

def generate_bundle_map(data: Dict[str, Any]) -> str:
    """
    Generates a bundle map string based on the provided data.

    Args:
        data (Dict[str, Any]): A dictionary containing the data to be used for generating the bundle map.

    Returns:
        str: A string representing the bundle map.
    """
    bundle_map_lines = []
    main_class_lines = ["\n\nclass Bundle:\n"]
        
    for key, value in data.items():
        key = replace_strings(key)
        if isinstance(value, dict):
            class_name = key
            bundle_map_lines.append(generate_class(class_name, value))
            main_class_lines.append(f"    {class_name}=_{class_name}()\n")
        else:
            main_class_lines.append(f'    {key}: str = "{value}"\n')
        
    main_class_lines.append("\n\njs_bundle = Bundle()")
    return ''.join(bundle_map_lines + main_class_lines)

def generate_class(name: str, data: Dict[str, Any], indent: str = "") -> str:
    """
    Generates a string representing a Python class based on the provided data.

    Args:
        name (str): The name of the class to be generated.
        data (Dict[str, Any]): A dictionary containing the data to be used for generating the class.
        indent (str): The indentation string to be used for the class definition. Defaults to an empty string.

    Returns:
        str: A string representing the generated class.
    """
    class_lines = [f"\n{indent}class _{name}:\n"]
    for key, value in data.items():
        key = replace_strings(key)
        if isinstance(value, dict):
            if value:  # Only generate subclass if the dictionary is not empty
                sub_class_name = f"{name}_{key}"
                class_lines.append(generate_class(sub_class_name, value, indent + "    "))
                class_lines.append(f"{indent}    {key} = _{sub_class_name}()\n")
        else:
            class_lines.append(f'{indent}    {key}: str = "{value}"\n')
        
    if len(class_lines) == 1:  # If no attributes were added, add a pass statement
        class_lines.append(f"{indent}    pass\n")
        
    return ''.join(class_lines)

def replace_strings(text: str) -> str:
    """
    Replaces all non-alphanumeric characters in the given text with underscores, and prepends a 'n_' prefix to the text if it starts with a digit.
    Removes multiple consecutive underscores and trims leading and trailing underscores.
    If the resulting text is a Python keyword, it is prefixed with 'v_'.
    If the resulting text is not a valid Python identifier, it is appended with an underscore.
    
    :param text: The input text to be processed.
    :type text: str
    :return: The processed text with all non-alphanumeric characters replaced with underscores, and optional prefixes and suffixes added.
    :rtype: str
    """
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

def url_for_module(file_path:str) -> str:
    return f"{MODULES_DIR}/{file_path}"

def url_for_public(file_path: str) -> str:
    return f"{PUBLIC_DIR}/{file_path}"

# if __name__ == "__main__":
#     # # Or specify custom paths
#     generate_source_map(
#         root_path='node_modules', 
#         include_file_types=['.js', '.css']
#     )