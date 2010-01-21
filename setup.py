from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='aaolm.portlet.facebook',
      version=version,
      description="Facebook Fan Page Portlet for Advanced Aquarist",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone facebook fan-page portlet',
      author='Shane Graber',
      author_email='sgraber@gmail.com',
      url='http://www.advancedaquarist.com/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['aaolm', 'aaolm.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
