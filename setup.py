#!/usr/bin/env python

from setuptools import setup, find_packages

# with open('README.md', encoding='utf-8') as f:
#       long_description = f.read().strip()
long_description = "A simple offline pincode validator for India"

setup(name="pincode",
      version="1.0.3",
      description=long_description,
      long_description=long_description,
      long_description_content_type='text/markdown',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
    )
