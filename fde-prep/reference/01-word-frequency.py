"""Reference — 01 word-frequency. Check AFTER attempting."""
import string


def word_frequency(text):
    counts = {}
    for token in text.split():
        word = token.strip(string.punctuation).lower()
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_n(text, n):
    counts = word_frequency(text)
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ranked[:n]
