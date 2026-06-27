"""Reference — 14 mini-table. Check AFTER attempting."""


class MiniTable:
    def __init__(self):
        self._rows = []

    def insert(self, row):
        self._rows.append(dict(row))  # defensive copy

    def select(self, *columns, **filters):
        matches = [
            row for row in self._rows
            if all(row.get(col) == val for col, val in filters.items())
        ]
        if not columns:
            return [dict(row) for row in matches]
        return [{col: row.get(col) for col in columns} for row in matches]

    def where(self, predicate):
        return [dict(row) for row in self._rows if predicate(row)]
