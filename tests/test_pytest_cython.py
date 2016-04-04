import pytest_cython.plugin


SCRIPT = '''
def foo(a, b):
    """
    >>> foo(1, 1)
    2
    """
    return a + b
'''


def test_main():
    assert pytest_cython.plugin  # use your library here


def test_simple(testdir):
    script = testdir.makepyfile(SCRIPT)
    result = testdir.runpytest('-v', '--doctest-cython', script)
    assert False
    print result
