"""16 — mini-sheet. First pass in plain text (see ../../CONSTRAINTS.md)."""


class CycleError(Exception):
    """Raised when resolving a cell revisits a cell on the current resolution path."""


class MiniSheet:
    """Named cells holding literals or '=CELL' references."""

    def __init__(self):
        raise NotImplementedError

    def set(self, cell, value):
        raise NotImplementedError

    def get(self, cell):
        """Resolve the cell's value. Literals return directly; '=X' references resolve X.
        KeyError if a needed cell is unset; CycleError on a reference cycle (follow-ups)."""
        raise NotImplementedError
