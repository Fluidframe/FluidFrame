import sys, os, platform
from Cython.Build import cythonize
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages, Extension
from fluidframe.utilities.package_manager import get_node_manager

sys.dont_write_bytecode = True

class CustomBuild(build_py):
    def run(self):
        node_manager = get_node_manager()
        if not node_manager.check_node_installed():
            node_manager.install_node()
        build_py.run(self)
        print("FluidFrame build complete, start a project by running `fluidframe init <project_name>`")

extensions = [
    Extension(
        "fluidframe.core.tags.tags", 
        ["fluidframe/core/tags/tags.pyx"],
        extra_link_args = ["-O3"] if platform.system() != "Windows" else [],
        extra_compile_args = ["-O3"] if platform.system() != "Windows" else [],
        py_limited_api = True
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
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Web Development :: Libraries :: Node Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Framework :: AsyncIO",
        "Environment :: Web Environment",
        "Natural Language :: English",
        "Typing :: Typed",
    ],
    entry_points={
        'console_scripts': [
            'fluidframe=fluidframe.cli:main',
        ],
    },
    cmdclass={
        'build_py': CustomBuild,
    },
    include_package_data=True,
    package_data={
        'fluidframe': [
            'core/tags/*.pyi',
            'node_modules/**/*',
        ],
    },
    python_requires='>=3.10',
    ext_modules=cythonize(extensions, language_level="3"),
)