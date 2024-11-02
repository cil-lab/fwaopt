from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

cec17_extension = Extension(
    name="cec17",
    sources=["cec17.pyx"],
    libraries=["cec17"],
    library_dirs=["lib"],
    include_dirs=["lib"],
)
setup(name="cec17", ext_modules=cythonize([cec17_extension]),include_dirs=[numpy.get_include()], compiler_directives={'language_level' : "3"})
