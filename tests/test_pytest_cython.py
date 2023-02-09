from __future__ import absolute_import

import py
import pytest
from setuptools.sandbox import run_setup

import pytest_cython.plugin


PATH = py.path.local(__file__).dirpath()
PATH = PATH.join('example-project', 'src', 'pypackage')

PYTEST_MAJOR_VERSION = int(pytest.__version__.split('.')[0])
IMPORT_MODES = ['prepend', 'append']
if PYTEST_MAJOR_VERSION >= 6:
    IMPORT_MODES.insert(0, 'importlib')


def get_module(basename, suffix='.pyx'):
    return PATH.join(basename + suffix)


def run_pytest(testdir, module, import_mode):
    return testdir.runpytest('-vv', '--doctest-cython', '--import-mode', import_mode, str(module))


@pytest.fixture(scope='module', autouse=True)
def build_example_project():
    path = py.path.local(__file__).dirpath()
    setup_py = path.join('example-project', 'setup.py')
    run_setup(str(setup_py), ['build_ext', '--inplace'])


@pytest.mark.parametrize('import_mode', IMPORT_MODES)
def test_cython_ext_module(testdir, import_mode):
    module = get_module('cython_ext_module')
    assert module.check()
    result = run_pytest(testdir, module, import_mode)
    result.stdout.fnmatch_lines([
        "*Eggs.__init__ *PASSED*",
        "*Eggs.blarg*PASSED*",
        "*Eggs.failing_test*FAILED*",
        "*Eggs.fubar*PASSED*",
        "*",
        "*FAILURES*",
        "*pypackage.cython_ext_module.Eggs.failing_test*",
        "078*",
        "079         >>> eggs = Eggs(1, 1)*",
        "080         >>> eggs.failing_test()*",
        "Expected:*",
        "    False*",
        "Got:*",
        "    True*"
    ])
    assert result.ret == 1


@pytest.mark.parametrize('import_mode', IMPORT_MODES)
def test_wrap_c_ext_module(testdir, import_mode):
    module = get_module('wrap_c_ext_module')
    assert module.check()
    result = run_pytest(testdir, module, import_mode)
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


@pytest.mark.parametrize('import_mode', IMPORT_MODES)
def test_wrap_cpp_ext_module(testdir, import_mode):
    module = get_module('wrap_cpp_ext_module')
    assert module.check()
    result = run_pytest(testdir, module, import_mode)
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


@pytest.mark.parametrize('import_mode', IMPORT_MODES)
def test_pure_py_module(testdir, import_mode):
    module = get_module('pure_py_module', suffix='.py')
    assert module.check()
    result = run_pytest(testdir, module, import_mode)
    result.stdout.fnmatch_lines([
        "*Eggs.__init__*PASSED*",
        "*Eggs.foo*PASSED*",
        "*foo*PASSED*",
    ])
    assert result.ret == 0
