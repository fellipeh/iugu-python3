# -*- coding: utf-8 -*-
try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

import sys, os
from setuptools import find_packages
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
# from iugu.version import __version__

setup(
    name='iugu-python3',
    version='0.1',
    author='Fellipe Henrique',
    author_email='fellipeh@gmail.com',
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    scripts=[],
    url='https://github.com/fellipeh/iugu-python3',
    download_url='https://github.com/fellipeh/iugu-python3/tarball/master',
    license='Apache License',
    description='This package is an idiomatic python lib to work with Iugu service',
    long_description="""
  This iugu-python3 lib is the more pythonic way to work with webservices of payments
  iugu.com. This provides python objects to each entity of the service as Subscriptions,
  Plans, Customers, Invoices, etc.
  http://iugu.com/referencias/api - API Reference
""",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['iugu', 'rest', 'payment']
)
