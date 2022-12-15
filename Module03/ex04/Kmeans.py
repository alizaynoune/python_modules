import sys
import numpy as np


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid  # number of centroids
        self.max_iter = max_iter  # number iterations to update the centroids
        self.centroids = []  # values of the centroids

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids,
        random pick ncentroids from the dataset.
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
        if not isinstance(X, np.ndarray) or X.shape[0] < self.ncentroid:
            return None
        indexs = np.random.choice(
            X.shape[0] - 1, size=self.ncentroid, replace=False)
        self.centroids = X[indexs]
        distances = [[] for _ in range(self.ncentroid)]
        for _ in range(self.max_iter):
            clusters = [[] for _ in range(self.ncentroid)]
            for i, centeroid in enumerate(self.centroids):
                distances[i] = (np.linalg.norm(X - centeroid, axis=1))

            minDistValues = (np.min(distances, axis=0))
            clustersIndices = (np.argmin(distances, axis=0))
            for i, v in zip(clustersIndices, minDistValues):
                clusters[i].append(np.where(distances[i] == v)[0][0])
            tmp = self.centroids.copy()
            for i in range(self.ncentroid):
                self.centroids[i] = np.sum(
                    X[clusters[i]], axis=0) / len(clusters[i])

            if (tmp == self.centroids).all():
                return None
        return None

    def predict(self, X):
        """
        Predict from which cluster each datapoint belongs to.
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
        if not isinstance(X, np.ndarray) or\
                X.shape[0] < self.ncentroid or not len(self.centroids):
            return None
        distances = [[] for _ in range(self.ncentroid)]
        for i, centeroid in enumerate(self.centroids):
            distances[i] = (np.linalg.norm(X - centeroid, axis=1))
        return (np.argmin(distances, axis=0))


def parse_arg(argv):
    """
    parse arguments [filepath, max_iter, ncentroid]
    """
    args = {}
    if len(argv) != 4:
        return None
    for i in argv[1:]:
        name = i.split('=')
        if len(name) != 2 or\
                name[0] not in ['filepath', 'max_iter', 'ncentroid']:
            return None
        args[name[0]] = name[1]
    try:
        args['max_iter'] = int(args['max_iter'])
        args['ncentroid'] = int(args['ncentroid'])
        if args['max_iter'] <= 0 or args['ncentroid'] <= 0:
            return None
    except Exception:
        return None
    return args


def read_dataset(filepath):
    """
    read dataset from filepath
    return np.array
    """
    try:
        file = open(filepath, 'r')
        lines = file.read().splitlines()
        file.close()
        data = []
        H_len = len(lines[0].split(','))
        for line in lines[1:]:
            l_split = line.split(',')
            if len(l_split) != H_len:
                return None
            data.append([float(i) for i in l_split[1:]])
        return np.array(data)
    except Exception:
        return None


def display_info(km, predict):
    if not isinstance(predict, np.ndarray)\
            or not isinstance(km, KmeansClustering):
        print('Error')
        return None
    clusters = np.unique(predict, return_counts=True)
    if len(clusters[0]) != km.ncentroid:
        print('Error')
        return None
    if km.ncentroid == 4 and (len(km.centroids)) == 4:
        areas = {}
        centroids = km.centroids.copy()
        centroids = centroids[centroids[:, 0].argsort()]  # sort by day
        centroids = centroids[centroids[:, 2].argsort(kind='mergesort')[::-1]]
        areas['Belt'] = centroids[-1]
        centroids = centroids[centroids[:3, 1].argsort(kind='mergesort')[::-1]]
        areas['Venus'] = centroids[-1]
        centroids = centroids[centroids[:2, 0].argsort(kind='mergesort')]
        areas['Mars'] = centroids[-1]
        areas['Earth'] = centroids[0]
        f = 'Coordinates of the different centroids and the associated region'
        print(f)
        print(f"{areas['Venus']} . The flying cities of Venus")
        print(f"{areas['Earth']} . United Nations of Earth")
        print(f"{areas['Mars']} . Mars Republic")
        print(f"{areas['Belt']} . Asteroids' Belt colonies\n")

    print('Number of individuals associated to each centroid')
    for i in range(km.ncentroid):
        print(f"{km.centroids[i]} . {clusters[1][i]}")


if __name__ == "__main__":
    args = parse_arg(sys.argv)
    if args:
        dataset = read_dataset(args['filepath'])
        if dataset is not None:
            km = KmeansClustering(
                max_iter=args['max_iter'], ncentroid=args['ncentroid'])
            km.fit(dataset)
            predict = km.predict(dataset)
            if predict is not None:
                display_info(km, predict)
            else:
                print('Error')

        else:
            print('Error: invalid file')
    else:
        print('Error : invalid arguments')
