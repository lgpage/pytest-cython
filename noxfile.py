import nox


@nox.session()
def lint(session):
    session.install("flake8")
    session.run("flake8", "src", "tests", "setup.py", "noxfile.py", "docs/conf.py")


@nox.session()
def check(session):
    session.install("build")
    session.install("twine")
    session.install("wheel")
    session.install("check-manifest")

    session.run("check-manifest")
    session.run("python", "-m", "build")
    session.run("twine", "check", "dist/*.*")


@nox.session
@nox.parametrize(
    "python,pytest",
    [
        (python, pytest)
        for python in ("3.9", "3.10", "3.11", "pypy3")
        for pytest in ("5", "6", "7")
        if (python, pytest) != ("3.10", "5") and (python, pytest) != ("3.11", "5")
    ],
)
@nox.parametrize('cython', ["0.29"])
def test(session, pytest, cython):
    session.install(f"pytest=={pytest}.*")
    session.install(f"cython=={cython}.*")
    session.install("-e", ".")

    session.run("pytest", "-vv", "tests", "src")


@nox.session()
def docs(session):
    session.install("-r", "docs/requirements.txt")
    session.install("-e", ".")

    session.run("sphinx-build", "-b", "spelling", "docs", "dist/docs")
    session.run("sphinx-build", "-b", "linkcheck", "docs", "dist/docs")
    session.run("sphinx-build", "-E", "-b", "html", "docs", "dist/docs")
