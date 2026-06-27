from solution import merge, merge_k


class TestBasic:
    def test_interleaved(self):
        assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_back_to_back(self):
        assert merge([1, 2], [3, 4]) == [1, 2, 3, 4]

    def test_reversed_order_inputs(self):
        assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]


class TestEdge:
    def test_one_empty(self):
        assert merge([], [2, 4]) == [2, 4]
        assert merge([1, 3], []) == [1, 3]

    def test_both_empty(self):
        assert merge([], []) == []

    def test_duplicates(self):
        assert merge([1, 1, 2], [1, 3]) == [1, 1, 1, 2, 3]

    def test_unequal_lengths(self):
        assert merge([1], [2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    def test_negatives(self):
        assert merge([-3, -1, 0], [-2, 5]) == [-3, -2, -1, 0, 5]

    def test_inputs_not_mutated(self):
        a, b = [1, 3], [2, 4]
        merge(a, b)
        assert a == [1, 3] and b == [2, 4]


class TestStretch:
    def test_merge_k_basic(self):
        assert merge_k([[1, 4], [2], [0, 3, 5]]) == [0, 1, 2, 3, 4, 5]

    def test_merge_k_empty_input(self):
        assert merge_k([]) == []

    def test_merge_k_with_empty_lists(self):
        assert merge_k([[], [1, 2], [], [0]]) == [0, 1, 2]

    def test_merge_k_single_list(self):
        assert merge_k([[3, 1, 2]]) == [3, 1, 2]  # already-"sorted" input returned as-is

    def test_merge_k_duplicates(self):
        assert merge_k([[1, 1], [1], [1, 1]]) == [1, 1, 1, 1, 1]

    def test_merge_large(self):
        a = list(range(0, 1000, 2))
        b = list(range(1, 1000, 2))
        assert merge(a, b) == list(range(1000))
