"""Reference — 15 trie. Check AFTER attempting."""

_END = object()  # sentinel marker for "a word ends here" — can't collide with a character


class Trie:
    def __init__(self):
        self._root = {}

    def insert(self, word):
        node = self._root
        for ch in word:
            node = node.setdefault(ch, {})
        node[_END] = True

    def _find(self, s):
        """Return the node reached by walking s, or None if the path breaks."""
        node = self._root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word):
        node = self._find(word)
        return node is not None and _END in node

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def autocomplete(self, prefix):
        node = self._find(prefix)
        if node is None:
            return []
        results = []

        def dfs(current, suffix):
            if _END in current:
                results.append(prefix + suffix)
            for ch in sorted(k for k in current if k is not _END):
                dfs(current[ch], suffix + ch)

        dfs(node, "")
        return results
