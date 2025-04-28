"""
This file instructs scitkit-build how to build the module. This is very close
to the classical setuptools, but wraps some things for us to build the native
modules easier and more reliable.

For a proper installation with `pip install .`, you additionally need a
`pyproject.toml` to specify the dependencies to load this `setup.py`.

You can use `python3 setup.py install` to build and install the package
locally, with verbose output. To build this package in place, which may be
useful for debugging, use `python3 setup.py develop`. This will build
the native modules and move them into your source folder.

The setup options are documented here:
https://scikit-build.readthedocs.io/en/latest/usage.html#setup-options
"""

from setuptools import find_packages
from skbuild_conan import setup
import sys

def readme():
    # Simply return the README.md as string
    with open("README.md") as file:
        return file.read()

setup(  # https://scikit-build.readthedocs.io/en/latest/usage.html#setup-options
    # ~~~~~~~~~ BASIC INFORMATION ~~~~~~~~~~~
    name="cgshop2023_pyutils",
    version="0.2.11",  # TODO: Use better approach for managing version number.
    description="Official utilities for the CG:SHOP Challenge 2023.",
    long_description=readme(),
    url="https://github.com/CG-SHOP/pyutils23",
    long_description_content_type="text/markdown",
    author="TU Braunschweig, IBR, Algorithms Group (Phillip Keldenich and Dominik Krupke)",
    author_email="keldenich@ibr.cs.tu-bs.de, krupke@ibr.cs.tu-bs.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    # ~~~~~~~~~~~~ CRITICAL PYTHON SETUP ~~~~~~~~~~~~~~~~~~~
    # This project structures defines the python packages in a subfolder.
    # Thus, we have to collect this subfolder and define it as root.
    packages=find_packages("python"),  # Include all packages in `./python`.
    package_dir={"": "python"},  # The root for our python package is in `./python`.
    python_requires=">=3.7",  # lowest python version supported.
    install_requires=[
        # requirements necessary for basic usage (subset of requirements.txt)
        "chardet>=4.0.0",
        "networkx>=2.5.1",
        "requests>=2.25.1",
    ],
    conan_requirements=["fmt/[>=10.0.0]", "cgal/[>=6.0]"],  # C++ Dependencies
    conan_profile_settings={"compiler.cppstd": 17},
    cmake_minimum_required_version="3.17",
)
