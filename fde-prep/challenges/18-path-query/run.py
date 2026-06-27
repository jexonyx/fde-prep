"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import get_path, set_path

if __name__ == "__main__":
    data = {"a": {"b": [{"c": 42}]}}
    print("get_path('a.b.0.c'):", get_path(data, "a.b.0.c"))
    print("get_path('a.x', default=0):", get_path(data, "a.x", default=0))
    fresh = {}
    set_path(fresh, "user.name", "Ada")
    print("after set_path('user.name', 'Ada'):", fresh)
