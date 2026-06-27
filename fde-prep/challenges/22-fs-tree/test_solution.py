import pytest

from solution import FileSystem


class TestBasic:
    def test_mkdir_and_ls(self):
        fs = FileSystem()
        fs.mkdir("/a")
        assert fs.ls("/") == ["a"]

    def test_add_file_and_du(self):
        fs = FileSystem()
        fs.add_file("/a/f.txt", 10)
        assert fs.du("/a") == 10
        assert fs.du("/") == 10

    def test_ls_sorted(self):
        fs = FileSystem()
        fs.mkdir("/b")
        fs.mkdir("/a")
        fs.add_file("/c.txt", 1)
        assert fs.ls("/") == ["a", "b", "c.txt"]


class TestEdge:
    def test_ls_missing_raises(self):
        with pytest.raises(KeyError):
            FileSystem().ls("/nope")

    def test_du_of_file(self):
        fs = FileSystem()
        fs.add_file("/f.txt", 7)
        assert fs.du("/f.txt") == 7

    def test_du_empty_dir(self):
        fs = FileSystem()
        fs.mkdir("/empty")
        assert fs.du("/empty") == 0

    def test_add_file_creates_intermediate_dirs(self):
        fs = FileSystem()
        fs.add_file("/x/y/z.txt", 5)
        assert fs.ls("/x") == ["y"]
        assert fs.du("/x") == 5

    def test_mkdir_nested(self):
        fs = FileSystem()
        fs.mkdir("/a/b/c")
        assert fs.ls("/a") == ["b"]
        assert fs.ls("/a/b") == ["c"]

    def test_overwrite_file_size(self):
        fs = FileSystem()
        fs.add_file("/f", 10)
        fs.add_file("/f", 3)
        assert fs.du("/f") == 3

    def test_find_basic(self):
        fs = FileSystem()
        fs.add_file("/a/f.txt", 1)
        fs.add_file("/b/f.txt", 1)
        fs.add_file("/b/g.txt", 1)
        assert fs.find("f.txt") == ["/a/f.txt", "/b/f.txt"]


class TestStretch:
    def test_du_recursive(self):
        fs = FileSystem()
        fs.add_file("/a/f.txt", 10)
        fs.add_file("/a/b/g.txt", 5)
        fs.add_file("/a/b/h.txt", 2)
        assert fs.du("/a") == 17
        assert fs.du("/a/b") == 7

    def test_mv_file_into_dir(self):
        fs = FileSystem()
        fs.mkdir("/dest")
        fs.add_file("/a/f.txt", 10)
        fs.mv("/a/f.txt", "/dest")
        assert fs.ls("/dest") == ["f.txt"]
        assert fs.ls("/a") == []
        assert fs.du("/dest") == 10

    def test_mv_rename(self):
        fs = FileSystem()
        fs.add_file("/a/f.txt", 4)
        fs.mv("/a/f.txt", "/a/g.txt")
        assert fs.ls("/a") == ["g.txt"]
        assert fs.du("/a/g.txt") == 4

    def test_mv_missing_source_raises(self):
        fs = FileSystem()
        fs.mkdir("/dest")
        with pytest.raises(KeyError):
            fs.mv("/ghost", "/dest")

    def test_mv_directory_with_contents(self):
        fs = FileSystem()
        fs.add_file("/a/sub/x.txt", 5)
        fs.add_file("/a/sub/y.txt", 3)
        fs.mkdir("/dest")
        fs.mv("/a/sub", "/dest")
        assert fs.du("/dest/sub") == 8
        assert sorted(fs.ls("/dest/sub")) == ["x.txt", "y.txt"]
        assert fs.ls("/a") == []

    def test_find_nested(self):
        fs = FileSystem()
        fs.add_file("/a/b/target", 1)
        fs.add_file("/a/target", 1)
        fs.mkdir("/c/target")
        assert fs.find("target") == ["/a/b/target", "/a/target", "/c/target"]
