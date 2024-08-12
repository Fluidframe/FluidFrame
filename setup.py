import sys
import subprocess
from pathlib import Path
from Cython.Build import cythonize
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages, Extension

sys.dont_write_bytecode = True

class CustomBuild(build_py):
    def run(self):
        project_root = Path.cwd()
        library_root = Path(__file__).parent
        self.build_tailwind(project_root, library_root)
        
        build_py.run(self)

    def build_tailwind(self, project_root, library_root):
        from fluidframe.utilities.tailwind_utils import generate_local_tailwind_config
        from fluidframe.utilities.node_utils import check_node_installed, install_node

        if not check_node_installed():
            install_node()
        generate_local_tailwind_config(project_root, library_root)
        
        config_path = project_root / "tailwind.config.js"
        input_path = library_root / "fluidframe" / "static" / "input.css"
        output_path = library_root / "fluidframe" / "static" / "dist" / "output.css"
        subprocess.run(f"npx tailwindcss -c {config_path} -i {input_path} -o {output_path}", shell=True, check=True)

extensions = [
    Extension(
        "fluidframe.core.tags.tags", 
        ["fluidframe/core/tags/tags.pyx"],
        extra_compile_args=["-O3"], 
        extra_link_args=["-O3"],
        py_limited_api=True
    )
]

setup(
    name='fluidframe',
    version='0.0.1',
    author='Aswanth C Manoj',
    author_email='aswanthmanoj51@gmail.com',
    description="FluidFrame is a powerful, pythonic web application framework that embraces the simplicity and capability of hypermedia concepts. It combines Python's elegance with HTMX's innovative approach to create dynamic, interactive web applications without the need for complex JavaScript.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/AswanthManoj/fluidframe',
    packages=find_packages(include=["fluidframe", "fluidframe.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'build_py': CustomBuild,
    },
    include_package_data=True,
    package_data={
        'fluidframe': [
            'core/tags/*.pyi',
            'static/dist/output.css',
            '../node_modules/**/*',
        ],
    },
    python_requires='>=3.10',
    ext_modules=cythonize(extensions, language_level="3"),
)