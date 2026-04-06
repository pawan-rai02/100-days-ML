'''
K-Means Clustering Implementation Algorithm from Scratch
    1. decide the number of clusters (k)
    2. randomly initialize the centroids (k points in the feature space)
    3. assign each data point to the nearest centroid, forming k clusters
    4. update the centroids by calculating the mean of the data points in each cluster
    5. repeat steps 3 and 4 until convergence (when the centroids do not change significantly or a maximum number of iterations is reached)
'''

import random
import numpy as np


class KMeans:
    def __init__(self, n_clusters = 2, max_iters = 100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.centroids = None

    def fit_predict(self, x):
        random_idx = (random.sample(range(0, x.shape[0]), self.n_clusters))
        self.centroids = x[random_idx]
        
        for _ in range(self.max_iters):
            # assign clusters
            cluster_group = self.assign_clusters(x)

            # move the centroids
            old_centroids = self.centroids.copy()
            self.centroids = self.move_centroids(x, cluster_group)

            # check finish
            if (old_centroids == self.centroids).all():
                break
        return cluster_group


    def assign_clusters(self, x):
        cluster_group = []
        distances = []

        for row in x:
            for centroid in self.centroids:
                distance = np.sqrt(np.dot(row - centroid, row - centroid))
                distances.append(distance)
            min_distance = min(distances)
            idx_pos = distances.index(min_distance)
            cluster_group.append(idx_pos)
            distances.clear()
        return np.array(cluster_group)
    
    def move_centroids(self, x, cluster_group):
        new_centroids = []

        cluster_types = np.unique(cluster_group)
        for cluster in cluster_types:
            cluster_points = x[cluster_group == cluster]
            new_centroid = np.mean(cluster_points, axis=0)
            new_centroids.append(new_centroid)
        return np.array(new_centroids)