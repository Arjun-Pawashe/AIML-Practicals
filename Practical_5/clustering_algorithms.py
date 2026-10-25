"""
Practical 6: Clustering Algorithms Implementation & Performance Evaluation
Dataset : Iris (real-world, 150 samples, 4 features)
Models  : K-Means, Agglomerative (Ward) Hierarchical Clustering, DBSCAN
Metrics : Silhouette Score, Davies-Bouldin Index, Calinski-Harabasz Index
Run     : python clustering_algorithms.py
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # works without a display; remove if running interactively
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import (silhouette_score, davies_bouldin_score,
                             calinski_harabasz_score)
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

# ---------------------------------------------------------------------------
# 1. Data preparation
# ---------------------------------------------------------------------------
iris = load_iris()
X = iris.data
feature_names = iris.feature_names

# Standardise features (clustering is distance based)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2-D projection for visualisation only
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

results = {}


def evaluate_clustering(name, labels, X_data):
    """Evaluate a clustering; noise points (-1, e.g. from DBSCAN) are excluded."""
    unique_labels = set(labels)
    valid_mask = (labels != -1) if -1 in unique_labels else np.ones(len(labels), dtype=bool)

    n_clusters = len(unique_labels - {-1})
    n_noise = int((labels == -1).sum())
    if n_clusters > 1:
        sil = silhouette_score(X_data[valid_mask], labels[valid_mask])
        db = davies_bouldin_score(X_data[valid_mask], labels[valid_mask])
        ch = calinski_harabasz_score(X_data[valid_mask], labels[valid_mask])
    else:
        sil, db, ch = np.nan, np.nan, np.nan

    results[name] = {"Clusters": n_clusters, "Silhouette Score": sil,
                     "Davies-Bouldin Index": db, "Calinski-Harabasz Index": ch}

    print(f"--- {name} Performance ---")
    print(f"Estimated Clusters: {n_clusters}")
    print(f"Noise Points       : {n_noise}")
    print(f"Silhouette Score   : {sil:.4f} (Higher is better)")
    print(f"Davies-Bouldin Index: {db:.4f} (Lower is better)")
    print(f"Calinski-Harabasz  : {ch:.4f} (Higher is better)\n")


def plot_clusters(labels, title, cmap, colorbar_label, filename):
    """Scatter plot of the clusters in the 2-D PCA space."""
    plt.figure(figsize=(7, 5))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap=cmap, s=50, alpha=0.8)
    plt.title(title)
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")
    plt.colorbar(label=colorbar_label)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# 2. K-Means
# ---------------------------------------------------------------------------
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)
evaluate_clustering("K-Means", kmeans_labels, X_scaled)
plot_clusters(kmeans_labels, "K-Means Clustering (2D PCA Projection)",
              "viridis", "Cluster", "kmeans_clusters.png")

# ---------------------------------------------------------------------------
# 3. Agglomerative hierarchical clustering
# ---------------------------------------------------------------------------
agg_clustering = AgglomerativeClustering(n_clusters=3, linkage="ward")
agg_labels = agg_clustering.fit_predict(X_scaled)
evaluate_clustering("Agglomerative Clustering", agg_labels, X_scaled)
plot_clusters(agg_labels, "Agglomerative Clustering (2D PCA Projection)",
              "plasma", "Cluster", "agglomerative_clusters.png")

# ---------------------------------------------------------------------------
# 4. DBSCAN
# ---------------------------------------------------------------------------
dbscan = DBSCAN(eps=0.6, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)
evaluate_clustering("DBSCAN", dbscan_labels, X_scaled)
plot_clusters(dbscan_labels, "DBSCAN Clustering (2D PCA Projection)",
              "coolwarm", "Cluster Label (-1: Noise)", "dbscan_clusters.png")

# ---------------------------------------------------------------------------
# 5. Comparative analysis
# ---------------------------------------------------------------------------
df_results = pd.DataFrame(results).T
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)
print("=" * 69)
print("                   CLUSTERING EVALUATION SUMMARY")
print("=" * 69)
print(df_results.round(4))
print("=" * 69 + "\n")
df_results.round(4).to_csv("results.csv")

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
df_results["Silhouette Score"].plot(kind="bar", ax=ax[0], color="skyblue")
ax[0].set_title("Silhouette Score (Higher = Better)")
ax[0].set_ylabel("Score")
ax[0].grid(axis="y", linestyle="--", alpha=0.7)
df_results["Davies-Bouldin Index"].plot(kind="bar", ax=ax[1], color="salmon")
ax[1].set_title("Davies-Bouldin Index (Lower = Better)")
ax[1].set_ylabel("Score")
ax[1].grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("metrics_comparison.png", dpi=150)
