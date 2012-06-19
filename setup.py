#!/usr/bin/env python

try:
	from setuptools import setup, find_packages
except ImportError:
	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup, find_packages

setup(
    name='django-webtemplates',
    version="0.1.0",
    description='Load templates from an external web site.',
    author='Tim Heap',
    author_email='tim@ionata.com.au',
    url='https://bitbucket.org/ionata/django-webtemplates',
    packages=['webtemplates', 'django_pronouns.fixtures'],
    install_requires = ['requests'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
