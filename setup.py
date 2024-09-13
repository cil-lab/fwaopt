# import setuptools
from setuptools import setup, find_packages

setup(
    name="mpopt",
    version="1.1.0",
    author="CIL-LAB",
    description="Fireworks Algorithm",
    package=['mpopt'],
    package_dir={
          'mpopt': 'mpopt',
      }
    # py_modules=[],
)
