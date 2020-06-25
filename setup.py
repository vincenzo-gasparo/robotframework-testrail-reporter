#!/usr/bin/env python

from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError as error:
    from distutils.core import setup

VERSION = ""
DESCRIPTION = """
Library used to update TestRail test run status from RobotFramework output.xml
"""[1:-1]

CLASSIFIERS = """
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

version_file = join(dirname(abspath(__file__)), 'src', 'TestRailRobotReporter', 'version.py')

with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)

setup(
    name='robotframework-testrail-reporter',
    version=VERSION,
    description='robotframework-testrail-reporter',
    long_description=DESCRIPTION,
    author='Vincenzo Gasparo',
    author_email='vincenzo.gasparo@gmail.it',
    maintainer='Vincenzo Gasparo',
    maintainer_email='vincenzo.gasparo@gmail.it',
    url='',
    license='MIT',
    keywords='robotframework testrail test  testinga utomation',
    platforms='any',
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    packages=['TestRailRobotReporter'],
    install_requires=[
        'lxml',
        'testrail'
    ],
    entry_points={'console_scripts':
                      ['rf-tr-reporter = RobotTestrailReporter.RobotTestrailReporter:run_cli']}
      )

""" Official release from master
# make sure the setup version has been increased
"""
