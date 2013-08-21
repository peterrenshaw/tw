#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import os
from setuptools import setup
from setuptools import find_packages
from distutils.core import setup

name = 'tw'
version = '0.2.1'
setup( name=name,
       version=version,
       py_modules=[name,'tw'], 
       author='Peter Renshaw',
       author_email='goonmail@netspace.net.au',
       url='http://seldomlogical/%s/'%name,
       description='twitter writing application',
       license='GNU GPL 3.0',
       keywords=['dynamic','twitter','client'],
       platforms=[],
       packages = find_packages(), 
       classifiers=['Development Status :: 0 - Experimental',
                    'Intended Audience :: others',
                    'License :: OSI Approved :: GNU General Public License (GPL)',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python'                    
                    ]
       )

# vim: noet:noai:ts=4:sw=4:tw=78
