from collections import Counter
import string
def analyze_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text.split()
    word_counts = Counter(words)
    print("Word Frequency Analysis:")
    for word, count in word_counts.items():
        print(f"{word}: {count} times")
if __name__ == "__main__":
    example_text = "This is an example sentence. It contains some words, and some words are repeated."
    analyze_text(example_text)
