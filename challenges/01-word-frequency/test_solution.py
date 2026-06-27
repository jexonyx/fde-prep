from solution import word_frequency, top_n


class TestBasic:
    def test_simple_counts(self):
        assert word_frequency("a b a") == {"a": 2, "b": 1}

    def test_case_insensitive(self):
        assert word_frequency("The cat sat. The CAT ran!") == {
            "the": 2, "cat": 2, "sat": 1, "ran": 1,
        }

    def test_strips_trailing_punctuation(self):
        assert word_frequency("hello, hello.") == {"hello": 2}


class TestEdge:
    def test_empty_string(self):
        assert word_frequency("") == {}

    def test_only_whitespace(self):
        assert word_frequency("   \t\n ") == {}

    def test_only_punctuation_tokens_dropped(self):
        assert word_frequency("... !!! ?") == {}

    def test_repeated_punctuation(self):
        assert word_frequency("hello!!! world??") == {"hello": 1, "world": 1}

    def test_single_word(self):
        assert word_frequency("solo") == {"solo": 1}


class TestStretch:
    def test_top_n_basic(self):
        text = "a a a b b c"
        assert top_n(text, 2) == [("a", 3), ("b", 2)]

    def test_top_n_alphabetical_tie_break(self):
        # b and c both appear twice -> alphabetical order
        text = "c c b b a"
        assert top_n(text, 3) == [("b", 2), ("c", 2), ("a", 1)]

    def test_top_n_beyond_vocab_returns_all(self):
        assert top_n("x y", 10) == [("x", 1), ("y", 1)]

    def test_top_n_zero(self):
        assert top_n("x y z", 0) == []

    def test_top_n_empty_text(self):
        assert top_n("", 3) == []

    def test_apostrophes_kept_inside_word(self):
        # internal punctuation stays; only the EDGES are stripped
        assert word_frequency("don't don't stop.") == {"don't": 2, "stop": 1}
