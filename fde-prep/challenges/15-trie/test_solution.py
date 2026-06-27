from solution import Trie


def make_trie(words):
    t = Trie()
    for w in words:
        t.insert(w)
    return t


class TestBasic:
    def test_search_inserted(self):
        t = make_trie(["app", "apple"])
        assert t.search("app") is True
        assert t.search("apple") is True

    def test_prefix_is_not_a_word(self):
        t = make_trie(["apple"])
        assert t.search("app") is False

    def test_starts_with(self):
        t = make_trie(["apple"])
        assert t.starts_with("app") is True
        assert t.starts_with("apx") is False


class TestEdge:
    def test_search_missing(self):
        assert make_trie(["cat"]).search("dog") is False

    def test_empty_trie(self):
        t = Trie()
        assert t.search("x") is False
        assert t.starts_with("x") is False

    def test_word_that_is_prefix_of_another(self):
        t = make_trie(["app", "apple"])
        assert t.search("app") is True
        assert t.search("apple") is True
        assert t.search("appl") is False

    def test_starts_with_empty_prefix(self):
        t = make_trie(["a"])
        assert t.starts_with("") is True  # empty prefix matches the root

    def test_starts_with_empty_on_empty_trie(self):
        assert Trie().starts_with("") is True

    def test_overlapping_branches(self):
        t = make_trie(["car", "card", "care", "dog"])
        assert t.search("car") and t.search("care")
        assert t.starts_with("ca")
        assert not t.search("ca")


class TestStretch:
    def test_autocomplete_sorted(self):
        t = make_trie(["car", "card", "care", "cat", "dog"])
        assert t.autocomplete("car") == ["car", "card", "care"]

    def test_autocomplete_includes_prefix_word(self):
        t = make_trie(["app", "apple", "apply"])
        assert t.autocomplete("app") == ["app", "apple", "apply"]

    def test_autocomplete_all(self):
        t = make_trie(["b", "a", "c"])
        assert t.autocomplete("") == ["a", "b", "c"]

    def test_autocomplete_unknown_prefix(self):
        t = make_trie(["apple"])
        assert t.autocomplete("xyz") == []

    def test_autocomplete_single(self):
        t = make_trie(["apple", "banana"])
        assert t.autocomplete("ban") == ["banana"]
