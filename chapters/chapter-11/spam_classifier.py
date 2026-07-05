"""Week 4 Spam Classifier skeleton.

Complete the TODO sections in the NaiveBayesSpamClassifier class.
"""

from collections import Counter, defaultdict
import math
from text_preprocessing import load_spam_csv, preprocess_message


class NaiveBayesSpamClassifier:
    def __init__(self):
        self.class_counts = Counter()
        self.word_counts = defaultdict(Counter)
        self.total_words = Counter()
        self.vocabulary = set()
        self.total_messages = 0

    def fit(self, labels, messages):
        """Learn priors and word counts from labelled messages."""
        self.total_messages = len(messages)

        for label, message in zip(labels, messages):
            # TODO 1: count each class label
            # TODO 2: preprocess the message into tokens
            # TODO 3: update vocabulary, word_counts and total_words
            pass

    def class_prior(self, label):
        """Return P(class)."""
        # TODO: return class count divided by total messages
        raise NotImplementedError

    def word_likelihood(self, word, label):
        """Return P(word | class) using Laplace smoothing."""
        # TODO: use (word count + 1) / (total words in class + vocabulary size)
        raise NotImplementedError

    def predict_one(self, message):
        """Predict 'spam' or 'ham' for one message using log scores."""
        tokens = preprocess_message(message)
        scores = {}

        for label in self.class_counts:
            # TODO 1: start with log prior
            # TODO 2: add log likelihood for each token
            # TODO 3: store the score
            pass

        # TODO: return the label with the highest score
        raise NotImplementedError

    def predict(self, messages):
        return [self.predict_one(message) for message in messages]


def confusion_counts(true_labels, predicted_labels):
    counts = {"TP": 0, "TN": 0, "FP": 0, "FN": 0}
    for true, pred in zip(true_labels, predicted_labels):
        if true == "spam" and pred == "spam":
            counts["TP"] += 1
        elif true == "ham" and pred == "ham":
            counts["TN"] += 1
        elif true == "ham" and pred == "spam":
            counts["FP"] += 1
        elif true == "spam" and pred == "ham":
            counts["FN"] += 1
    return counts


def safe_divide(top, bottom):
    return top / bottom if bottom else 0


def calculate_metrics(counts):
    tp = counts["TP"]
    tn = counts["TN"]
    fp = counts["FP"]
    fn = counts["FN"]
    accuracy = safe_divide(tp + tn, tp + tn + fp + fn)
    precision = safe_divide(tp, tp + fp)
    recall = safe_divide(tp, tp + fn)
    f1 = safe_divide(2 * precision * recall, precision + recall)
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def print_report(counts, metrics):
    print("Confusion counts:", counts)
    for name, value in metrics.items():
        print(f"{name}: {value:.3f}")


if __name__ == "__main__":
    labels, messages = load_spam_csv("spam.csv")
    split = int(len(messages) * 0.7)
    train_labels = labels[:split]
    train_messages = messages[:split]
    check_labels = labels[split:]
    check_messages = messages[split:]

    classifier = NaiveBayesSpamClassifier()
    classifier.fit(train_labels, train_messages)
    predictions = classifier.predict(check_messages)
    counts = confusion_counts(check_labels, predictions)
    metrics = calculate_metrics(counts)
    print_report(counts, metrics)
