#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

rel_file = lambda *args: os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)

def read_from(filename):
    fp = open(filename)
    try:
        return fp.read()
    finally:
        fp.close()

def get_version():
    data = read_from(rel_file('src', 'exceptional', '__init__.py'))
    return re.search(r"__version__ = '([^']+)'", data).group(1)

setup(
    name             = 'pylons-exceptional',
    version          = get_version(),
    author           = "Alexis Le-Quoc",
    author_email     = "alq@datadoghq.com",
    url              = 'http://github.com/DataDog/pylons-exceptional',
    description      = "A pylons client for Exceptional (getexceptional.com), ported from django-exceptional",
    packages         = ['exceptional'],
    package_dir      = {'': 'src'},
    install_requires=[
        "Pylons>=1.0",
        ],
)
