#!/usr/bin/env python
# -*- encoding: utf-8 -*-


if __name__ == "__main__":
    import os
    import sys

    from setuptools import setup
    from setuptools import Extension
    from Cython.Build import cythonize

    directives = {
        'profile': True,
        'embedsignature': False,
        'linetrace': False,
        'language_level': sys.version_info[0],
        # this is the default, but use it explicitly in case that ever
        # changes
        'autotestdict': True
    }

    # Enable code coverage for C code: we can't use CFLAGS=-coverage in
    # tox.ini, since that may mess with compiling dependencies (e.g. numpy).
    # Therefore we set SETUPPY_CFLAGS=-coverage in tox.ini and copy it to
    # CFLAGS here (after deps have been safely installed).
    macros = []
    if 'TOXENV' in os.environ and 'SETUPPY_CFLAGS' in os.environ:
        os.environ['CFLAGS'] = os.environ['SETUPPY_CFLAGS']
        if '-coverage' in os.environ['SETUPPY_CFLAGS']:
            directives['linetrace'] = True
            macros = [[('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1')]]


    extensions = [
        Extension('*', ['src/pypackage/*.pyx'], define_macros=macros)
    ]

    setup(
        name='pytest-cython',
        version='0.2.1',
        description="Example Cython project for pytest-cython tests",
        package_dir={'': 'src'},
        packages=['pypackage'],
        zip_safe=False,
        ext_modules=cythonize(extensions, compiler_directives=directives)
    )
