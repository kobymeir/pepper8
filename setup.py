# -*- coding: utf-8

import os
import sys

from pepper8tc.main import VERSION

__version__ = VERSION

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
with open('README.rst') as r:
    readme = r.read()

# Dependencies
requires = [
    'Jinja2>=2.7',
]

setup(
    name='pepper8tc',
    version=__version__,
    description='Transforms pep8 or flake8 output into an HTML or TeamCity report output.',
    long_description=readme,
    author="Koby Meir (Initially code by Aleksander 'myth' Skraastad)",
    author_email='myth@overflow.no',
    packages=['pepper8tc'],
    license='MIT License',
    install_requires=requires,
    url='https://github.com/kobymeir/pepper8',
    package_data={
        'pepper8tc': ['templates/*_template.*']
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': ['pepper8tc = pepper8tc.main:main']
    }
)
