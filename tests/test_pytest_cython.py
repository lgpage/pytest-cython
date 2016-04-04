import py

import pytest_cython.plugin

PATH = py.path.local(__file__).dirpath()
PATH = PATH.join('example-project', 'src', 'pypackage')


def test_cython_ext_module(testdir):
    module = 'cython_ext_module.so'
    result = testdir.runpytest('-v', '--doctest-cython', str(PATH.join(module)))
    result.stdout.fnmatch_lines([
        "*Eggs.__init__ *PASSED",
        "*Eggs.blarg*PASSED",
        "*Eggs.fubar*PASSED",
    ])
    assert result.ret == 0


def test_wrap_c_ext_module(testdir):
    module = 'wrap_c_ext_module.so'
    result = testdir.runpytest('-v', '--doctest-cython', str(PATH.join(module)))
    result.stdout.fnmatch_lines([
        "*sqr*PASSED",
    ])
    assert result.ret == 0


def test_wrap_cpp_ext_module(testdir):
    module = 'wrap_cpp_ext_module.so'
    result = testdir.runpytest('-v', '--doctest-cython', str(PATH.join(module)))
    result.stdout.fnmatch_lines([
        "*sqr*PASSED",
    ])
    assert result.ret == 0


def test_pure_py_module(testdir):
    module = 'pure_py_module.py'
    result = testdir.runpytest('-v', '--doctest-cython', str(PATH.join(module)))
    result.stdout.fnmatch_lines([
        "*Eggs.__init__*PASSED",
        "*Eggs.foo*PASSED",
        "*foo*PASSED",
    ])
    assert result.ret == 0
