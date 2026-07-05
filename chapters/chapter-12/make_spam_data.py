"""Generate spam_data.npz for Week 4 Lab 4 if a tutor wants the binary fallback file.

Run from this folder after installing NumPy:

    python make_spam_data_npz.py
"""

from collections import Counter
import numpy as np
from text_preprocessing import load_spam_csv, build_vocabulary, build_matrix

labels, messages = load_spam_csv("spam.csv")
vocabulary = build_vocabulary(messages, max_words=30)
matrix = build_matrix(messages, vocabulary)

np.savez(
    "spam_data.npz",
    labels=np.array(labels),
    vocabulary=np.array(vocabulary),
    matrix=np.array(matrix),
)

print("Saved spam_data.npz")
print("Messages:", len(labels))
print("Vocabulary size:", len(vocabulary))
