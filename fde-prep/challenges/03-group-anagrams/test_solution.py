from solution import group_anagrams, group_anagrams_normalized


class TestBasic:
    def test_classic(self):
        assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
            ["eat", "tea", "ate"], ["tan", "nat"], ["bat"],
        ]

    def test_two_groups(self):
        assert group_anagrams(["abc", "bca", "xy"]) == [["abc", "bca"], ["xy"]]


class TestEdge:
    def test_empty_list(self):
        assert group_anagrams([]) == []

    def test_single_word(self):
        assert group_anagrams(["solo"]) == [["solo"]]

    def test_duplicates_share_group(self):
        assert group_anagrams(["ab", "ab", "ba"]) == [["ab", "ab", "ba"]]

    def test_empty_string_word(self):
        assert group_anagrams(["", "a", ""]) == [["", ""], ["a"]]

    def test_case_sensitive_by_default(self):
        # "Tea" and "eat" do NOT group in the base version
        assert group_anagrams(["Tea", "eat"]) == [["Tea"], ["eat"]]


class TestStretch:
    def test_normalized_case_and_space(self):
        assert group_anagrams_normalized(["Listen", "silent", "Tin sel"]) == [
            ["Listen", "silent", "Tin sel"],
        ]

    def test_normalized_keeps_originals(self):
        result = group_anagrams_normalized(["Eat", "TEA", "bat"])
        assert result == [["Eat", "TEA"], ["bat"]]

    def test_normalized_preserves_group_order(self):
        assert group_anagrams_normalized(["dog", "God", "act", "Cat"]) == [
            ["dog", "God"], ["act", "Cat"],
        ]
