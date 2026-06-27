"""Reference — 19 versioned-store. Check AFTER attempting."""


class VersionedStore:
    def __init__(self):
        self._history = {}  # key -> list of values, index == version

    def set(self, key, value):
        self._history.setdefault(key, []).append(value)

    def get(self, key):
        if key not in self._history:
            raise KeyError(key)
        return self._history[key][-1]

    def get_at(self, key, version):
        if key not in self._history:
            raise KeyError(key)
        history = self._history[key]
        if version < 0 or version >= len(history):
            raise IndexError(version)
        return history[version]

    def revert(self, key, version):
        value = self.get_at(key, version)  # validates key + version
        self.set(key, value)               # append as a new version
        return value
