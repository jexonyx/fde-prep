"""22 — fs-tree. First pass in plain text (see ../../CONSTRAINTS.md)."""


class FileSystem:
    """An in-memory filesystem rooted at '/'."""

    def __init__(self):
        raise NotImplementedError

    def mkdir(self, path):
        """Create a directory (and missing parents). No-op if it exists; raise on file clash."""
        raise NotImplementedError

    def add_file(self, path, size):
        """Create/overwrite a file of `size` (creating missing parent dirs)."""
        raise NotImplementedError

    def ls(self, path):
        """Sorted child names for a directory; [name] for a file. KeyError if missing."""
        raise NotImplementedError

    def find(self, name):
        """All absolute paths whose final component == name, sorted."""
        raise NotImplementedError

    def du(self, path):
        """Total size of all files at or under path (recursive)."""
        raise NotImplementedError

    def mv(self, src, dst):
        """Follow-up. Move src into dst (if dst is a dir) or rename to dst. KeyError if src
        is missing."""
        raise NotImplementedError
