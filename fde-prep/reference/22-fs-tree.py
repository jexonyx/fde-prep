"""Reference — 22 fs-tree. Check AFTER attempting."""


class _Dir:
    def __init__(self):
        self.children = {}  # name -> _Dir | _File


class _File:
    def __init__(self, size):
        self.size = size


class FileSystem:
    def __init__(self):
        self._root = _Dir()

    @staticmethod
    def _split(path):
        return [part for part in path.split("/") if part]

    def _resolve(self, parts):
        """Return the node at parts, or raise KeyError if any step is missing."""
        node = self._root
        for part in parts:
            if not isinstance(node, _Dir) or part not in node.children:
                raise KeyError("/" + "/".join(parts))
            node = node.children[part]
        return node

    def mkdir(self, path):
        node = self._root
        for part in self._split(path):
            child = node.children.get(part)
            if child is None:
                child = _Dir()
                node.children[part] = child
            elif not isinstance(child, _Dir):
                raise NotADirectoryError(part)
            node = child

    def add_file(self, path, size):
        parts = self._split(path)
        if not parts:
            raise ValueError("a file needs a name")
        *dirs, name = parts
        node = self._root
        for part in dirs:
            child = node.children.get(part)
            if child is None:
                child = _Dir()
                node.children[part] = child
            elif not isinstance(child, _Dir):
                raise NotADirectoryError(part)
            node = child
        if isinstance(node.children.get(name), _Dir):
            raise IsADirectoryError(name)
        node.children[name] = _File(size)

    def ls(self, path):
        parts = self._split(path)
        node = self._resolve(parts)
        if isinstance(node, _File):
            return [parts[-1]]
        return sorted(node.children)

    def du(self, path):
        return self._size(self._resolve(self._split(path)))

    def _size(self, node):
        if isinstance(node, _File):
            return node.size
        return sum(self._size(child) for child in node.children.values())

    def find(self, name):
        results = []

        def walk(node, prefix):
            for child_name, child in node.children.items():
                child_path = prefix + "/" + child_name
                if child_name == name:
                    results.append(child_path)
                if isinstance(child, _Dir):
                    walk(child, child_path)

        walk(self._root, "")
        return sorted(results)

    def mv(self, src, dst):
        src_parts = self._split(src)
        if not src_parts:
            raise ValueError("cannot move the root")
        node = self._resolve(src_parts)            # KeyError if src missing
        parent = self._resolve(src_parts[:-1])
        name = src_parts[-1]

        dst_parts = self._split(dst)
        try:
            dst_node = self._resolve(dst_parts)
        except KeyError:
            dst_node = None

        if isinstance(dst_node, _Dir):
            target_parent, target_name = dst_node, name
        else:
            target_parent = self._resolve(dst_parts[:-1])  # parent must exist
            target_name = dst_parts[-1]

        del parent.children[name]
        target_parent.children[target_name] = node
