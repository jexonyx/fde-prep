# 17 — calc

**Tier 3 · ~40 min.** Ties strings + parsing + OOP together; the natural sequel to
`10-tokeniser`.

## Concepts drilled
**Tokenise → parse → evaluate** as three clean stages, operator **precedence** and
**left-associativity**, recursive-descent parsing, and a recursive grammar for parentheses.

## Problem statement
Write `calc(expr)` that evaluates an arithmetic expression string with `+ - * /` and the usual
precedence (`*` and `/` bind tighter than `+` and `-`), left-to-right within a precedence
level. Numbers are non-negative integers (possibly multi-digit). Whitespace is insignificant.

## Worked example
```
calc("1 + 2")            # -> 3
calc("2 + 3 * 4")        # -> 14   (precedence)
calc("10 - 4 - 3")       # -> 3    (left-associative)
calc("8 / 2")            # -> 4
```

## Constraints / assumptions
- Operators: `+ - * /`. Integer literals only (no unary minus, no decimals).
- `/` is division; dividing by zero raises `ZeroDivisionError`. Results compare equal to ints
  where exact (`8 / 2 == 4`).
- A malformed expression may raise `ValueError` (you choose where; the tests don't probe it
  heavily).

## Follow-up extensions  → `TestStretch`
1. **Parentheses:** support `( ... )` to override precedence, nested arbitrarily —
   `calc("(2 + 3) * 4") == 20`, `calc("2 * (3 + 4) - 1") == 13`. The clean way is a recursive
   grammar: `expression := term (('+'|'-') term)*`, `term := factor (('*'|'/') factor)*`,
   `factor := NUMBER | '(' expression ')'`.

## Edge cases to consider
- Leading/trailing/internal whitespace; multi-digit numbers.
- Division by zero.
- A single bare number.

## Complexity target
O(n) tokenising, O(n) single-pass recursive-descent parse/eval. Be ready to contrast with the
shunting-yard / two-stack approach and say why both are O(n).

## Narration prompts
- "Three stages: tokenise to numbers and operator symbols, parse with a recursive-descent
  grammar that encodes precedence, evaluate as I parse."
- Say how the grammar levels (`expression` vs `term`) *are* the precedence.
- Call out left-associativity: the `while` loop folding left, not right recursion.
