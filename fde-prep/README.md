# fde-prep — Google GenAI FDE coding practice

A graded ladder of small Python challenges that reloads the everyday idioms and then drills
the interview's real format: **build a small stateful class, then extend it.** No graphs, no
DP, no exotic algorithms — just strings, lists, dicts, and classes, with the edge-case load
rising as you go. Practise it the way the round actually runs (plain text, narrate out loud,
no autocomplete) — the rules live in [CONSTRAINTS.md](CONSTRAINTS.md). **Read that first.**

**Start here →** `cd primers/00-python-idioms`, read `primer.py`, do the exercises, then
work down the ladder below.

## Two ways to verify

1. **Smoke check** — inside any challenge dir, `python run.py` prints a couple of worked
   examples so you can eyeball that your solution behaves.
2. **The real gate** — inside any challenge dir, `pytest test_solution.py`. Tests are tiered
   `TestBasic → TestEdge → TestStretch`; the stretch tier hides the nasty cases and the
   follow-up extensions.

From the repo root, `python verify.py` runs everything and prints your progress board.
Run `pip install -r requirements.txt` once first (pytest only).

## The ladder

### Phase Zero — syntax primers (do these first)
- [ ] `primers/00-python-idioms` — list/dict/set/tuple ops, slicing, comprehensions, `get`/`defaultdict`, `enumerate`/`zip`/unpacking, `sorted(key=)`, string methods, truthiness
- [ ] `primers/00b-oop-primer` — `__init__`/`self`, instance vs class attrs, `__repr__`, `__eq__`+`__hash__`, hashable tuples as dict keys, `@dataclass`, exceptions

### Tier 0 — Rust-off: pure functions, idiom reload
- [ ] `01-word-frequency` — count word occurrences · `dict.get`/`defaultdict`, case-folding
- [ ] `02-pair-with-target` — two indices summing to target · dict-as-lookup
- [ ] `03-group-anagrams` — group anagrams · tuple keys / sorted signatures
- [ ] `04-run-length-encode` — `"aaabb"`→`"a3b2"` and back · string building, round-trip
- [ ] `05-merge-sorted` — merge two sorted lists · clean two-pointer control flow

### Tier 1 — one small stateful class
- [ ] `06-counter-class` — `increment`/`decrement`/`most_common(n)` · first class
- [ ] `07-min-stack` — `push`/`pop`/`top`/`get_min`, all O(1) · auxiliary structure
- [ ] `08-kv-store` — `get`/`set`/`delete`/`exists` · `KeyError` vs sentinel defaults
- [ ] `09-lru-cache` — `LRUCache(capacity)` with O(1) `get`/`put` · dict + ordering
- [ ] `10-tokeniser` — split into `(KIND, value)` tokens · char-class control flow + tuples

### Tier 2 — class + extension, real edge cases
- [ ] `11-kv-ttl` — kv-store with TTL expiry · injectable clock, lazy vs active expiry
- [ ] `12-event-log` — append events, query by type and time range · aggregation
- [ ] `13-rate-limiter` — `allow(user)`, fixed then sliding window · injectable clock
- [ ] `14-mini-table` — `insert(row)` / `select(**filters)` · predicate + projection
- [ ] `15-trie` — `insert`/`search`/`starts_with` · nested nodes, autocomplete
- [ ] `16-mini-sheet` — cells, then references, then cycle detection · the steep step
### Tier 3 — multi-method systems, hardest edges + complexity
- [ ] `17-calc` — evaluate `+ - * /` with precedence · tokenise → parse → eval, parens
- [ ] `18-path-query` — get/set by `"a.b.0.c"` path · intermediate-node creation, defaults
- [ ] `19-versioned-store` — `set`/`get`/`get_at`/`revert` · snapshots
- [ ] `20-pubsub` — `subscribe`/`publish`/`unsubscribe` · wildcard topics, handler isolation
- [ ] `21-window-topk` — top-K frequent in a sliding window · eviction-heavy
- [ ] `22-fs-tree` — `mkdir`/`add_file`/`ls`/`find`/`du`/`mv` · class tree + recursion

## Workflow per challenge

1. Read the challenge `README.md` — spec, worked example, constraints, follow-ups, narration
   prompts.
2. Write your **first pass in plain text**, narrating (see CONSTRAINTS.md).
3. Paste into `solution.py`, run `pytest test_solution.py`.
4. Do the follow-ups as a **second timed pass** — they map to `TestStretch`.
5. Only then diff against `reference/<name>.py` and ask what was cleaner.
