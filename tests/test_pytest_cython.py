from __future__ import absolute_import

import pathlib
import pytest
import shutil

from setuptools.sandbox import run_setup

# import pytest_cython as a quite check to ensure it was installed before running tests
import pytest_cython.plugin


ROOT_PATH = pathlib.Path(__file__).parent
PROJECT_PATH = ROOT_PATH.joinpath('example-project')
PACKAGE_PATH = PROJECT_PATH.joinpath('src', 'pypackage')

IMPORT_MODES = ["append", "prepend", "importlib"]


def get_module(basename: str, suffix='.pyx') -> pathlib.Path:
    return PACKAGE_PATH.joinpath(basename + suffix)


def run_pytest(pytester: pytest.Pytester, module: pathlib.Path, import_mode) -> pytest.RunResult:
    return pytester.runpytest('-vv', '--doctest-cython', '--import-mode', import_mode, str(module))


@pytest.fixture(scope='module', autouse=True)
def build_example_project():
    shutil.rmtree(PROJECT_PATH.joinpath('build'), True)
    shutil.rmtree(PACKAGE_PATH.joinpath('__pycache__'), True)

    for file in PACKAGE_PATH.glob('*.pyd'):
        file.unlink()

    for file in PACKAGE_PATH.glob('*.c'):
        file.unlink()

    setup_py = PROJECT_PATH.joinpath('setup.py')
    run_setup(str(setup_py), ['build_ext', '--inplace'])


@pytest.mark.parametrize('import_mode', IMPORT_MODES)
def test_cython_ext_module(pytester, import_mode):
    module = get_module('cython_ext_module')
    assert module.exists()

    result = run_pytest(pytester, module, import_mode)
    result.stdout.fnmatch_lines([
        "*Eggs.__init__*PASSED*",
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
def test_wrap_c_ext_module(pytester, import_mode):
    module = get_module('wrap_c_ext_module')
    assert module.exists()

    result = run_pytest(pytester, module, import_mode)
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


@pytest.mark.parametrize('import_mode', IMPORT_MODES)
def test_wrap_cpp_ext_module(pytester, import_mode):
    module = get_module('wrap_cpp_ext_module')
    assert module.exists()

    result = run_pytest(pytester, module, import_mode)
    result.stdout.fnmatch_lines([
        "*sqr*PASSED*",
    ])
    assert result.ret == 0


@pytest.mark.parametrize('import_mode', IMPORT_MODES)
def test_pure_py_module(pytester, import_mode):
    module = get_module('pure_py_module', suffix='.py')
    assert module.exists()

    result = run_pytest(pytester, module, import_mode)
    result.stdout.fnmatch_lines([
        "*Eggs.__init__*PASSED*",
        "*Eggs.foo*PASSED*",
        "*foo*PASSED*",
    ])
    assert result.ret == 0
