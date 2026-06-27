# 04 — run-length-encode

**Tier 0 · ~20 min.**

## Concepts drilled
Building a string from runs, a single forward scan tracking "current run," multi-digit
parsing on the way back, and the **round-trip property** as a correctness check.

## Problem statement
Write two functions:
- `encode(s)` — compress runs of the same character to `char + count`. The count is **always
  written**, even when it's 1. `"aaabb"` → `"a3b2"`, `"abc"` → `"a1b1c1"`.
- `decode(s)` — the inverse: `"a3b2"` → `"aaabb"`. Counts may be multi-digit (`"a12"` → twelve
  a's), so you can't assume one digit per run.

## Worked example
```
encode("aaabb")   # -> "a3b2"
encode("abc")     # -> "a1b1c1"
decode("a3b2")    # -> "aaabb"
decode("a12")     # -> "aaaaaaaaaaaa"
```

## Constraints / assumptions
- `encode` input contains **no digits** (digits in the data would make the encoding
  ambiguous). State this assumption out loud — it's the kind of clarifying question they want.
- Letters are case-sensitive (`"aA"` → `"a1A1"`).

## Follow-up extensions  → `TestStretch`
1. **Round-trip property:** for any valid input `x`, `decode(encode(x)) == x`. Make your two
   functions agree on the format so this holds, and be ready to argue *why* it holds rather
   than just testing a few cases.

## Edge cases to consider
- Empty string (both directions).
- Single character; a string with no repeats.
- Long runs that produce multi-digit counts.

## Complexity target
Both O(n) time over the string length, O(n) space for the output. The two-pointer / digit
scan in `decode` should not be quadratic.

## Narration prompts
- Before coding `encode`: "I track the current character and a running count; when the next
  char differs I flush `char+count` and reset."
- For `decode`, say how you handle multi-digit counts: "read one char, then consume *all*
  following digits before converting."
- State the round-trip invariant and why writing the count unconditionally guarantees it.
