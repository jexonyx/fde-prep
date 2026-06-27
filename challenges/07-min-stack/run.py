"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import MinStack

if __name__ == "__main__":
    s = MinStack()
    for x in [3, 1, 2, 1]:
        s.push(x)
        print(f"push {x} -> top={s.top()} min={s.get_min()}")
    while True:
        try:
            popped = s.pop()
        except IndexError:
            print("stack empty")
            break
        print(f"pop -> {popped}")
