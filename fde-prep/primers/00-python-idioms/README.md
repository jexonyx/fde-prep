# Primer 00 — Python idioms

**~15–20 min.** Not a problem to solve — a narrated cheat-sheet to reload the everyday
toolkit before you touch any challenge.

## How to use it

1. Read `primer.py` top to bottom. Every section ends in an `assert`, so **running the file
   is the check**: `python primer.py`. Clean exit = every idiom shown did what the comment
   said it would. Read the asserts — they are the "expected output."
2. Then open `exercises.py` and fill in the six TODOs (one or two lines each). The point is to
   *type* the idioms, not just read them.
3. Gate yourself: `pytest test_primer.py`.

## What this covers

- list / dict / set / tuple creation and core ops
- indexing and **slicing** (`s[::-1]`, `s[1:-1]`, `s[::2]`)
- `dict.get(k, default)`, `collections.defaultdict`, `dict.items()`
- **comprehensions** (list / dict / set) — and when a plain loop reads better
- **f-strings**
- `enumerate`, `zip`, unpacking (`a, *rest = ...`)
- `sorted(..., key=..., reverse=...)`
- common string methods: `.split`, `.join`, `.strip`, `.lower`, `.isdigit`
- truthiness and the empty-collection gotchas
- `in` membership: dict/set (O(1)) vs list (O(n)) — and why
