"""Week 5 Lab 2: model comparison starter.

This script compares several classifiers using a holdout split and cross-validation.
"""

try:
    import numpy as np
    from sklearn.datasets import load_wine, load_breast_cancer
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import confusion_matrix, classification_report
except ModuleNotFoundError as exc:
    print("Missing package:", exc.name)
    print("Use the prepared lab environment or ask your tutor which Python environment to open.")
    raise SystemExit(1)


# STEP 1: Choose a dataset
# Change DATASET_NAME to "breast_cancer" for the challenge task.
DATASET_NAME = "wine"

if DATASET_NAME == "wine":
    data = load_wine()
elif DATASET_NAME == "breast_cancer":
    data = load_breast_cancer()
else:
    raise ValueError("Unknown dataset")

X = data.data
y = data.target

print("Dataset:", DATASET_NAME)
print("Examples:", X.shape[0])
print("Features:", X.shape[1])
print("Classes:", list(data.target_names))
print()

# STEP 2: Split data
X_train, X_holdout, y_train, y_holdout = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# STEP 3: Define models
models = {
    "k-NN": KNeighborsClassifier(n_neighbors=5),
    "Decision tree": DecisionTreeClassifier(random_state=42),
    "Logistic regression": LogisticRegression(max_iter=2000),
}

# STEP 4: Train, score and cross-validate
for name, model in models.items():
    print("=", name)
    model.fit(X_train, y_train)
    train_score = model.score(X_train, y_train)
    holdout_score = model.score(X_holdout, y_holdout)
    cv_scores = cross_val_score(model, X, y, cv=5)

    print("Training score:", round(train_score, 3))
    print("Holdout score:", round(holdout_score, 3))
    print("Cross-validation scores:", np.round(cv_scores, 3))
    print("CV mean:", round(cv_scores.mean(), 3))
    print("CV standard deviation:", round(cv_scores.std(), 3))

    predictions = model.predict(X_holdout)
    print("Confusion matrix:")
    print(confusion_matrix(y_holdout, predictions))
    print("Classification report:")
    print(classification_report(y_holdout, predictions, target_names=data.target_names, zero_division=0))
    print()

# TODO: Add your written interpretation in model_comparison_results.md.
