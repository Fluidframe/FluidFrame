import sys
import subprocess
from pathlib import Path
from Cython.Build import cythonize
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages, Extension

library_root = Path(__file__).parent

class CustomBuild(build_py):
    def run(self):
        subprocess.check_call([sys.executable, str(Path('build.py'))])
        build_py.run(self)

extensions = [
    Extension(
        "fluidframe.core.tags.tags", 
        [str(library_root / "fluidframe" / "core" / "tags" / "tags.pyx")],
        extra_compile_args=["-O3"], extra_link_args=["-O3"]
    )
]

setup(
    name='fluidframe',
    version='0.1.0',
    packages=find_packages(
        include=[
            "fluidframe", 
            "fluidframe.*"
        ]
    ),
    cmdclass={
        'build_py': CustomBuild,
    },
    include_package_data=True,
    package_data={
        'fluidframe': [
            'core/tags/*.pyi',
            '../node_modules/**/*',
        ],
    },
    ext_modules=cythonize(extensions, language_level="3"),
)