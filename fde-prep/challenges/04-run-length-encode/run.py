"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import encode, decode

if __name__ == "__main__":
    s = "aaabbbbc"
    e = encode(s)
    print(f"encode({s!r}) -> {e!r}")
    print(f"decode({e!r}) -> {decode(e)!r}")
