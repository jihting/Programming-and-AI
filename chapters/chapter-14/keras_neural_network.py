"""Week 5 Lab 3: neural network and decision-boundary starter.

This script uses TensorFlow/Keras if available. If TensorFlow is not installed,
it prints a clear fallback message and uses scikit-learn's MLPClassifier instead.
"""

try:
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
except ModuleNotFoundError as exc:
    print("Missing package:", exc.name)
    print("Use the prepared lab environment or ask your tutor which Python environment to open.")
    raise SystemExit(1)


def load_two_feature_iris():
    iris = load_iris()
    # Use petal length and petal width so the decision boundary can be plotted in 2D.
    X = iris.data[:, [2, 3]]
    y = iris.target
    return X, y, iris.target_names


def plot_boundary(model, X, y, filename, title):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 200),
        np.linspace(y_min, y_max, 200),
    )
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(grid)
    if getattr(Z, "ndim", 1) > 1:
        Z = np.argmax(Z, axis=1)
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(7, 5))
    plt.contourf(xx, yy, Z, alpha=0.25)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k")
    plt.xlabel("petal length")
    plt.ylabel("petal width")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(filename)
    print("Saved", filename)


def run_keras_version(X_train, X_holdout, y_train, y_holdout, X_scaled, y):
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    from tensorflow.keras.utils import to_categorical

    y_train_cat = to_categorical(y_train, num_classes=3)
    y_holdout_cat = to_categorical(y_holdout, num_classes=3)

    model = Sequential([
        Dense(8, activation="relu", input_shape=(2,)),
        Dense(8, activation="relu"),
        Dense(3, activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )

    history = model.fit(
        X_train,
        y_train_cat,
        epochs=60,
        validation_split=0.2,
        verbose=0,
    )

    loss, accuracy = model.evaluate(X_holdout, y_holdout_cat, verbose=0)
    print("Keras neural network holdout accuracy:", round(accuracy, 3))

    plt.figure(figsize=(7, 5))
    plt.plot(history.history["accuracy"], label="training accuracy")
    plt.plot(history.history["val_accuracy"], label="validation accuracy")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.legend()
    plt.tight_layout()
    plt.savefig("nn_training_curves.png")
    print("Saved nn_training_curves.png")

    plot_boundary(model, X_scaled, y, "nn_decision_boundary.png", "Neural network decision boundary")
    return accuracy


def run_fallback_version(X_train, X_holdout, y_train, y_holdout, X_scaled, y):
    print("TensorFlow/Keras is not available in this environment.")
    print("Fallback: using sklearn.neural_network.MLPClassifier so you can still observe the idea.")
    from sklearn.neural_network import MLPClassifier

    model = MLPClassifier(hidden_layer_sizes=(8, 8), max_iter=1200, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_holdout)
    accuracy = accuracy_score(y_holdout, predictions)
    print("MLPClassifier holdout accuracy:", round(accuracy, 3))
    plot_boundary(model, X_scaled, y, "nn_decision_boundary.png", "MLPClassifier decision boundary")
    return accuracy


def main():
    X, y, target_names = load_two_feature_iris()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_holdout, y_train, y_holdout = train_test_split(
        X_scaled,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    try:
        nn_accuracy = run_keras_version(X_train, X_holdout, y_train, y_holdout, X_scaled, y)
    except ModuleNotFoundError:
        nn_accuracy = run_fallback_version(X_train, X_holdout, y_train, y_holdout, X_scaled, y)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    knn_accuracy = knn.score(X_holdout, y_holdout)
    print("k-NN holdout accuracy:", round(knn_accuracy, 3))

    print("Target names:", list(target_names))
    print("Use these results in decision_boundary_notes.md")


if __name__ == "__main__":
    main()
