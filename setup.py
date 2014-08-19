#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.0.1'

setup(
    name='faced',
    version=VERSION,
    description='API for face detection',
    author='Michael Karpitsky',
    author_email='michael.karpitsky@gmail.com',
    license='BSD',
    url='https://github.com/karpitsky/faced',
    keywords=['Facedetection', 'Python'],
    packages=['faced'],
    requires=['opencv', 'numpy', 'flask']
)