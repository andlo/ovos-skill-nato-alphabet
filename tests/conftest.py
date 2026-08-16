"""Shared pytest fixtures for the NATO alphabet skill test suite."""
import importlib.util
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

_INIT_PATH = Path(__file__).resolve().parents[1] / "__init__.py"
_spec = importlib.util.spec_from_file_location("nato_skill", _INIT_PATH)
_module = importlib.util.module_from_spec(_spec)
sys.modules["nato_skill"] = _module
_spec.loader.exec_module(_module)

NatoAlphabet = _module.NatoAlphabet


@pytest.fixture
def skill(monkeypatch):
    s = NatoAlphabet.__new__(NatoAlphabet)
    s.log = MagicMock()
    s.skill_id = "ovos-skill-nato-alphabet.test"
    s.status = MagicMock()
    s._bus = MagicMock()
    monkeypatch.setattr(NatoAlphabet, "lang", "en-us", raising=False)
    s.res_dir = str(Path(__file__).resolve().parents[1])
    s._lang_resources = {}
    return s
