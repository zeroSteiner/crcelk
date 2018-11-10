#!/usr/bin/python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 noexpandtab
#
# Copyright (C) 2005, 2007  Ray Burr
# Copyright (C) 2016        Spencer McIntyre
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

#  Original (Moose) Homepage: http://www.nightmare.com/~ryb/
#  New (Elk) Homepage: https://github.com/zeroSteiner/crcelk/

import os
import sys

from crcelk import __version__

base_directory = os.path.dirname(__file__)

try:
	from setuptools import setup, find_packages
except ImportError:
	print('This project needs setuptools in order to build. Install it using your package')
	print('manager (usually python-setuptools) or via pip (pip install setuptools).')
	sys.exit(1)

with open(os.path.join(base_directory, 'README.rst'), 'r') as file_h:
	long_description = file_h.read()

DESCRIPTION = """\
CrcElk is an updated fork of the CrcMoose module for recent versions of \
Python. It provides a pure Python implementation of the CRC algorithm and \
allows for variants to easily be defined by providing their parameters such as \
width, starting polynomial, etc. Python versions 2.6+ and 3.1+ are supported.\
"""

setup(
    name='crcelk',
    version=__version__,
    author='Ray Burr',
    maintainer='Spencer McIntyre',
    maintainer_email='zeroSteiner@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    url='https://github.com/zeroSteiner/crcelk',
    license='MIT',
    py_modules=['crcelk'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
