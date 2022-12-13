
class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number of max iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# # %matplotlib inline
# X = -2 * np.random.rand(100, 2)
# print(X)
# # X1 = 1 + 2 * np.random.rand(50, 2)
# # X[50:100, :] = X1
# # plt.scatter(X[:, 0], X[:, 1], s=50, c= 'b')
# # plt.show()
# Kmean = KMeans(n_clusters=2)
# Kmean.fit(X)
# Kmean.cluster_centers_
# plt.scatter(X[:, 0], X[:, 1], s=50, c='b')
# # plt.scatter(-0.94665068, -0.97138368, s=200, c='g', marker='s')
# # plt.scatter(2.01559419, 2.02597093, s=200, c='r', marker='s')
# plt.show()
# Kmean.labels_
# sample_test = np.array([-3.0, -3.0])
# second_test = sample_test.reshape(1, -1)
# Kmean.predict(second_test)
