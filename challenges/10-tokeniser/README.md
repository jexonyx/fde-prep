# 10 — tokeniser

**Tier 1 · ~25 min.** Closes Tier 1 and sets up the parsing work in Tier 3 (see `17-calc`).

## Concepts drilled
Character-class control flow, the **"consume a run" inner loop**, returning `(KIND, value)`
**tuples**, integer parsing.

## Problem statement
Write `tokenize(s)` that splits a string into a list of `(KIND, value)` tuples:
- `("NUMBER", n)` — a maximal run of digits, `value` is the **int**.
- `("WORD", w)` — a maximal run of letters, `value` is the **string**.
- `("PUNCT", c)` — any single non-alphanumeric, non-whitespace character, one token each.
- Whitespace is a separator and produces no tokens.

## Worked example
```
tokenize("ab12, c!")
# -> [("WORD", "ab"), ("NUMBER", 12), ("PUNCT", ","), ("WORD", "c"), ("PUNCT", "!")]

tokenize("100")        # -> [("NUMBER", 100)]
tokenize("")           # -> []
```

## Constraints / assumptions
- Numbers are non-negative integer runs; `"007"` → `("NUMBER", 7)`.
- A WORD is letters only in the base version; `"ab12"` splits into a WORD then a NUMBER.
- Punctuation never merges: `"!!"` → two `PUNCT` tokens.

## Follow-up extensions  → `TestStretch`
1. `tokenize_identifiers(s)` — like `tokenize`, but a WORD may contain digits **after** its
   first letter (programming-identifier rules). So `"x1"` → `("WORD", "x1")`, while `"12x"` →
   `("NUMBER", 12), ("WORD", "x")` (a token starting with a digit is still a NUMBER).

## Edge cases to consider
- Empty / whitespace-only input.
- Multi-digit numbers; leading zeros.
- Trailing punctuation; runs of punctuation.

## Complexity target
O(n) over the input — each character is consumed exactly once. Watch that your inner "consume
a run" loops advance the outer index so you don't rescan.

## Narration prompts
- "I'll branch on the character class at the current position, then greedily consume the rest
  of that run before emitting one token."
- Say why `value` is an `int` for NUMBER but the raw string for WORD/PUNCT.
- For the follow-up, state the one rule that changes: which characters a WORD may *continue*
  with.
