"""Reference — 04 run-length-encode. Check AFTER attempting."""


def encode(s):
    if not s:
        return ""
    parts = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            parts.append(f"{prev}{count}")
            prev = ch
            count = 1
    parts.append(f"{prev}{count}")
    return "".join(parts)


def decode(s):
    result = []
    i, n = 0, len(s)
    while i < n:
        ch = s[i]
        i += 1
        start = i
        while i < n and s[i].isdigit():
            i += 1
        count = int(s[start:i])
        result.append(ch * count)
    return "".join(result)
