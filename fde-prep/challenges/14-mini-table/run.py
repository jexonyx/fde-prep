"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import MiniTable

if __name__ == "__main__":
    t = MiniTable()
    t.insert({"name": "Ada", "city": "London", "age": 36})
    t.insert({"name": "Bo", "city": "London", "age": 28})
    t.insert({"name": "Cy", "city": "Paris", "age": 36})
    print("select(city='London'):", t.select(city="London"))
    print("select('name', city='London'):", t.select("name", city="London"))
    print("where(age >= 30):", t.where(lambda r: r["age"] >= 30))
