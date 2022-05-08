from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
import numpy as np

extensions = [
    Extension("bbroker", sources=["bbroker.pyx"], include_dirs=[np.get_include()])
]

setup(
    name="bbroker",
    ext_modules = cythonize(extensions, annotate=True),
)
