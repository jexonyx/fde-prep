"""When FDE_REFERENCE=1 (set by `verify.py --reference`), transparently import the matching
reference solution instead of the local `solution.py`, so the harness can confirm every test
tier is reachable. Without the env var, does nothing and your own `solution.py` is used.
"""
import importlib.util
import os
import sys
from pathlib import Path

if os.environ.get("FDE_REFERENCE"):
    _here = Path(__file__).parent
    _ref = _here.parent.parent / "reference" / (_here.name + ".py")
    _spec = importlib.util.spec_from_file_location("solution", _ref)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    sys.modules["solution"] = _mod
