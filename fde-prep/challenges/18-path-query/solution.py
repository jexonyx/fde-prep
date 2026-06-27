"""18 — path-query. First pass in plain text (see ../../CONSTRAINTS.md)."""

_MISSING = object()


def get_path(data, path, default=_MISSING):
    """Return the value at the dotted path. Numeric segments index lists; others key dicts.
    Missing/out-of-range/descend-into-scalar -> KeyError, or default if supplied.

    >>> get_path({"a": {"b": [{"c": 42}]}}, "a.b.0.c")
    42
    """
    raise NotImplementedError


def set_path(data, path, value):
    """Follow-up. Set value at path, creating intermediate dicts as needed; return data."""
    raise NotImplementedError
