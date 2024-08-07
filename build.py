import os
import subprocess
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize

def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()

def setup_node_environment():
    run_command("poetry run nodeenv -p")
    run_command("npm install")

def build_tailwind():
    run_command("npx tailwindcss -i ./fluidframe/static/css/input.css -o ./fluidframe/static/css/dist/output.css")

def build_cython():
    extensions = [
        Extension(
            "fluidframe.core.tags.tags", 
            ["fluidframe/core/tags/tags.pyx"],
            extra_compile_args=["-O3"], extra_link_args=["-O3"]
        )
    ]
    return cythonize(extensions, language_level="3")

if __name__ == "__main__":
    setup_node_environment()
    build_tailwind()
    build_cython()
