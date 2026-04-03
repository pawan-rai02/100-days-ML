from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from _71_kMeans import KMeans

centroids = [(-5, -5), (5, 5), (-9, -2), (2.5, -2.5)]
cluster_std = [1, 1, 1, 1]


x, y = make_blobs(n_samples=1000, centers=centroids, cluster_std=cluster_std, random_state=42)


km = KMeans(n_clusters=4, max_iters=100)
labels = km.fit_predict(x)

plt.scatter(x[:, 0], x[:, 1], c=labels, cmap='viridis')
plt.scatter(km.centroids[:, 0], km.centroids[:, 1], c='red', marker='X')
plt.title('K-Means Clustering from Scratch')
plt.show()