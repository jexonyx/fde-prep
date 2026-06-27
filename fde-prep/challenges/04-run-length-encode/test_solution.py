from solution import encode, decode


class TestBasic:
    def test_encode_runs(self):
        assert encode("aaabb") == "a3b2"

    def test_encode_no_repeats(self):
        assert encode("abc") == "a1b1c1"

    def test_decode_runs(self):
        assert decode("a3b2") == "aaabb"


class TestEdge:
    def test_encode_empty(self):
        assert encode("") == ""

    def test_decode_empty(self):
        assert decode("") == ""

    def test_encode_single_char(self):
        assert encode("a") == "a1"

    def test_decode_single(self):
        assert decode("a1") == "a"

    def test_case_sensitive(self):
        assert encode("aA") == "a1A1"

    def test_long_run_multi_digit(self):
        assert encode("a" * 12) == "a12"

    def test_decode_multi_digit(self):
        assert decode("a12") == "a" * 12


class TestStretch:
    def test_round_trip_letters(self):
        for x in ["", "a", "aaabb", "abcabc", "zzzzzzzzzz", "Mississippi"]:
            assert decode(encode(x)) == x

    def test_round_trip_long(self):
        x = "w" * 100 + "x" * 5 + "y"
        assert decode(encode(x)) == x

    def test_encode_then_decode_mixed_case(self):
        x = "aAaAbbBB"
        assert decode(encode(x)) == x
