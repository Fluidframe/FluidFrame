from typing import List, Optional

SCRIPTS = {
    "tooltip": 
        {
            "style": "fluidframe/utils/tooltip/style.css",
            "script": "fluidframe/utils/tooltip/script.js"
        }
}

'''class InteractiveScript:
    
    def __init__(self) -> None:
        self.all_scripts: dict = {}
        self.dependencies: dict = {}
        
    def add_script(self, name: str, script_path: str):
        if name in self.all_scripts:
            raise ("The given script name already exists as part of pre-built scripts, you may have to rename it in order to add it.")
        with open(script_path, 'r') as file:
            js_script = file.read()
        self.all_scripts[name] = js_script

    def add_tooltip(self, id: str, message: str) -> str:
        if "tooltip" not in self.dependencies:
            self.dependencies["tooltip"]
        return f"<script>addTooltip(document.getElementById('{id}'), '{message}');</script>"
'''

from typing import Dict, List, Optional
import os

class ScriptManager:
    def __init__(self):
        self.scripts: Dict[str, Dict[str, str]] = {}
        self.used_scripts: Dict[str, bool] = {}
        self.custom_scripts: Dict[str, str] = {}
        self.custom_styles: Dict[str, str] = {}

    def register_script(self, name: str, script_path: str, style_path: Optional[str] = None):
        """Register a new script (and optionally its style)."""
        if name in self.scripts:
            raise ValueError(f"Script '{name}' is already registered.")
        
        script_content = self._read_file(script_path)
        style_content = self._read_file(style_path) if style_path else None
        
        self.scripts[name] = {
            "script": script_content,
            "style": style_content
        }
        self.used_scripts[name] = False

    def use_script(self, name: str):
        """Mark a script as used."""
        if name not in self.scripts:
            raise ValueError(f"Script '{name}' is not registered.")
        self.used_scripts[name] = True

    def add_custom_script(self, name: str, content: str):
        """Add a custom script."""
        self.custom_scripts[name] = content

    def add_custom_style(self, name: str, content: str):
        """Add a custom style."""
        self.custom_styles[name] = content

    def get_used_scripts(self) -> str:
        """Get all used scripts and their styles."""
        output = ""
        for name, used in self.used_scripts.items():
            if used:
                script_data = self.scripts[name]
                if script_data["style"]:
                    output += f"<style>{script_data['style']}</style>\n"
                output += f"<script>{script_data['script']}</script>\n"
        
        for style in self.custom_styles.values():
            output += f"<style>{style}</style>\n"
        
        for script in self.custom_scripts.values():
            output += f"<script>{script}</script>\n"
        
        return output

    @staticmethod
    def _read_file(path: str) -> str:
        """Read file content."""
        with open(path, 'r') as file:
            return file.read()

class Component:
    def __init__(self, script_manager: ScriptManager):
        self.script_manager = script_manager

    def use_tooltip(self, element_id: str, message: str) -> str:
        self.script_manager.use_script("tooltip")
        return f'<div id="{element_id}" data-tooltip="{message}"></div>'

    # Add more component methods as needed

# Usage example:
script_manager = ScriptManager()

# Register built-in scripts
script_manager.register_script("tooltip", "path/to/tooltip.js", "path/to/tooltip.css")

# Create a component
component = Component(script_manager)

# Use the component in your HTML
html_content = component.use_tooltip("my-element", "This is a tooltip")

# At the end of your HTML rendering, include used scripts
scripts_and_styles = script_manager.get_used_scripts()

# Add custom script or style if needed
script_manager.add_custom_script("custom-script", "console.log('Custom script');")
script_manager.add_custom_style("custom-style", ".custom-class { color: red; }")

# Final HTML output
final_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
    {scripts_and_styles}
</head>
<body>
    {html_content}
</body>
</html>
"""
    