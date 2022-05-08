from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
import numpy as np

extensions = [
    Extension("strategy", sources=["strategy.pyx"], include_dirs=[np.get_include()])
]

setup(
    name="strategy",
    ext_modules = cythonize(extensions, annotate=True),
)
