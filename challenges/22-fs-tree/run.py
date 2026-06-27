"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import FileSystem

if __name__ == "__main__":
    fs = FileSystem()
    fs.mkdir("/a")
    fs.add_file("/a/f.txt", 10)
    fs.add_file("/a/b/g.txt", 5)
    print("ls('/a'):", fs.ls("/a"))
    print("du('/a'):", fs.du("/a"))
    print("find('g.txt'):", fs.find("g.txt"))
    fs.mkdir("/dest")
    fs.mv("/a/b", "/dest")
    print("after mv('/a/b','/dest') -> du('/dest'):", fs.du("/dest"))
