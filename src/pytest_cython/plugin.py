""" discover and run doctests in Cython extension modules."""
from __future__ import absolute_import

import sys
import pytest

try:
    import sysconfig
except ImportError:
    from distutils import sysconfig

import _pytest
from _pytest.doctest import get_optionflags
from _pytest.doctest import DoctestItem

try:
    from _pytest.doctest import _get_checker
except ImportError:
    _get_checker = None


def pytest_addoption(parser):
    group = parser.getgroup("cython")
    group.addoption(
        "--doctest-cython",
        action="store_true",
        default=False,
        help="run doctests in all .so and .pyd modules",
        dest="doctest_cython",
        )
    group.addoption(
        "--cython-ignore-import-errors",
        action="store_true",
        default=False,
        help="ignore doctest ImportErrors",
        dest="doctest_ignore_import_errors",
        )


def _find_matching_pyx_file(path, extensions):
    for ext in extensions:
        newpath = path.new(ext=ext)
        if newpath.check():
            return newpath


def pytest_collect_file(path, parent):
    bin_exts = ['.so']
    cy_exts = ['.pyx', '.py']  # collect .so files if .py file exists
    ext_suffix = sysconfig.get_config_var("EXT_SUFFIX")

    config = parent.config
    if path.ext in bin_exts:
        if config.getoption('--doctest-cython'):
            if ext_suffix is None:
                bin_file = path
                # XXX EXT_SUFFIX is None for pypy (python2.7)
                if '.pypy' in path.basename:
                    basename = path.basename.split('.')[0]
                    bin_file = path.new(purebasename=basename, ext=path.ext)

            else:
                basename = path.basename.replace(ext_suffix, "")
                bin_file = path.new(purebasename=basename, ext=path.ext)

            pyx_file = _find_matching_pyx_file(bin_file, cy_exts)
            # only run test if matching .so and .pyx files exist
            # create addoption for this ??
            if pyx_file is not None:
                return DoctestModule(path, parent)


# XXX patch pyimport to support PEP 3149
def _patch_pyimport(fspath, **kwargs):
    ext_suffix = sysconfig.get_config_var("EXT_SUFFIX")
    # XXX EXT_SUFFIX is None for pypy (python2.7)
    if ext_suffix is None and '.pypy' not in fspath.basename:
        return fspath.pyimport(**kwargs)

    else:
        # XXX EXT_SUFFIX is None for pypy (python2.7)
        if '.pypy' in fspath.basename:
            ext_suffix = fspath.ext
            basename = fspath.basename.split('.')[0]
            fspath = fspath.new(purebasename=basename, ext=fspath.ext)

        pkgroot = fspath.dirpath()
        fspath._ensuresyspath(True, pkgroot)
        names = fspath.relto(pkgroot).split(fspath.sep)
        modname = ".".join(names).replace(ext_suffix, "")
        __import__(modname)
        return sys.modules[modname]


class DoctestModule(pytest.Module):

    def collect(self):
        import doctest

        if self.fspath.basename == "conftest.py":
            module = self.config.pluginmanager._importconftest(self.fspath)
        else:
            try:
                # XXX patch pyimport in pytest._pytest.doctest.DoctestModule
                module = _patch_pyimport(self.fspath)
            except ImportError:
                if self.config.getoption('--cython-ignore-import-errors'):
                    pytest.skip('unable to import module %r' % self.fspath)
                else:
                    raise

        # uses internal doctest module parsing mechanism
        finder = doctest.DocTestFinder()
        optionflags = get_optionflags(self)
        checker = None if _get_checker is None else _get_checker()
        runner = doctest.DebugRunner(verbose=0, optionflags=optionflags,
                                     checker=checker)
        for test in finder.find(module, module.__name__):
            if test.examples:  # skip empty doctests
                yield DoctestItem(test.name, self, runner, test)

    def _importtestmodule(self):
        # we assume we are only called once per module
        importmode = self.config.getoption("--import-mode", default=True)
        try:
            # XXX patch pyimport in pytest._pytest.pythod.Module
            mod = _patch_pyimport(self.fspath, ensuresyspath=importmode)
        except SyntaxError:
            raise self.CollectError(
                _pytest._code.ExceptionInfo().getrepr(style="short"))
        except self.fspath.ImportMismatchError:
            e = sys.exc_info()[1]
            raise self.CollectError(
                "import file mismatch:\n"
                "imported module %r has this __file__ attribute:\n"
                "  %s\n"
                "which is not the same as the test file we want to collect:\n"
                "  %s\n"
                "HINT: remove __pycache__ / .pyc files and/or use a "
                "unique basename for your test file modules"
                % e.args
            )
        # print "imported test module", mod
        self.config.pluginmanager.consider_module(mod)
        return mod
