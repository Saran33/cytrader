from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
import numpy as np

extensions = [
    Extension("mathsupport", sources=["mathsupport.pyx"],), # include_dirs=[np.get_include()]
    Extension("dataseries", sources=["dataseries.pyx"],),
]

setup(
    ext_modules = cythonize(extensions, annotate=True),
)
