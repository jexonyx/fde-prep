from solution import tokenize, tokenize_identifiers


class TestBasic:
    def test_mixed(self):
        assert tokenize("ab12, c!") == [
            ("WORD", "ab"), ("NUMBER", 12), ("PUNCT", ","),
            ("WORD", "c"), ("PUNCT", "!"),
        ]

    def test_just_number(self):
        assert tokenize("100") == [("NUMBER", 100)]

    def test_just_word(self):
        assert tokenize("hello") == [("WORD", "hello")]


class TestEdge:
    def test_empty(self):
        assert tokenize("") == []

    def test_whitespace_only(self):
        assert tokenize("   \t ") == []

    def test_leading_zeros(self):
        assert tokenize("007") == [("NUMBER", 7)]

    def test_trailing_punct(self):
        assert tokenize("a.") == [("WORD", "a"), ("PUNCT", ".")]

    def test_runs_of_punct_split(self):
        assert tokenize("a!!") == [("WORD", "a"), ("PUNCT", "!"), ("PUNCT", "!")]

    def test_whitespace_separates(self):
        assert tokenize("a b") == [("WORD", "a"), ("WORD", "b")]


class TestStretch:
    def test_identifiers_keep_trailing_digits(self):
        assert tokenize_identifiers("x1") == [("WORD", "x1")]

    def test_identifiers_number_then_word(self):
        assert tokenize_identifiers("12x") == [("NUMBER", 12), ("WORD", "x")]

    def test_identifiers_full_expression(self):
        assert tokenize_identifiers("var2 = 7 + ab3") == [
            ("WORD", "var2"), ("PUNCT", "="), ("NUMBER", 7),
            ("PUNCT", "+"), ("WORD", "ab3"),
        ]

    def test_base_tokenize_splits_alnum(self):
        # base version still splits "x1" into WORD + NUMBER
        assert tokenize("x1") == [("WORD", "x"), ("NUMBER", 1)]

    def test_dense_mixed_no_spaces(self):
        assert tokenize("a1b2") == [
            ("WORD", "a"), ("NUMBER", 1), ("WORD", "b"), ("NUMBER", 2),
        ]
