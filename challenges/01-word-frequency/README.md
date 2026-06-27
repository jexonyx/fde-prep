# 01 — word-frequency

**Tier 0 · ~20 min.**

## Concepts drilled
`dict.get` / `collections.defaultdict`, case-folding, stripping punctuation, `sorted(key=)`
with tuple tie-breaks.

## Problem statement
Write `word_frequency(text)` that returns a dict mapping each **word** to the number of times
it appears. Counting is **case-insensitive** ("The" and "the" are the same word), and
**leading/trailing punctuation** is stripped from each word ("cat." counts as "cat"). Words
are separated by whitespace. Empty input yields an empty dict.

## Worked example
```
word_frequency("The cat sat. The CAT ran!")
# -> {"the": 2, "cat": 2, "sat": 1, "ran": 1}
```

## Constraints / assumptions
- Input is a `str`; words are whitespace-delimited.
- "Word" = a token with surrounding punctuation (`. , ! ? ; :` etc.) stripped, lower-cased.
- A token that is *only* punctuation contributes nothing.
- Counts are returned in any order (it's a dict); the *follow-up* is where order matters.

## Follow-up extensions  → `TestStretch`
1. `top_n(text, n)` — return the `n` most frequent words as a list of `(word, count)` tuples,
   sorted by count **descending**, ties broken **alphabetically** (a stable, deterministic
   order). `n` larger than the vocabulary returns everything; `n == 0` returns `[]`.

## Edge cases to consider
- Empty string; strings that are only whitespace or only punctuation.
- Mixed case and repeated punctuation (`"hello!!!"`).
- (A couple more are hidden in `TestStretch` — think about ties and apostrophes.)

## Complexity target
`word_frequency`: O(total characters). `top_n`: O(V log V) for V distinct words (the sort).

## Narration prompts
- State your tokenisation choice *before* coding: "split on whitespace, then strip
  punctuation off each token" — and why that's simpler than a regex here.
- Name your counting structure (`dict` + `.get`, or `defaultdict(int)`) and why.
- For the follow-up, say the sort key out loud: "negative count primary, word secondary."
