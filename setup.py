#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

def load_requirements(fname):
    #TODO: use pkg_resources to grab the file (in case we're inside an archive)
    with open(fname, 'r') as reqfile:
        reqs = reqfile.read()

    return filter(None, reqs.strip().splitlines())

REQUIREMENTS = load_requirements('requirements.txt')

setup(
    name='flaskapi',
    version='0.1',
    package_dir = {'': 'src'},
    packages = find_packages('src'),

    install_requires=REQUIREMENTS,
    entry_points = {
        'console_scripts': [
            'flaskapi = flaskapi.main:main',
            ]
    },
)
