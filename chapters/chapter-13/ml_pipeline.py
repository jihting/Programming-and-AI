"""Week 5 Lab 1: scikit-learn pipeline starter.

Work through the TODO comments in the Week 5 Lab Workbook.
This file uses a local iris.csv file so that you can see the data directly.
"""

from pathlib import Path

try:
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import confusion_matrix
except ModuleNotFoundError as exc:
    print("Missing package:", exc.name)
    print("Use the prepared lab environment or ask your tutor which Python environment to open.")
    raise SystemExit(1)


# STEP 1: Load and inspect the data
DATA_FILE = Path(__file__).with_name("iris.csv")
df = pd.read_csv(DATA_FILE)

print("First five rows:")
print(df.head())
print()
print("Rows and columns:", df.shape)
print("Species:", sorted(df["species"].unique()))
print()

# STEP 2: Separate features from label
feature_columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
X = df[feature_columns]
y = df["species"]

# STEP 3: Train/holdout split
X_train, X_holdout, y_train, y_holdout = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("Training examples:", len(X_train))
print("Holdout examples:", len(X_holdout))
print()

# STEP 4: Your first model: k-nearest neighbours
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
knn_predictions = knn.predict(X_holdout)
knn_accuracy = knn.score(X_holdout, y_holdout)

print("k-NN holdout accuracy:", round(knn_accuracy, 3))
print("k-NN confusion matrix:")
print(confusion_matrix(y_holdout, knn_predictions, labels=sorted(y.unique())))
print()

# STEP 5: Prediction on new data
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = knn.predict(new_flower)
print("Prediction for new_flower:", prediction[0])
print()

# STEP 6: Try a second model
# TODO 1: create a DecisionTreeClassifier with random_state=42
# TODO 2: train it using .fit(X_train, y_train)
# TODO 3: make predictions on X_holdout
# TODO 4: print its score using .score(X_holdout, y_holdout)

# Example structure:
# tree = DecisionTreeClassifier(random_state=42)
# tree.fit(...)
# tree_predictions = tree.predict(...)
# print("Decision tree holdout accuracy:", ...)
