# 16 — mini-sheet

**Tier 2 · ~35 min.** The deliberately steep step in Tier 2 — the follow-ups change the data
model and force you to think about traversal and cycles.

## Concepts drilled
Storing cells in a dict, distinguishing **literals from references**, recursive resolution
with a **visited set**, and raising a **custom exception** on a reference cycle.

## Problem statement
Build a `MiniSheet` of named cells holding literal values:
- `set(cell, value)` — store a value at a cell (e.g. `set("A1", 5)`).
- `get(cell)` — return the cell's value. `KeyError` if the cell was never set.

## Worked example (base)
```
sheet = MiniSheet()
sheet.set("A1", 5)
sheet.set("A2", "hello")
sheet.get("A1")     # -> 5
sheet.get("A3")     # -> raises KeyError
```

## Constraints / assumptions
- Cell names are strings; values may be any literal.
- **Reference convention (for the follow-ups):** a value that is a string beginning with `"="`
  is a *reference* to another cell — `"=A1"` means "this cell's value is whatever `A1`
  resolves to." (A literal string that happens to start with `=` is out of scope; state this
  assumption.)

## Follow-up extensions  → `TestStretch`
1. **References:** `get` must resolve references, including **chains** (`A1 -> =A2 -> =A3 -> 7`
   returns `7`). A reference to an unset cell raises `KeyError`.
2. **Cycle detection:** if resolving a cell revisits a cell already on the current resolution
   path (`A1 -> =A2 -> =A1`, or a self-reference `A1 -> =A1`), raise `CycleError` (a custom
   exception you define and export from the module).

## Edge cases to consider
- A reference to a cell that doesn't exist.
- Self-reference; two-cell and longer cycles.
- Overwriting a reference with a literal (which should break a previously-cyclic chain).

## Complexity target
`get` is O(length of the reference chain). Cycle detection adds O(1) per hop with a visited
set; the chain length is bounded by the number of cells before a repeat.

## Narration prompts
- "Literals return directly; a `=`-prefixed string means recurse into the target cell."
- "To catch cycles I carry a set of cells currently being resolved; re-entering one is a
  cycle — I raise `CycleError`."
- Say why a fresh path-set per top-level `get` (not a global one) is the correct scope.
