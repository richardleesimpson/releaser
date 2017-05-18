# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='releaser',
    version='0.0.1',
    description='Build a release directory... hopefully',
    long_description=readme,
    author='Richard Simpson',
    author_email='richard@8thdaysoftware.com',
    url='https://github.com/richard8thday/releaser',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)