from solution import two_sum, all_pairs


class TestBasic:
    def test_simple(self):
        assert two_sum([2, 7, 11, 15], 9) == (0, 1)

    def test_later_pair(self):
        assert two_sum([3, 2, 4], 6) == (1, 2)

    def test_no_solution(self):
        assert two_sum([1, 2, 3], 99) is None


class TestEdge:
    def test_empty(self):
        assert two_sum([], 5) is None

    def test_single_element(self):
        assert two_sum([5], 5) is None

    def test_duplicates(self):
        assert two_sum([3, 3], 6) == (0, 1)

    def test_negatives(self):
        assert two_sum([-1, -2, -3, -4], -6) == (1, 3)

    def test_smallest_second_index_wins(self):
        # 1+3 (=>(0,2)) completes before 2+2 (=>(1,3)) as we scan
        assert two_sum([1, 2, 3, 2], 4) == (0, 2)


class TestStretch:
    def test_all_pairs_basic(self):
        assert all_pairs([1, 2, 3, 2, 4], 5) == [(1, 4), (2, 3)]

    def test_all_pairs_no_duplicates(self):
        assert all_pairs([1, 1, 1, 4, 4], 5) == [(1, 4)]

    def test_all_pairs_value_with_itself(self):
        assert all_pairs([3, 3], 6) == [(3, 3)]

    def test_all_pairs_needs_two_copies(self):
        # single 3 cannot pair with itself
        assert all_pairs([3, 1, 2], 6) == []

    def test_all_pairs_no_solution(self):
        assert all_pairs([1, 2, 3], 100) == []

    def test_all_pairs_with_zero_and_negatives(self):
        assert all_pairs([0, 0, -1, 1, 2, -2], 0) == [(-2, 2), (-1, 1), (0, 0)]
