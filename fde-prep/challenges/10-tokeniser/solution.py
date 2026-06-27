"""10 — tokeniser. First pass in plain text (see ../../CONSTRAINTS.md)."""


def tokenize(s):
    """Split s into (KIND, value) tuples: NUMBER (int), WORD (str of letters), PUNCT (single
    char). Whitespace separates and yields nothing.

    >>> tokenize("ab12, c!")
    [('WORD', 'ab'), ('NUMBER', 12), ('PUNCT', ','), ('WORD', 'c'), ('PUNCT', '!')]
    """
    raise NotImplementedError


def tokenize_identifiers(s):
    """Follow-up. Like tokenize, but a WORD may contain digits after its first letter
    (identifier rules): "x1" -> ("WORD", "x1"); "12x" -> NUMBER 12 then WORD x."""
    raise NotImplementedError
