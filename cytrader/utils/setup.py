from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
import numpy as np

extensions = [
    Extension("dateintern", sources=["dateintern.pyx"],),
    Extension("ordereddefaultdict", sources=["ordereddefaultdict.pyx"],),
    Extension("py3", sources=["py3.pyx"],),
]

setup(
    ext_modules = cythonize(extensions, annotate=True),
)
