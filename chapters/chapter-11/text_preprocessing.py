"""Week 4 text preprocessing pipeline for the spam-filter labs.

The functions are complete. Students use and inspect them before building the classifier.
"""

import re
from collections import Counter

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "for", "from", "has", "have",
    "i", "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "you",
    "your", "we", "with"
}


def load_spam_csv(path):
    labels = []
    messages = []
    with open(path, encoding="utf-8") as file:
        next(file)  # header
        for line in file:
            label, message = line.rstrip("\n").split(",", 1)
            labels.append(label)
            messages.append(message)
    return labels, messages


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9£$ ]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenise(text):
    return clean_text(text).split()


def remove_stopwords(tokens):
    return [token for token in tokens if token not in STOPWORDS]


def preprocess_message(text):
    return remove_stopwords(tokenise(text))


def build_vocabulary(messages, max_words=50):
    counter = Counter()
    for message in messages:
        counter.update(preprocess_message(message))
    most_common = counter.most_common(max_words)
    return [word for word, count in most_common]


def text_to_vector(text, vocabulary):
    tokens = preprocess_message(text)
    counts = Counter(tokens)
    return [counts[word] for word in vocabulary]


def build_matrix(messages, vocabulary):
    return [text_to_vector(message, vocabulary) for message in messages]


if __name__ == "__main__":
    labels, messages = load_spam_csv("spam.csv")
    vocabulary = build_vocabulary(messages, max_words=20)
    matrix = build_matrix(messages, vocabulary)
    print("Messages:", len(messages))
    print("Vocabulary size:", len(vocabulary))
    print("First 10 vocabulary words:", vocabulary[:10])
    print("First vector:", matrix[0])
