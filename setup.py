#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from setuptools import setup, find_packages

full_version = ''

root_dir = os.path.abspath(os.path.dirname(__file__))

readme_file = os.path.join(root_dir, 'README.rst')
with open(readme_file, encoding='utf-8') as f:
	long_description = f.read()

version_module = os.path.join(root_dir, 'src', 'timedriver', 'version.py')
with open(version_module, encoding='utf-8') as f:
	exec(f.read())


setup(
	name='timedriver',
	version=full_version,
	description='A Python TiMe messenger driver',
	long_description=long_description,
	url='https://github.com/nyorf/python-time-driver',
	author='Dmitry Dolgov',
	author_email='me@nyorf.com',
	license='MIT',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: 3.12',
		'Programming Language :: Python :: 3.13',
	],
	package_dir={'': 'src'},
	packages=find_packages('src'),
	python_requires=">=3.9",
	install_requires=[
		'websockets>=14.0',
		'requests>=2.32.0'
	],
)
