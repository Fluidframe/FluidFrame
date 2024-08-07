from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "fluidframe.core.tags.tags", 
        ["fluidframe/core/tags/tags.pyx"],
        extra_compile_args=["-O3"], extra_link_args=["-O3"]
    )
]

setup(
    ext_modules=cythonize(extensions, language_level="3")
)