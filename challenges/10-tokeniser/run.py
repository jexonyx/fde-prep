"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import tokenize, tokenize_identifiers

if __name__ == "__main__":
    s = "ab12, c!"
    print(f"tokenize({s!r}):")
    for tok in tokenize(s):
        print("  ", tok)
    print("tokenize_identifiers('var2 = 7'):", tokenize_identifiers("var2 = 7"))
