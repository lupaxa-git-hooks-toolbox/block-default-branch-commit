# The hook is one script. Install the dev tools. Do not build a package.
PIP_INSTALL_DEV = pytest ruff mypy bump-my-version
PIP_INSTALL_TEST = pytest
MYPY_ARGS = src/pre-commit
