#!/usr/bin/env python

from setuptools import setup

setup(
    name='CalculationService',
    description='Service for calculations.',
    version='1.0',
    author='Anton Iskov',
    author_email='aiskov@jiss-software.com',
    url='http://www.jiss-software.com',
    packages=[
        'handler'
    ],
    install_requires=[
        'tornado==4.2.1'
    ]
)
