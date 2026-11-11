#!/usr/bin/env python3
"""Semantic-version shape for src/pre-commit. Do not assert a literal version."""

from __future__ import annotations

import importlib.util
from importlib.machinery import SourceFileLoader
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "src" / "pre-commit"


def _load_script():
    loader = SourceFileLoader("block_default_branch_commit_version", str(SCRIPT))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load src/pre-commit")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_version_is_semantic():
    version = _load_script().__version__
    assert isinstance(version, str)
    parts = version.split(".")
    assert len(parts) >= 2
    assert all(part.isdigit() for part in parts[:2])
