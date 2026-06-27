# 18 — path-query

**Tier 3 · ~35 min.**

## Concepts drilled
Walking a heterogeneous nested structure (dicts **and** lists), dispatching on node type,
**sentinel-default vs raising**, and mutating-with-intermediate-creation on the way back.

## Problem statement
Given nested data (dicts and lists) and a dotted **path string** like `"a.b.0.c"`, look up the
value. Each path segment is a dict key, **or** a list index when the current node is a list.
Write:
- `get_path(data, path, default=_MISSING)` — return the value at `path`. If any segment is
  missing/out-of-range, raise `KeyError` — unless a `default` is supplied, in which case
  return it.

## Worked example
```
data = {"a": {"b": [{"c": 42}]}}
get_path(data, "a.b.0.c")          # -> 42
get_path(data, "a.b.5.c")          # -> raises KeyError
get_path(data, "a.x", default=0)   # -> 0
```

## Constraints / assumptions
- Segments are split on `.`. A numeric segment indexes a list (`int(segment)`); a non-numeric
  segment keys a dict.
- Trying to descend into a scalar (e.g. path continues past a leaf) is a miss.
- `default` may itself be `None`, so detect "no default" with a sentinel, not `None`.

## Follow-up extensions  → `TestStretch`
1. `set_path(data, path, value)` — set the value at `path`, **creating intermediate dicts**
   for any missing keys along the way, then return `data`. Traversing an existing list by
   index works; a segment whose existing value is a scalar gets replaced by a dict so the
   path can continue. (Decide and state how you treat list-vs-dict creation.)

## Edge cases to consider
- Missing key vs missing list index vs descending into a scalar.
- `default=None` returned (not raised) on a miss.
- `set_path` building a path from an empty dict; overwriting an existing leaf.

## Complexity target
O(d) for a path of depth d, both get and set.

## Narration prompts
- "At each step I check whether the current node is a list (index it) or a dict (key it), and
  treat anything else as a miss."
- Explain the sentinel default: "I can't use `None` as 'no default' because `None` is a valid
  default value."
- For `set_path`, say your rule for creating intermediates before you write it.
