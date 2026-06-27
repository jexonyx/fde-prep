"""Reference — 16 mini-sheet. Check AFTER attempting."""


class CycleError(Exception):
    """Raised when resolving a cell revisits a cell on the current resolution path."""


class MiniSheet:
    def __init__(self):
        self._cells = {}

    def set(self, cell, value):
        self._cells[cell] = value

    def get(self, cell):
        return self._resolve(cell, set())

    def _resolve(self, cell, path):
        if cell not in self._cells:
            raise KeyError(cell)
        if cell in path:
            raise CycleError(f"reference cycle through {cell}")
        value = self._cells[cell]
        if isinstance(value, str) and value.startswith("="):
            target = value[1:]
            return self._resolve(target, path | {cell})
        return value
