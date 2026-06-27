# 15 — trie

**Tier 2 · ~30 min.**

## Concepts drilled
A **prefix tree** built from nested dicts, walking it character by character, an **end-of-word
marker**, and a sorted depth-first traversal for autocomplete.

## Problem statement
Build a `Trie`:
- `insert(word)` — add a word.
- `search(word)` — `True` if the **exact** word was inserted.
- `starts_with(prefix)` — `True` if any inserted word has this prefix.

The distinction between `search` and `starts_with` is the point: walking to a node tells you
the prefix exists; an **end marker** at that node tells you a full word ends there.

## Worked example
```
t = Trie()
t.insert("app")
t.insert("apple")
t.search("app")          # -> True
t.search("ap")           # -> False   (prefix, not a full word)
t.starts_with("ap")      # -> True
t.starts_with("apx")     # -> False
```

## Constraints / assumptions
- Words are non-empty lowercase strings in the tests (the empty string is exercised once —
  decide what inserting/searching `""` means and be consistent).
- Use nested dicts (`char -> child node`) with a marker for "a word ends here." Avoid using a
  marker character that could collide with a real input character.

## Follow-up extensions  → `TestStretch`
1. `autocomplete(prefix)` — return **all** inserted words that begin with `prefix`, **sorted**
   ascending. If the prefix itself is a complete word, include it. Unknown prefix → `[]`.

## Edge cases to consider
- `search` for a prefix that is not a full word.
- A word that is a prefix of another (`"app"` and `"apple"`).
- `starts_with("")` and inserting/searching the empty string.

## Complexity target
`insert` / `search` / `starts_with`: O(L) for a word of length L. `autocomplete`: O(L +
total characters under the prefix), plus the sort.

## Narration prompts
- "Each node is a dict from character to child; I mark word-ends with a sentinel key so I can
  tell `search` from `starts_with`."
- Say how you avoid the marker colliding with a real letter.
- For autocomplete: "I walk to the prefix node, then DFS in sorted character order so results
  come out sorted without a separate sort step."
