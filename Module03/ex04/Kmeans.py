import sys
import numpy as np


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
        # print(X.shape)
        if not isinstance(X, np.ndarray) or X.shape[0] < self.ncentroid:
            return None
        indexs = np.random.choice(
            X.shape[0] - 1, size=self.ncentroid, replace=False)
        self.centroids = X[indexs]
        # print(self.centroids)
        #sq (c.i - x.i)**2 + (c.i - y.i)**2 + (c.i - y.i)**2
        # np.sqrt(np.sum((a-b)**2,axis=1))
        # print(np.sqrt(np.sum([1] - [1])**2))
        print(np.sqrt(np.sum(np.subtract([9, 9, 20], [0, 9, 3])**2)))
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
        pass


def parse_arg(argv):
    """
    parse arguments [filepath, max_iter, ncentroid]
    """
    args = {}
    if len(argv) != 4:
        return None
    for i in argv[1:]:
        name = i.split('=')
        if len(name) != 2 or name[0] not in ['filepath', 'max_iter', 'ncentroid']:
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
        for l in lines[1:]:
            l_split = l.split(',')
            if len(l_split) != H_len:
                return None
            data.append([float(i) for i in l_split[1:]])
        return np.array(data)
    except Exception:
        return None


def display_info(dataset):
    pass


#sq (c.i - x.i)**2 + (c.i - y.i)**2 + (c.i - y.i)**2


if __name__ == "__main__":
    args = parse_arg(sys.argv)
    if args:
        dataset = read_dataset(args['filepath'])
        if not dataset is None:
            # print(dataset[0])
            km = KmeansClustering(
                max_iter=args['max_iter'], ncentroid=args['ncentroid'])
            km.fit(dataset)
        else:
            print('Error: invalid file')
    else:
        print('Error : invalid arguments')
