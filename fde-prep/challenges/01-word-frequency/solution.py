"""01 — word-frequency. Write your first pass in plain text (see ../../CONSTRAINTS.md)."""


def word_frequency(text):
    """Return a dict mapping each word to its occurrence count.

    Case-insensitive; strips leading/trailing punctuation from each whitespace-separated
    token; ignores tokens that are empty after stripping.

    >>> word_frequency("The cat sat. The CAT ran!")
    {'the': 2, 'cat': 2, 'sat': 1, 'ran': 1}
    """
    raise NotImplementedError


def top_n(text, n):
    """Follow-up. Return the n most frequent words as (word, count) tuples, sorted by count
    descending with ties broken alphabetically. n beyond the vocabulary returns all of it."""
    raise NotImplementedError
