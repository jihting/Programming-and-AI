"""Week 5 Lab 4: final ML comparison exercise starter.

Compare one classical classifier with one neural-network-style classifier on the same dataset.
"""

try:
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris, load_wine, load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay
except ModuleNotFoundError as exc:
    print("Missing package:", exc.name)
    print("Use the prepared lab environment or ask your tutor which Python environment to open.")
    raise SystemExit(1)


DATASETS = {
    "iris": load_iris,
    "wine": load_wine,
    "breast_cancer": load_breast_cancer,
}

# Choose: "iris", "wine" or "breast_cancer"
DATASET_NAME = "iris"


def load_dataset(name):
    if name not in DATASETS:
        raise ValueError(f"Unknown dataset: {name}")
    data = DATASETS[name]()
    return data.data, data.target, data.target_names


def evaluate_model(name, model, X_train, X_holdout, y_train, y_holdout, target_names):
    model.fit(X_train, y_train)
    predictions = model.predict(X_holdout)

    average = "binary" if len(target_names) == 2 else "macro"
    accuracy = accuracy_score(y_holdout, predictions)
    precision = precision_score(y_holdout, predictions, average=average, zero_division=0)
    recall = recall_score(y_holdout, predictions, average=average, zero_division=0)
    matrix = confusion_matrix(y_holdout, predictions)

    print("=", name)
    print("Accuracy:", round(accuracy, 3))
    print("Precision:", round(precision, 3))
    print("Recall:", round(recall, 3))
    print("Confusion matrix:")
    print(matrix)
    print()

    display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=target_names)
    display.plot(cmap="Blues", xticks_rotation=45)
    plt.title(name)
    filename = name.lower().replace(" ", "_").replace("-", "_") + "_confusion_matrix.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print("Saved", filename)

    return {
        "model": name,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "confusion_matrix": matrix,
    }


def main():
    X, y, target_names = load_dataset(DATASET_NAME)
    print("Dataset:", DATASET_NAME)
    print("Examples:", X.shape[0])
    print("Features:", X.shape[1])
    print("Classes:", list(target_names))
    print()

    X_train, X_holdout, y_train, y_holdout = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    classical_model = DecisionTreeClassifier(max_depth=4, random_state=42)
    neural_style_model = make_pipeline(
        StandardScaler(),
        MLPClassifier(hidden_layer_sizes=(16,), max_iter=1200, random_state=42),
    )

    results = []
    results.append(evaluate_model("Classical decision tree", classical_model, X_train, X_holdout, y_train, y_holdout, target_names))
    results.append(evaluate_model("Neural style MLP", neural_style_model, X_train, X_holdout, y_train, y_holdout, target_names))

    print("Results table")
    print("model,accuracy,precision,recall")
    for row in results:
        print(f"{row['model']},{row['accuracy']:.3f},{row['precision']:.3f},{row['recall']:.3f}")

    print()
    print("Use these results in ml_comparison_writeup.md")


if __name__ == "__main__":
    main()
