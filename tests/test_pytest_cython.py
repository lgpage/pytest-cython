from __future__ import absolute_import

import sysconfig

import py
import pytest
from setuptools.sandbox import run_setup

import pytest_cython.plugin


PATH = py.path.local(__file__).dirpath()
PATH = PATH.join('example-project', 'src', 'pypackage')
EXT_SUFFIX = sysconfig.get_config_var("EXT_SUFFIX") or '.so'


def get_module(basename, suffix=EXT_SUFFIX):
    return PATH.join(basename + suffix)


@pytest.fixture(scope='module', autouse=True)
def build_example_project():
    path = py.path.local(__file__).dirpath()
    setup_py = path.join('example-project', 'setup.py')
    run_setup(str(setup_py), ['build_ext', '--inplace'])


def test_cython_ext_module(testdir):
    module = get_module('cython_ext_module')
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*Eggs.__init__ *PASSED*",
        "*Eggs.blarg*PASSED*",
        "*Eggs.fubar*PASSED*",
    ])
    assert result.ret == 0


def test_wrap_c_ext_module(testdir):
    module = get_module('wrap_c_ext_module')
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


def test_wrap_cpp_ext_module(testdir):
    module = get_module('wrap_cpp_ext_module')
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


def test_pure_py_module(testdir):
    module = get_module('pure_py_module', suffix='.py')
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*Eggs.__init__*PASSED*",
        "*Eggs.foo*PASSED*",
        "*foo*PASSED*",
    ])
    assert result.ret == 0
