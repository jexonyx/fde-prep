# 14 — mini-table

**Tier 2 · ~30 min.**

## Concepts drilled
Rows as dicts, an **equality where-clause** built from `**kwargs`, the `all(...)` predicate
idiom, then generalising to an arbitrary predicate function and **column projection**.

## Problem statement
Build an in-memory `MiniTable`:
- `insert(row)` — `row` is a dict of `column -> value`. Store a copy (later mutation of the
  caller's dict must not change the table).
- `select(**filters)` — return all rows where **every** `column == value` in `filters` holds.
  No filters → all rows. Return a list of row dicts (copies).

## Worked example
```
t = MiniTable()
t.insert({"name": "Ada", "city": "London", "age": 36})
t.insert({"name": "Bo",  "city": "London", "age": 28})
t.insert({"name": "Cy",  "city": "Paris",  "age": 36})
t.select(city="London")          # -> the Ada and Bo rows
t.select(city="London", age=36)  # -> just the Ada row
```

## Constraints / assumptions
- A filter on a column a row doesn't have fails to match that row (treat missing as not
  equal, unless the filter value is `None`).
- Rows keep insertion order in the results.

## Follow-up extensions  → `TestStretch`
1. **Predicate select:** `where(predicate)` returns the rows for which `predicate(row)` is
   truthy — for range/inequality queries the equality filter can't express.
2. **Projection:** extend `select` to take positional column names —
   `select("name", "age", city="London")` returns rows narrowed to just those columns. With
   no positional columns, return whole rows.

## Edge cases to consider
- Empty table; filters that match nothing.
- Filtering on a column some rows lack.
- Projecting a column some rows lack (decide: omit, or include as `None`? state it).

## Complexity target
`insert` O(1). `select` / `where` O(n · f) for n rows and f filters. (Mention that a real DB
would index a column to beat the linear scan.)

## Narration prompts
- "Rows are dicts; a select is a filter where `all(row.get(col) == val for col, val in
  filters.items())`."
- Call out the defensive copy on insert and why it matters.
- For projection, state how you handle a projected column that a row is missing.
