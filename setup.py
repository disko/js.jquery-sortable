# -*- coding: utf-8 -*-

"""
Created on 2014-05-12
:author: Andreas Kaiser (disko)
"""

import os
from setuptools import find_packages
from setuptools import setup

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '.postX' suffix with an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4.post1 .

version = '0.9.14.dev0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_sortable', 'test_jquery_sortable.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_sortable',
    version=version,
    description='Fanstatic packaging of jQuery Sortable',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
    ],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/fanstatic/js.jquery-sortable',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_sortable = js.jquery_sortable:library',
        ],
    },
    extras_require={
        'testing': ['setuptools-git', 'pytest', 'tox', ],
    },
)
