from setuptools import setup, find_packages
import os

version = '1.0.3'

long_description = open('README.md').read()

setup(name='cco.schema',
      version=version,
      description="schema and form configuration",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='cyberconcepts.org team',
      author_email='team@cyberconcepts.org',
      url='http://www.cyberconcepts.org',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['cco'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'loops',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
