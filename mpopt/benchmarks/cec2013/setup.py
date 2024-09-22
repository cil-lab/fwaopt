from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

cec13_extension = Extension(
    name="cec13",
    sources=["cec13.pyx"],
    libraries=["cec13"],
    library_dirs=["lib"],
    include_dirs=["lib"],
)
setup(name="cec13", ext_modules=cythonize([cec13_extension]),include_dirs=[numpy.get_include()], compiler_directives={'language_level' : "3"})
