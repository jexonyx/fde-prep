"""Smoke runner — `python run.py`. Real gate: pytest test_solution.py"""
from solution import RateLimiter


class Clock:
    def __init__(self): self.t = 0
    def __call__(self): return self.t
    def advance(self, d): self.t += d


if __name__ == "__main__":
    clock = Clock()
    rl = RateLimiter(limit=2, window=10, clock=clock)
    for i in range(3):
        print(f"t={clock.t} allow('u'):", rl.allow("u"))
    clock.advance(10)
    print(f"t={clock.t} allow('u'):", rl.allow("u"))
