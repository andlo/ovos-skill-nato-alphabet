"""Smoke test: confirms the skeleton skill imports cleanly. Replace/
expand once real implementation lands - see DEVELOPMENT.md."""
import importlib.util
from pathlib import Path


def test_module_imports_without_error():
    init_path = Path(__file__).resolve().parents[1] / "__init__.py"
    spec = importlib.util.spec_from_file_location("skeleton_skill", init_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module is not None
