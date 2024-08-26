import os, platform
from setuptools import Extension
from Cython.Build import cythonize

def build(setup_kwargs):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to your .pyx file
    pyx_path = os.path.join(current_dir, 'fluidframe_test', 'core', 'tags', 'tags.pyx')
    
    # Define the extension
    extensions = [
        Extension(
            "fluidframe_test.core.tags.tags",
            [pyx_path],
            extra_link_args = ["-O3"] if platform.system() != "Windows" else [],
            extra_compile_args = ["-O3"] if platform.system() != "Windows" else [],
            py_limited_api=True
        )
    ]
    
    # Cythonize the extension
    ext_modules = cythonize(extensions, language_level="3")
    
    # Update setup_kwargs with ext_modules
    setup_kwargs.update({
        'ext_modules': ext_modules,
    })

    print("Cython extensions built successfully.")

if __name__ == '__main__':
    build(setup_kwargs={})