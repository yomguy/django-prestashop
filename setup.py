#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

setup(
    name='django-prestashop',
    url='https://forge.ircam.fr/p/django-prestashop/',
    description="Django module accessing PrestaShop databases",
    long_description=open('README.rst').read(),
    author="Guillaume Pellerin",
    author_email="guillaume.pellerin@ircam.fr",
    version='1.0',
    install_requires=['django',],
    platforms=['OS Independent'],
    license='Lesser GNU Public License v3',
    packages=['eve'],
    include_package_data=True,
    zip_safe=False,
    )
