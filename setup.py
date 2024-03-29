"""Briefy Choreographer Service."""
from setuptools import find_packages
from setuptools import setup

import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'HISTORY.rst')) as f:
    CHANGES = f.read()

requires = [
    'briefy.common',
    'boto3',
    'google-cloud-bigquery',
    'icalendar',
    'newrelic',
    'requests',
    'setuptools',
    'wheel',
    'zope.component',
    'zope.configuration',
    'zope.event',
    'zope.interface',
]

test_requirements = [
    'flake8',
    'pytest'
]

setup(
    name='briefy.choreographer',
    version='2.1.7',
    description='Briefy Choreographer composes actions based on events.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
    ],
    author='Briefy Tech Team',
    author_email='developers@briefy.co',
    url='https://github.com/BriefyHQ/briefy.choreographer',
    keywords='choreographer briefy',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['briefy', ],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements,
    install_requires=requires,
    entry_points="""
    [console_scripts]
    worker = briefy.choreographer.worker:main
    """,
)
