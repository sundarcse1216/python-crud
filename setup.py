#!/usr/bin/env python
# http://pymbook.readthedocs.io/en/latest/projectstructure.html

"""CRUD project"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='PythonCRUD',
      version='0.0.1',
      description="Python CRUD Operations",
      long_description=long_description,
      platforms=["linux"],
      author="sundar",
      author_email="sundarcse1216@gmail.com",
      # url="https://pymbook.readthedocs.io/en/latest/",
      # license = "MIT",
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',

          # Pick your license as you wish (should match "license" above)
          # 'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      # What does your project relate to?
      keywords='sample CRUD development',
      packages=find_packages(exclude=['tests', 'tests*']),
      install_requires=['python-interface', 'pymysql', 'configparser'],
      test_require=['pytest-cov', 'pytest'],
      tast_suite="tests",
      entry_points={'console_scripts': ['run = PythonCRUD.__main__']}
      )
