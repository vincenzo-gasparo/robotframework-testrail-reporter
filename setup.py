#!/usr/bin/env python

from os.path import abspath, dirname, join

try:
    from setuptools import setup, find_packages
except ImportError as error:
    from distutils.core import setup

VERSION = ""
with open("README.md", "r") as f:
    DESCRIPTION = f.read()

CLASSIFIERS = """
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(
    name='robotframework-testrail-reporter',
    version="0.0.16",
    description='robotframework-testrail-reporter',
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author='Vincenzo Gasparo',
    author_email='vincenzo.gasparo@gmail.it',
    maintainer='Vincenzo Gasparo',
    maintainer_email='vincenzo.gasparo@gmail.it',
    url='https://github.com/vincenzo-gasparo/robotframework-testrail-reporter',
    license='MIT',
    keywords='robotframework testrail test  testing automation',
    platforms='any',
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'lxml',
        'testrail'
    ],
    entry_points={'console_scripts': ['rf-tr-reporter=RobotTestrailReporter.RobotTestrailReporter:main']}
)

""" Official release from master
# make sure the setup version has been increased
"""
