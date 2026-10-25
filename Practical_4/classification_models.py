"""
Practical 5: Classification Models Implementation & Comparative Analysis
Models : Support Vector Machine, Decision Tree, K-Nearest Neighbors, Naive Bayes
Metrics: Accuracy, Precision, Recall, F1-Score, Log Loss
Run    : python classification_models.py
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # works without a display; remove if running interactively
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, log_loss)
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# ---------------------------------------------------------------------------
# 1. Dataset generation, split and scaling
# ---------------------------------------------------------------------------
X, y = make_classification(n_samples=1000, n_features=10, n_informative=8,
                           n_redundant=2, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Scaling is essential for distance-based algorithms (SVM, KNN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

results = {}


def evaluate_model(name, model, X_test_data, y_true):
    """Calculate, store and print performance metrics for a fitted model."""
    y_pred = model.predict(X_test_data)

    # Probability predictions are needed for Log Loss
    if hasattr(model, "predict_proba"):
        y_proba = model.predict_proba(X_test_data)
    elif hasattr(model, "decision_function"):
        d = model.decision_function(X_test_data)
        p = 1 / (1 + np.exp(-d))
        y_proba = np.vstack([1 - p, p]).T
    else:
        y_proba = None

    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    loss = log_loss(y_true, y_proba) if y_proba is not None else np.nan

    results[name] = {"Accuracy": acc, "Precision": prec, "Recall": rec,
                     "F1-Score": f1, "Log Loss": loss}

    print(f"--- {name} Performance ---")
    print(f"Accuracy : {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall   : {rec:.4f}")
    print(f"F1-Score : {f1:.4f}")
    print(f"Log Loss : {loss:.4f}\n")


# ---------------------------------------------------------------------------
# 2. Models
# ---------------------------------------------------------------------------
svm_model = SVC(kernel="rbf", C=1.0, probability=True, random_state=42)
svm_model.fit(X_train_scaled, y_train)
evaluate_model("Support Vector Machine", svm_model, X_test_scaled, y_test)

dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)  # Decision trees are scale-invariant
evaluate_model("Decision Tree", dt_model, X_test, y_test)

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train_scaled, y_train)
evaluate_model("K-Nearest Neighbors", knn_model, X_test_scaled, y_test)

nb_model = GaussianNB()
nb_model.fit(X_train_scaled, y_train)
evaluate_model("Naïve Bayes", nb_model, X_test_scaled, y_test)

# ---------------------------------------------------------------------------
# 3. Comparative analysis
# ---------------------------------------------------------------------------
df_results = pd.DataFrame(results).T
print("=" * 69)
print("                      COMPARATIVE ANALYSIS SUMMARY")
print("=" * 69)
print(df_results.round(4))
print("=" * 69 + "\n")
df_results.round(4).to_csv("results.csv")

df_results[["Accuracy", "Precision", "Recall", "F1-Score"]].plot(
    kind="bar", figsize=(10, 6))
plt.title("Model Performance Comparison")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig("model_comparison.png", dpi=150)
