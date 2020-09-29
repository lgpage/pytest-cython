from __future__ import absolute_import

import py
import sys

import pytest_cython.plugin

PATH = py.path.local(__file__).dirpath()
PATH = PATH.join('example-project', 'src', 'pypackage')
sys.path.insert(0, str(PATH))


def test_cython_ext_module(testdir):
    module = PATH.listdir(fil='cython_ext_module*.so')[0]
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*Eggs.__init__ *PASSED*",
        "*Eggs.blarg*PASSED*",
        "*Eggs.fubar*PASSED*",
    ])
    assert result.ret == 0


def test_wrap_c_ext_module(testdir):
    module = PATH.listdir(fil='wrap_c_ext_module*.so')[0]
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


def test_wrap_cpp_ext_module(testdir):
    module = PATH.listdir(fil='wrap_cpp_ext_module*.so')[0]
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


def test_pure_py_module(testdir):
    module = PATH.listdir(fil='pure_py_module*.py')[0]
    assert module.check()
    result = testdir.runpytest('-vv', '--doctest-cython', str(module))
    result.stdout.fnmatch_lines([
        "*Eggs.__init__*PASSED*",
        "*Eggs.foo*PASSED*",
        "*foo*PASSED*",
    ])
    assert result.ret == 0
