# 22 — fs-tree

**Tier 3 · ~45 min.** The capstone: a class tree with recursion across several methods.

## Concepts drilled
Modelling a tree with node objects (directories vs files), walking absolute paths, **recursive
aggregation** (`du`), a recursive search (`find`), and re-parenting a subtree (`mv`).

## Problem statement
Build a `FileSystem` rooted at `/`:
- `mkdir(path)` — create a directory, creating any missing intermediate directories. Creating
  an existing directory is a no-op; colliding with an existing file raises.
- `add_file(path, size)` — create (or overwrite) a file of the given size, creating missing
  intermediate directories. Colliding with an existing directory raises.
- `ls(path)` — for a directory, the **sorted** list of child names; for a file, a list with
  just that file's name. Missing path raises `KeyError`.
- `find(name)` — every absolute path whose final component equals `name` (files or dirs),
  **sorted**.
- `du(path)` — total size of all files at or under `path` (recursive). For a file, its own
  size.

## Worked example
```
fs = FileSystem()
fs.mkdir("/a")
fs.add_file("/a/f.txt", 10)
fs.add_file("/a/b/g.txt", 5)     # creates /a/b on the way
fs.ls("/a")          # -> ["b", "f.txt"]
fs.du("/a")          # -> 15
fs.find("g.txt")     # -> ["/a/b/g.txt"]
```

## Constraints / assumptions
- Paths are absolute, `/`-separated; `/` is the root. Sizes are non-negative ints.
- Names are unique within a directory; a name is either a file or a directory, not both.

## Follow-up extensions  → `TestStretch`
1. `mv(src, dst)` — move the node at `src`. If `dst` is an existing directory, move `src`
   **into** it keeping its name; otherwise `dst` is the new path (a rename), and its parent
   directory must already exist. Moving a missing `src` raises `KeyError`. Moving a directory
   carries its whole subtree (so `du` is preserved).

## Edge cases to consider
- `ls`/`du` on a missing path.
- `du` of an empty directory (0) and of a single file (its size).
- `mv` of a directory with contents; `mv` of a missing source.

## Complexity target
`mkdir`/`add_file`/`ls`/`du`/`mv` are O(depth) to walk, plus O(subtree) for the recursive
`du`/`find`. `ls` adds the sort of one directory's children.

## Narration prompts
- "Two node kinds: a directory holds a dict of children; a file holds a size. The root is a
  directory."
- "`du` is a textbook recursion: a file returns its size, a directory returns the sum over its
  children."
- For `mv`, talk through the two cases (into-a-dir vs rename) and how you detach from the old
  parent and attach to the new one.
