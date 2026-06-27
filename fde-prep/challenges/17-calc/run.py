"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import calc

if __name__ == "__main__":
    for expr in ["2 + 3 * 4", "10 - 4 - 3", "(2 + 3) * 4", "20 / (2 + 3)"]:
        print(f"calc({expr!r}) =", calc(expr))
