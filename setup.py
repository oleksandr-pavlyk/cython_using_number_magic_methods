import setuptools
from setuptools import setup, Extension

setup(
    name="quaternion",
    ext_modules=[Extension(name="quaternion", sources=["quaternion.pyx"], language="c++")]
)
