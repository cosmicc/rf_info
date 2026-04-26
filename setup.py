#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages
from glob import glob
import os


def find_dirs(dir_name):
    for dir, dirs, files in os.walk('.'):
        if dir_name in dirs:
            yield os.path.relpath(os.path.join(dir, dir_name))


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['iso3166>=2.1.1', 'colorama>=0.4.6']

data_files = []
man_sections = {}
for dir in find_dirs('man'):
    for file in os.listdir(dir):
        section = file.split('.')[-1]
        man_sections[section] = man_sections.get(section, []) + [os.path.join(dir, file)]
for section in man_sections:
    data_files.append(('share/man/man'+section, man_sections[section]))
info_pages = {}
for dir in find_dirs('info'):
    for file in glob(os.path.join(dir, '*.info')):
        info_pages[dir] = info_pages.get(dir, []) + [file]
for dir in info_pages:
    data_files.append(('share/info', info_pages[dir]))

setup(
    author="Ian Perry",
    author_email='ianperry99@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    description="Python library and command line tool to get Information about a Radio Frequency",
    entry_points={
        'console_scripts': [
            'rf-info=rf_info.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='rf_info',
    name='rf_info',
    packages=find_packages(include=['rf_info', 'rf_info.*']),
    data_files=data_files,
    url='https://github.com/cosmicc/rf_info',
    version='0.9.0',
    zip_safe=False,
)
