#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name = "simpleimage",
    version = VERSION,
    author = '@emmmile',
    install_requires = [
        'opencv-python'
    ],
    license = 'MIT',
    test_suite = 'tests',
    python_requires = '>=3',
    packages = find_packages(exclude=["tests*"])
)
