import sys
from setuptools import setup, find_packages, Extension
from setuptools.command.build_py import build_py
import subprocess
from Cython.Build import cythonize

class CustomBuild(build_py):
    def run(self):
        subprocess.check_call([sys.executable, 'build.py'])
        build_py.run(self)

extensions = [
    Extension(
        "fluidframe.core.tags.tags", 
        ["fluidframe/core/tags/tags.pyx"],
        extra_compile_args=["-O3"], extra_link_args=["-O3"]
    )
]

setup(
    name='fluidframe',
    version='0.1.0',
    packages=find_packages(),
    cmdclass={
        'build_py': CustomBuild,
    },
    include_package_data=True,
    package_data={
        'fluidframe': ['static/css/*'],
    },
    ext_modules=cythonize(extensions, language_level="3"),
)