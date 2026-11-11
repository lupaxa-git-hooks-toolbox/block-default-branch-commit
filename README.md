<p align="center">
  <a href="https://github.com/lupaxa-git-hooks-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/git-hooks-toolbox/readme-logo.png" alt="Git Hooks Toolbox" />
  </a>
</p>

<h1 align="center">Block Default Branch Commit</h1>

Refuse a commit on the default branch.

The protected branch is `master`. Set `REMOTE_LOOKUP` to `True` in `src/pre-commit` to use `origin`'s HEAD branch instead. A failed lookup still uses `master`.

## Install With Setup Git Hooks

[setup-git-hooks](https://github.com/lupaxa-git-hooks-toolbox/setup-git-hooks) fetches `src/pre-commit` from this repository. In the consuming repo, add an entry to `hooks/pre-commit-config.yml`:

```yaml
- name: Block default branch
  filename: block-default-branch
  url: https://github.com/lupaxa-git-hooks-toolbox/block-default-branch-commit
  version: HEAD
```

That installs `hooks/pre-commit/NN-block-default-branch`. The multiplexer must already be installed as `.git/hooks/pre-commit`.

> **Note:** `setup-hooks --force` overwrites the generated file. An edit to `REMOTE_LOOKUP` in `hooks/pre-commit/NN-*` does not survive that reinstall. Change the constant in this repository, then install again.

## Remote Lookup

`REMOTE_LOOKUP` defaults to `False`. `True` runs `git remote show origin` on every commit and protects the `HEAD branch` it prints. There is no separate config file for the flag.

## Development

These steps are only for changing this repository. Using the hook does not need a pip install.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install pytest ruff mypy bump-my-version
python -m pytest
```

<a href="https://github.com/the-lupaxa-project">
  <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
