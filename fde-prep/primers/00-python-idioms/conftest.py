"""When FDE_REFERENCE=1 (set by `verify.py --reference`), transparently import the completed
reference instead of the local `exercises.py`, so the harness can confirm every drill is
reachable. Without the env var this file does nothing and your own `exercises.py` is used.
"""
import importlib.util
import os
import sys
from pathlib import Path

if os.environ.get("FDE_REFERENCE"):
    _here = Path(__file__).parent
    _ref = _here.parent.parent / "reference" / (_here.name + ".py")
    _spec = importlib.util.spec_from_file_location("exercises", _ref)
    _mod = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_mod)
    sys.modules["exercises"] = _mod
