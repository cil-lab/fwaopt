from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

cec20_extension = Extension(
    name="cec20",
    sources=["cec20.pyx"],
    libraries=["cec20"],
    library_dirs=["lib"],
    include_dirs=["lib"],
)
setup(name="cec20", ext_modules=cythonize([cec20_extension]),include_dirs=[numpy.get_include()], compiler_directives={'language_level' : "3"})
