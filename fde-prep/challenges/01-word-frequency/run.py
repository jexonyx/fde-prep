"""Smoke runner — `python run.py`. Prints a couple of examples so you can eyeball behaviour.
Run the real gate with: pytest test_solution.py"""
from solution import word_frequency, top_n

if __name__ == "__main__":
    text = "The cat sat. The CAT ran! The dog ran."
    print("text:", text)
    print("word_frequency:", word_frequency(text))
    print("top_n(2):", top_n(text, 2))
