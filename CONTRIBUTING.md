# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

## Bug reports

When [reporting a bug](https://github.com/lgpage/pytest-cython/issues)
please include:

- Your operating system name and version.
- The `cython` and `pytest` versions you are using
- Detailed steps to reproduce the bug.
- Any other details about your local setup that might be helpful in troubleshooting.

## Documentation improvements

`pytest-cython` could always use more documentation, whether as part of the official `pytest-cython` docs, in
docstrings, or even on the web in blog posts, articles, and such.

## Feature requests and feedback

The best way to send feedback is to [file an issue](https://github.com/lgpage/pytest-cython/issues). If you are
proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that code contributions are welcome :)

## Development

To set up `pytest-cython` for local development:

1. Fork [pytest-cython](https://github.com/lgpage/pytest-cython) (look for the \"fork\" button).

2. Clone your fork locally:

    ```shell
    git clone git@github.com:your_name_here/pytest-cython.git
    ```

3. Create a branch for local development:

    ```shell
    git checkout -b name-of-your-bugfix-or-feature
    ```

4. When you're done making changes, run all the checks and tests with  the [nox](https://tox.wiki/en/latest) command:

    ```shell
    nox
    ```

5. Commit your changes and push your branch to GitHub:

    ```shell
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```

6. Submit a pull request through the GitHub website.

## Pull Request Guidelines

If you need some code review or feedback while you're developing the code just make the pull request.

Before merging, you should:

1. Update the documentation when there's new API, functionality etc.
2. Add a note to `CHANGELOG.rst` about the changes.

## Tips

To list all [nox](https://tox.wiki/en/latest) tasks:

```shell
nox --list
```

To run a subset of tests use one of the task from the above list, for example:

```shell
nox --session "test(cython='0.29', python='3.9', pytest='7')"
```
