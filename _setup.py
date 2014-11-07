#!/usr/bin/env python3

import imp, json, os, sys
from setuptools import find_packages
try:
    from cx_Freeze import setup, Executable
except:
    from setuptools import setup

_srcdir = 'source'
_my_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.join(_my_path, _srcdir))

from you_get.utils import log
def gopen(filename, exit_code=1):
    try:
        return open(os.path.join(_my_path, filename), encoding='utf-8').read()
    except:
        log.wtf("Failed to open file: %s" % filename, exit_code=exit_code)
        return ''

_proj_name = 'you-get'
_program_name = 'you-get'
_package_name = 'you_get'

_metadata = json.loads(gopen("%s.json" % _proj_name))
_version = imp.load_source('version', os.path.join(_my_path, _srcdir, _package_name, 'version.py')).__version__

_readme = gopen('README.rst')
_changelog = gopen('CHANGELOG.rst')

setup(
    name = _metadata['name'],
    version = _version,

    author = _metadata['author'],
    author_email = _metadata['author_email'],
    url = _metadata['url'],
    license = _metadata['license'],

    description = _metadata['description'],
    keywords = _metadata['keywords'],

    long_description = _readme + '\n\n' + _changelog,

    packages = find_packages(_srcdir),
    package_dir = {'' : _srcdir},

    test_suite = 'tests',

    platforms = 'any',
    zip_safe = False,
    include_package_data = True,

    classifiers = _metadata['classifiers'],

    entry_points = {'console_scripts': _metadata['console_scripts']},

    executables = [Executable(
        script = _program_name,
        base = 'Console'
        )] if 'Executable' in vars() else None,
)
