"""Reference — 17 calc. Check AFTER attempting."""


def _tokenize(expr):
    tokens = []
    i, n = 0, len(expr)
    while i < n:
        ch = expr[i]
        if ch.isspace():
            i += 1
        elif ch.isdigit():
            start = i
            while i < n and expr[i].isdigit():
                i += 1
            tokens.append(int(expr[start:i]))
        elif ch in "+-*/()":
            tokens.append(ch)
            i += 1
        else:
            raise ValueError(f"unexpected character {ch!r}")
    return tokens


class _Parser:
    """Recursive descent: grammar levels encode precedence; while-loops give left-assoc."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def _peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def _advance(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def expression(self):
        value = self.term()
        while self._peek() in ("+", "-"):
            op = self._advance()
            rhs = self.term()
            value = value + rhs if op == "+" else value - rhs
        return value

    def term(self):
        value = self.factor()
        while self._peek() in ("*", "/"):
            op = self._advance()
            rhs = self.factor()
            value = value * rhs if op == "*" else value / rhs
        return value

    def factor(self):
        tok = self._peek()
        if tok == "(":
            self._advance()
            value = self.expression()
            if self._peek() != ")":
                raise ValueError("missing closing parenthesis")
            self._advance()
            return value
        if isinstance(tok, int):
            return self._advance()
        raise ValueError(f"unexpected token {tok!r}")


def calc(expr):
    parser = _Parser(_tokenize(expr))
    result = parser.expression()
    if parser.pos != len(parser.tokens):
        raise ValueError("unexpected trailing tokens")
    return result
