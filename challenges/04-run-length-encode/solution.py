"""04 — run-length-encode. First pass in plain text (see ../../CONSTRAINTS.md)."""


def encode(s):
    """Run-length encode s as char+count per run (count always written).

    >>> encode("aaabb")
    'a3b2'
    >>> encode("abc")
    'a1b1c1'
    """
    raise NotImplementedError


def decode(s):
    """Inverse of encode. Counts may be multi-digit.

    >>> decode("a3b2")
    'aaabb'
    """
    raise NotImplementedError
