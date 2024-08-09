import os
import subprocess
from pathlib import Path


def generate_local_tailwind_config(project_root, library_root):
    project_root = Path(project_root)
    library_root = Path(library_root)
    
    default_config_path = library_root / "default_tailwind_config.js"

    with default_config_path.open('r') as default_file:
        default_config = default_file.read()

    # Generate library paths
    library_paths = [
        os.path.relpath(str(library_root / "app.py"), start=str(project_root)),
        os.path.relpath(str(library_root / "fluidframe" / "core" / "components.py"), start=str(project_root)),
        os.path.relpath(str(library_root / "fluidframe" / "components" / "**" / "*.py"), start=str(project_root)),
        os.path.relpath(str(library_root / "fluidframe" / "templates" / "index.html"), start=str(project_root)),
    ]

    library_paths_str = ',\n    '.join(f'"{path}"' for path in library_paths)

    local_config = f"""const defaultConfig = {default_config}

defaultConfig.content = [
    {library_paths_str}
];

/** @type {{import('tailwindcss').Config}} */
module.exports = {{
  ...defaultConfig,
  content: [
    ...defaultConfig.content,
    // Add your custom content paths here
  ],
  theme: {{
    ...defaultConfig.theme,
    extend: {{
      // Add your custom theme extensions here
    }},
  }},
  plugins: [
    ...defaultConfig.plugins,
    // Add your custom plugins here
  ],
}}
"""

    local_config_path = project_root / "tailwind.config.js"
    with local_config_path.open('w') as local_file:
        local_file.write(local_config)

    print(f"Generated local tailwind.config.js at {local_config_path}")