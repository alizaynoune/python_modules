import numpy as np


class ScrapBooker:
    def __init__(self) -> None:
        pass

    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
    and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple)\
                or not isinstance(position, tuple) or len(dim) != 2 or\
                len(position) != 2 or not all(i >= 0 for i in dim + position):
            return None
        return array[
            position[0]:dim[0]+position[0], position[1]:dim[1]+position[1]
        ]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis
            (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of
            row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or\
            not isinstance(n, int) or not isinstance(axis, int)\
                or not 0 <= axis <= 1 or not 0 < n <= array.shape[1 - axis]:
            return None
        index = np.arange(n - 1, array.shape[1 - axis], n)
        return np.delete(array, index, axis=1 - axis)

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray)\
            or not isinstance(n, int) or not isinstance(axis, int)\
                or n < 1 or not 0 <= axis <= 1:
            return None

        return np.concatenate([array] * n, axis=axis)

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array.
        The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray)\
            or not isinstance(dim, tuple) or len(dim) != 2 \
                or not all(isinstance(i, int) and i > 0 for i in dim):
            return None

        return np.tile(array, dim)
