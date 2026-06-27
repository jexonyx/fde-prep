"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import EventLog

if __name__ == "__main__":
    log = EventLog()
    log.append(1, "click", {"x": 10})
    log.append(2, "view", {"page": "home"})
    log.append(3, "click", {"x": 20})
    print("by_type('click'):", log.by_type("click"))
    print("in_range(2, 3):", log.in_range(2, 3))
    print("count_by_type():", log.count_by_type())
