import numpy as np
import matplotlib.pyplot as plt


class ImageProcessor:
    def __init__(self) -> None:
        pass

    def load(self, path):
        try:
            ret = np.array(plt.imread(path, format=None))
            rshap = np.shape(ret)
            print(f'Loading image of dimensions {rshap[0]} x {rshap[1]}')
            return (ret)
        except Exception as e:
            print(e)
            return None

    def display(self, array):
        if not isinstance(array, np.ndarray):
            print("The array must be a numpy.array")
            return None
        try:
            fig, ax = plt.subplots()
            ax.axis('off')
            ax.imshow(array)
            fig.canvas.manager.set_window_title('loaded Imgae')
            plt.show()
        except Exception as e:
            print(e)
            return None


imP = ImageProcessor()
ff = imP.load('./42AI.png')
imP.display(ff)
