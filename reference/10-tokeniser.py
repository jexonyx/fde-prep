"""Reference — 10 tokeniser. Check AFTER attempting."""


def _scan(s, word_continues):
    """Shared scanner. word_continues(ch) decides whether ch extends a WORD run."""
    tokens = []
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        if ch.isspace():
            i += 1
        elif ch.isdigit():
            start = i
            while i < n and s[i].isdigit():
                i += 1
            tokens.append(("NUMBER", int(s[start:i])))
        elif ch.isalpha():
            start = i
            i += 1
            while i < n and word_continues(s[i]):
                i += 1
            tokens.append(("WORD", s[start:i]))
        else:
            tokens.append(("PUNCT", ch))
            i += 1
    return tokens


def tokenize(s):
    return _scan(s, lambda ch: ch.isalpha())


def tokenize_identifiers(s):
    return _scan(s, lambda ch: ch.isalnum())
