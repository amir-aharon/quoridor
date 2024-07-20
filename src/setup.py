from setuptools import find_packages
from distutils.core import setup

setup(
    name="quoridor",
    packages=find_packages("."),
    version="1.0.0",
    install_requires=["pygame"],
)
