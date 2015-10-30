#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
]

setup(
    name='ppprint',
    version='0.1.0',
    description='A prettier pretty-print',
    author='Carl Scheffler',
    author_email='carl.scheffler@gmail.com',
    url='https://github.com/cscheffler/ppprint',
    packages=[
        'ppprint',
    ],
    package_dir={'ppprint': 'ppprint'},
    install_requires=requirements,
    keywords='ppprint',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
)
