"""Reference — 07 min-stack. Check AFTER attempting."""


class MinStack:
    def __init__(self):
        self._stack = []
        self._mins = []  # _mins[i] = min of _stack[0..i]

    def push(self, x):
        self._stack.append(x)
        current_min = x if not self._mins else min(x, self._mins[-1])
        self._mins.append(current_min)

    def pop(self):
        if not self._stack:
            raise IndexError("pop from empty MinStack")
        self._mins.pop()
        return self._stack.pop()

    def top(self):
        if not self._stack:
            raise IndexError("top from empty MinStack")
        return self._stack[-1]

    def get_min(self):
        if not self._stack:
            raise IndexError("get_min from empty MinStack")
        return self._mins[-1]

    def __len__(self):
        return len(self._stack)
