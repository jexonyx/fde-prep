# Primer 00b — OOP for this interview

**~15–20 min.** The interview's format is "build a small stateful class, then extend it," so
you need the class mechanics to be automatic. This primer reloads exactly the OOP you'll
reach for — nothing more.

## How to use it

1. Read and run `primer.py`: `python primer.py`. Every section ends in `assert`s — a clean
   run means every class behaved as the comments claim.
2. Fill in the six TODOs in `exercises.py` (build a tiny `Point` and a `Tally` class).
3. Gate: `pytest test_primer.py`.

## What this covers

- `__init__` and `self` — what the instance actually is
- **instance vs class attributes** (the shared-mutable-default trap)
- methods, and returning `self` for chaining
- `__repr__` — and why it makes every debug session saner
- `__eq__` **and** `__hash__` together — the rule that they must agree
- **why tuples are hashable and make good dict keys** (directly relevant: "tuples, hashes")
- when `@dataclass` saves the boilerplate vs writing it by hand
- raising and catching exceptions cleanly — `KeyError`, and a custom exception
