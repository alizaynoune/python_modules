## Module 03
This fourth module of Python is designed to to get started with the library Numpy.
### ex00
#### Objective
Introduction to Numpy library.
#### Instructions
Write a class named NumPyCreator, that implements all of the following methods. Each
method receives as an argument a different type of data structure and transforms it into
a Numpy array:
- from_list(self, lst): takes a list or nested lists and returns its corresponding
Numpy array.
- from_tuple(self, tpl): takes a tuple or nested tuples and returns its corresponding Numpy array.
- from_iterable(self, itr): takes an iterable and returns an array which contains
all its elements.
- from_shape(self, shape, value): returns an array filled with the same value.
The first argument is a tuple which specifies the shape of the array, and the second
argument specifies the value of the elements. This value must be 0 by default.
- random(self, shape): returns an array filled with random values. It takes as an
argument a tuple which specifies the shape of the array.
- identity(self, n): returns an array representing the identity matrix of size n.
BONUS: Add to those methods an optional argument which specifies the datatype
(dtype) of the array (e.g. to represent its elements as integers, floats, ...)
ll those methods can be implemented in one line. You only need to find the right
Numpy functions.
### ex01
#### Objective
Basic manipulation of image via matplotlib library.
#### Instructions
Build a tool that will be helpful to load and display images in the upcoming exercises.
Write a class named ImageProcessor that implements the following methods:
- load(path): opens the PNG file specified by the path argument and returns an
array with the RGB values of the pixels image. It must display a message specifying
the dimensions of the image (e.g. 340 x 500).
- display(array): takes a numpy array as an argument and displays the corresponding RGB image.
You must handle errors, if the file passed as argument does not exist or if it can’t be
read as an image, with an appropriate message of your choice.
The image must to be displayed in a separate window when running in the console.
### ex02
#### Objective
Manipulation and initiation to slicing method on numpy arrays.
#### Instructions
Implement a class named ScrapBooker with the following methods:
- crop,
- thin,
- juxtapose,
- mosaic.
```
# within the class
def crop(self, array, dim, position=(0,0)):
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
... your code ...
def thin(self, array, n, axis):
"""
Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
Args:
-----
array: numpy.ndarray.
n: non null positive integer lower than the number of row/column of the array
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
... your code ...
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
... your code ...
def mosaic(self, array, dim):
"""
Makes a grid with multiple copies of the array. The dim argument specifies
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
... your code ...
```
In this exercise, when specifying positions or dimensions, we will assume that the first
coordinate is counted along the vertical axis starting from the top, and that the second
coordinate is counted along the horizontal axis starting from the left. Indexing starts
from 0.
### ex03
#### Objective
Manipulation of loaded image via numpy arrays, broadcasting.
#### Instructions
You have to develop a tool that can apply a variety of color filters on images. For this
exercise, the authorized functions and operators are specified for each methods. You are
not allowed to use anything else.
Write a class named ColorFilter with 6 methods with the following exact signatures:
You have some restrictions on the authorized methods and operators for each filter
method in class ColorFilter:
- invert:
◦ Authorized functions: .copy.
◦ Authorized operators: +,-,=.
- to_blue:
◦ Authorized functions: .copy, .zeros,.shape,.dstack.
◦ Authorized operators: =.
- to_green:
◦ Authorized functions: .copy.
◦ Authorized operators: *, =.
- to_red:
◦ Authorized functions: .copy, .to_green,.to_blue.
◦ Authorized operators: -,+, =.
- to_celluloid(array):
◦ Authorized functions: .copy, .arange,.linspace, .min, .max.
◦ Authorized operators: =, <=, >, & (or and).
- to_grayscale:
◦ Authorized functions: .sum,.shape,.reshape,.broadcast_to,.as_type.
◦ Authorized operators: *,/, =.
### ex04
#### Objective
Implementation of a basic Kmeans algorithm.
#### Instructions
The solar system census dataset is corrupted! The citizens’ homelands are missing! You
must implement the K-means clustering algorithm in order to recover the citizens’ origins.
You can find good explanations on how K-means is working here: Possibly the simplest
way to explain K-Means algorithm
The missing part is how to compute the distance between 2 data points (cluster centroid or a row in the data). In our case the data we have to process is composed of 3
values (height, weight and bone_density). Thus, each data point is a vector of 3 values.
Now that we have mathematically defined our data points (vector of 3 values), it is very
easy to compute the distance between two points using vector properties.
You can use L1 distance, L2 distance, cosine similarity, and so forth... Choosing the
distance to use is called hyperparameter tuning. I would suggest you to try with the
easiest setting (L1 distance) first.
What you will notice is that the final result of the "training"/"fitting" will depend a
lot on the random initialization. Commonly, in machine-learning libraries, K-means is
run multiple times (with different random initializations) and the best result is saved.
NB: To implement the fit function, keep in mind that a centroid can be considered as
the gravity center of a set of points.
Your program Kmeans.py takes 3 parameters: filepath, max_iter and ncentroid:
```
python Kmeans.py filepath='../ressources/solar_system_census.csv' ncentroid=4 max_iter=30
```
it is expected by running your program to:
- parse the arguments,
- read the dataset,
- fit the dataset,
- display the coordinates of the different centroids and the associated region (for the
case ncentroid=4),
- display the number of individuals associated to each centroid,
- (Optional) display on 3 differents plots, corresponding to 3 combinaisons of 2 parameters, the results. Use different colors to distinguish between Venus, Earth,
Mars and Belt asteroids citizens.
Create the class KmeansClustering with the following methods:
```
class KmeansClustering:
def __init__(self, max_iter=20, ncentroid=5):
self.ncentroid = ncentroid # number of centroids
self.max_iter = max_iter # number of max iterations to update the centroids
self.centroids = [] # values of the centroids
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
... your code ...
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
... your code ...
```
#### Dataset
The dataset, named solar_system_census can be found in the resources folder. It is
a part of the solar system census dataset, and contains biometric informations such as
the height, weight, and bone density of solar system citizens.
Solar citizens come from four registered areas:
- The flying cities of Venus,
- United Nations of Earth,
- Mars Republic,
- Asteroids’ Belt colonies.
Unfortunately the data about the planets of origin was lost... Use your K-means
algorithm to recover it! Once your clusters are found, try to find matches between
clusters and the citizens’ homelands.
- People are slender on Venus than on Earth.
- People of the Martian Republic are taller than on Earth.
- Citizens of the Belt are the tallest of the solar system and
have the lowest bone density due to the lack of gravity.

