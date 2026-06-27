# CONSTRAINTS — the practice discipline

The interview is **Python, OOP, no IDE, no autocomplete, no AI, no running code**. If you
practise with all those crutches on, you are not practising the thing being tested. These
constraints exist to reproduce the real round. Read them once, then hold yourself to them.

## 1. First pass in plain text

Do the **first pass of every challenge in a plain text editor or a Google Doc** — no
autocomplete, no linting, no syntax highlighting that fixes your brackets, and **do not run
it**. Write the whole thing by hand, top to bottom, the way you will at the whiteboard / in
the shared doc.

Only once you believe it is correct do you paste it into `solution.py` and run
`pytest test_solution.py`. The test run is your *first* feedback — exactly like the
interviewer asking "shall we run it?" at the end.

## 2. Narrate out loud

Talk (or record yourself) through the same five beats every time. This is scored as heavily
as the code:

1. **Clarify** — restate the problem, ask the assumptions out loud (input size? duplicates?
   case sensitivity? what happens on empty / missing?).
2. **State approach** — name your data structure and *why* before you type ("I'll use a dict
   keyed by the sorted-letter tuple, because anagrams share a signature and dict lookup is
   O(1)").
3. **Code** — keep narrating: what each function does, why this name.
4. **Hand-trace one example** — walk a concrete input through your code by hand. This is how
   you catch the bug before they do.
5. **State complexity** — time and space, and justify it.

Each challenge README ends with **Narration prompts** — the specific things to say for that
problem. Actually say them.

## 3. Treat follow-ups as a second timed pass

The follow-up extensions in each README are not optional polish — they *are* the interview.
The first version is the warm-up; the follow-up is where they watch how you extend a design.

- Do the base version, get its tests green.
- Then start a **fresh timer** and do the follow-up.
- Try to extend **without rewriting** the original — clean seams (a method you can add, a
  parameter with a default, a strategy you can swap) score far better than a teardown. If you
  find yourself rewriting, that is a signal your first design missed a degree of freedom;
  notice it out loud.

## 4. Only check the reference after attempting

`reference/` holds full worked solutions. Opening one before you have a passing (or
genuinely stuck) attempt robs you of the rep. Attempt → run tests → *then* diff against the
reference and ask "what did they do more cleanly than me?"
