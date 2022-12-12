import numpy as np
from matplotlib import pyplot as plt
# import cv2


class ColorFilter:
    def __init__(self) -> None:
        pass

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or len(array.shape) < 3 or array.shape[2] < 3:
            return None
        new_arr = array.copy()
        new_arr[:, :, 0:3] = 1.0 - new_arr[:, :, 0:3]
        return new_arr

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or len(array.shape) < 3 or array.shape[2] < 3:
            return None
        new_arr = array.copy()
        new_arr[:, :, 0:2] = 0
        return new_arr

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or len(array.shape) < 3 or array.shape[2] < 3:
            return None
        new_arr = array.copy()
        new_arr[:, :, (0, 2)] = 0
        return new_arr

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or len(array.shape) < 3 or array.shape[2] < 3:
            return None
        new_arr = array.copy()
        new_arr[:, :, 1:3] = 0
        return new_arr

    def to_celluloid(self, image):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray) is False:
            return None
        thresholds = np.linspace(array.min(), array.max(), 5)
        new_arr = array.copy()
        for i in range(1, len(thresholds)):
            new_arr[(array < thresholds[i]) & (
                array > thresholds[i - 1])] = thresholds[i]

        return new_arr

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        pass


cf = ColorFilter()
imgP = '../assets/elon_canaGAN.png'
# imgP = '../assets/42AI.png'
array = plt.imread(imgP)
# for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
#     plt.imshow(f(array))
#     plt.axis('off')
#     plt.show()

# im = cf.to_grayscale(array, "m")
# plt.imshow(array, cmap="gray")
# plt.axis('off')
# plt.show()

# im = cf.to_grayscale(array, "w", weights=[0.2126, 0.7152, 0.0722])
# plt.imshow(im, cmap="gray")
# plt.axis('off')
# plt.show()

im = cf.to_celluloid(array)
plt.imshow(im)
plt.axis('off')
plt.show()
