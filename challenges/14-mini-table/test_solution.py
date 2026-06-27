from solution import MiniTable


def make_table():
    t = MiniTable()
    t.insert({"name": "Ada", "city": "London", "age": 36})
    t.insert({"name": "Bo", "city": "London", "age": 28})
    t.insert({"name": "Cy", "city": "Paris", "age": 36})
    return t


class TestBasic:
    def test_select_all(self):
        assert len(make_table().select()) == 3

    def test_select_one_filter(self):
        rows = make_table().select(city="London")
        assert [r["name"] for r in rows] == ["Ada", "Bo"]

    def test_select_two_filters(self):
        rows = make_table().select(city="London", age=36)
        assert [r["name"] for r in rows] == ["Ada"]


class TestEdge:
    def test_empty_table(self):
        assert MiniTable().select() == []

    def test_no_match(self):
        assert make_table().select(city="Tokyo") == []

    def test_filter_on_missing_column(self):
        t = MiniTable()
        t.insert({"name": "Ada"})
        assert t.select(age=36) == []   # row lacks "age" -> no match

    def test_insert_is_copied(self):
        t = MiniTable()
        row = {"name": "Ada"}
        t.insert(row)
        row["name"] = "MUTATED"
        assert t.select()[0]["name"] == "Ada"

    def test_results_preserve_order(self):
        rows = make_table().select(age=36)
        assert [r["name"] for r in rows] == ["Ada", "Cy"]


class TestStretch:
    def test_where_predicate(self):
        rows = make_table().where(lambda r: r["age"] >= 30)
        assert sorted(r["name"] for r in rows) == ["Ada", "Cy"]

    def test_where_empty_result(self):
        assert make_table().where(lambda r: r["age"] > 100) == []

    def test_projection(self):
        rows = make_table().select("name", city="London")
        assert rows == [{"name": "Ada"}, {"name": "Bo"}]

    def test_projection_with_multiple_columns(self):
        rows = make_table().select("name", "age", city="Paris")
        assert rows == [{"name": "Cy", "age": 36}]

    def test_projection_missing_column_is_none(self):
        t = MiniTable()
        t.insert({"name": "Ada"})
        assert t.select("name", "age") == [{"name": "Ada", "age": None}]

    def test_select_returns_copies(self):
        t = make_table()
        rows = t.select(city="Paris")
        rows[0]["name"] = "X"
        assert t.select(city="Paris")[0]["name"] == "Cy"
