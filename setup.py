import datetime
import os
import re
import setuptools
import sys

from setuptools import setup, find_packages

# Set external files
try:
    from pypandoc import convert
    README = convert('README.md', 'rst')	 
except ImportError:
    README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_version(*file_paths):
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('lambda_packages', '__init__.py')
# HISTORY = open('HISTORY.rst').read().replace('.. :changelog:', '')


def get_package():
    filename = os.path.join(
        os.path.dirname(__file__), 'dist',
        'xref_lambda_packages-{}.tar.gz'.format(VERSION)
    )
    return filename


if sys.argv[-1] == 'publish':
    print('Publishing the the package on gemfury:')
    os.system('fury push {} --as xref'.format(get_package()))
    sys.exit()

if sys.argv[-1] == 'tag':
    print('Tagging the version on github:')
    os.system('git tag -a {} -m "version {}"'.format(VERSION, VERSION))
    os.system('git push --tags')
    sys.exit()



setup(
    name='xref_lambda_packages',
    version=VERSION,
    packages=['lambda_packages'],
    include_package_data=True,
    license='MIT License',
    description='AWS Lambda Packages',
    long_description=README,
    url='https://github.com/xrefdev/lambda-packages',
    author='X',
    author_email='',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
