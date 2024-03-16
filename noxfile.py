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
@nox.parametrize('python', ["3.10", "3.11", "3.12"])
@nox.parametrize('pytest', ["8"])
@nox.parametrize('cython', ["0.29", "3"])
def test(session, pytest, cython):
    session.install("--upgrade", "setuptools")

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
