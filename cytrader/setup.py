from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
import numpy as np


extensions = [
    Extension("mathsupport", sources=["mathsupport.pyx"],), # include_dirs=[np.get_include()]
    Extension("writer", sources=["writer.pyx"],),

    Extension("brokers.bbroker", sources=["brokers/bbroker.pyx"], include_dirs=[np.get_include()]),

    Extension("utils.cythfuncs", sources=["utils/cythfuncs.pyx"],),
    Extension("utils.dateintern", sources=["utils/dateintern.pyx"],),
    Extension("utils.ordereddefaultdict", sources=["utils/ordereddefaultdict.pyx"],),
    Extension("utils.py3", sources=["utils/py3.pyx"],),
]

setup(
    ext_modules = cythonize(extensions, ), # annotate=True
)