from setuptools import setup, find_packages
import os

version = '0.3'

setup(name='collective.profiler',
      version=version,
      description="'Declare function for profiling in zcml and profileit'",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Intended Audience :: Developers",
        "Topic :: Utilities"
        ],
      keywords='',
      author='yboussard',
      author_email='yboussard@alterway.fr',
      url='https://github.com/collective/collective.profiler',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'profilehooks',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
