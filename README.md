## Module 00
This first module of Python is designed to to get started with the Python language. You will study basic setup, variables, data types, functions,...
### ex00
here’s a few questions that need to be solved using
python, pip or conda. Save your answers in a file answers.txt (one answer per line and
per question), and check them with your peers.
Find the commands to:
- Output a list of installed packages and their versions.
- Show the package metadata of numpy.
- Remove the package numpy.
- (Re)install the package numpy.
- Freeze your python packages and their versions in a requirements.txt file you
have to turn-in.
### ex01
Make a program that takes a string as argument, reverses it, swaps its letters case
and print the result.
- If more than one argument are provided, merge them into a single string with each
argument separated by a space character.
- If no argument are provided, do nothing or print an usage.
### ex02
Make a program that takes a number as argument, checks whether it is odd, even or
zero, and print the result.
- If more than one argument are provided or if the argument is not an integer, print
an error message.
- If no argument are provided, do nothing or print an usage.
### ex03
Create a function called text_analyzer that takes a single string argument and displays
the sums of its upper-case characters, lower-case characters, punctuation characters and
spaces.
- If None or nothing is provided, the user is prompted to provide a string.
- If the argument is not a string, print an error message.
- This function must have a docstring explaning its behavior.
Test your function with the python console
### ex04
Write a program that takes two integers A and B as arguments and prints the result
of the following operations:
- If more or less than two argument are provided or if either of the argument is not
an integer, print an error message.
- If no argument are provided, do nothing or print an usage.
- If an operation is impossible, print an error message instead of a numerical result.
### ex05
Let’s get familiar with the useful concept of string formatting through a kata series.
Each exercice will provide you with a kata variable. This variable can be modified to
a certain extent: your program must react accordingly.
#### kata00
The kata variable is always a tuple and can only be filled with integer.
#### kata01
The kata variable is always a dictionary and can only be filled with strings.
#### kata02
The kata variable is always a tuple that contains 5 non-negative integers. The first
integer contains up to 4 digits, the rest up to 2 digits
#### kata03
The kata variable is always a string whose length is not higher than 42
#### kata04
The kata variable is always a tuple that contains, in the following order:
- 2 non-negative integer containing up to 2 digits
- 1 decimal
- 1 integer
- 1 decimal
### ex06
#### Part 1: Nested Dictionaries
Create a dictionary called cookbook. You will use this cookbook to store recipe.
A recipe is a dictionary that stores (at least) 3 couples key-value:
- ”ingredients": a list of string representing the list of ingredients
- "meal": a string representing the type of meal
- "prep_time": a non-negative integer representing a time in minutes
In the cookbook, the key to a recipe is the recipe name.
Initialize your cookbook with 3 recipes:
- The Sandwich’s ingredients are ham, bread, cheese and tomatoes. It is a lunch and
it takes 10 minutes of preparation.
- The Cake’s ingredients are flour, sugar and eggs. It is a dessert and it takes 60
minutes of preparation.
- The Salad’s ingredients are avocado, arugula, tomatoes and spinach. It is a lunch
and it takes 15 minutes of preparation.

#### Part 2: A series of Helpful Functions
Create a series of useful functions to handle your cookbook:
1. A function that print all recipe names.
2. A function that takes a recipe name and print its details.
3. A function that takes a recipe name and delete it.
4. A function that add a recipe from user input. You will need a name, a list of
ingredient, a meal type and a preparation time.
#### Part 3: A command line executable !
Create a program that use your cookbook and your functions.
The program will prompt the user to make a choice between printing the cookbook
content, printing one recipe, adding a recipe, deleting a recipe or quitting the cookbook.
Your program will continue to ask for prompt until the user decide to quit it. The
program cannot crash if a wrong value is entered: you must handle the error and ask for
another prompt.
### ex07
Make a program that takes a string S and an integer N as argument and print the list
of words in S that contains more than N non-punctuation characters.
- Words are separated from each other by space characters
- Punctuation symbols must be removed from the printed list: they are neither part
of a word nor a separator
- The program must contains at least one list comprehension expression.
If the number of argument is different from 2, or if the type of any argument is wrong,
the program prints an error message.
### ex08
Make a program that takes a string as argument and encode it into Morse code.
- The program supports space and alphanumeric characters
- An alphanumeric character is represented by dots . and dashes -:
- A space character is represented by a slash /
- Complete morse characters are separated by a single space
If more than one argument are provided, merge them into a single string with each
argument separated by a space character.
If no argument is provided, do nothing or print an usage.
### ex09
You have to make a program that will be an interactive guessing game. It will ask the
user to guess a number between 1 and 99. The program will tell the user if their input is
too high or too low. The game ends when the user finds out the secret number or types
exit. You will import the random module with the randint function to get a random
number. You have to count the number of trials and print that number when the user
wins.
If the user discovers the secret number on the first try, tell them. If the secret number
is 42, make a reference to Douglas Adams.
### ex10
You are about to discover the yield operator!
So let’s create a function called ft_progress(lst).
The function will display the progress of a for loop.

## Module 01
The goal of this module is to get started with the Python language. You will study objects, classes, inheritance, built-in functions, magic methods, generator ...
### ex00
#### Objective
The goal of the exercise is to get you familiar with the notions of classes and the manipulation of the objects related to those classes.
#### Instructions
You will have to make a class Book and a class Recipe. The classes Book and Recipe
will be written in book.py and recipe.py respectively.
Let’s describe the Recipe class. It has some attributes:
- name (str): name of the recipe,
- cooking_lvl (int): range from 1 to 5,
- cooking_time (int): in minutes (no negative numbers),
- ingredients (list): list of all ingredients each represented by a string,
- description (str): description of the recipe,
- recipe_type (str): can be "starter", "lunch" or "dessert".
You have to initialize the object Recipe and check all its values, only the description
can be empty. In case of input errors, you should print what they are and exit properly.
You will have to implement the built-in method __str__. It’s the method called when
the following code is executed:
The Book class also has some attributes:
- name (str): name of the book,
- last_update (datetime): the date of the last update,
- creation_date (datetime): the creation date,
- recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".
You will have to implement some methods in Book class:
You have to handle the error if the argument passed in add_recipe is not a Recipe.
Finally, you will provide a test.py file to test your classes and prove that they are
working properly. You can import all the classes into your test.py file by adding these
lines at the top of the test.py file:
### ex01
#### Objective
The goal of the exercise is to tackle the notion inheritance of class.
#### Instructions
Create a GotCharacter class and initialize it with the following attributes:
- first_name,
- is_alive (by default is True).
Pick up a GoT House (e.g., Stark, Lannister...) and create a child class that inherits
from GotCharacter and define the following attributes:
- family_name (by default should be the same as the Class)
- house_words (e.g., the House words for the Stark House is: "Winter is Coming")
Add two methods to your child class:
- print_house_words: prints the House words,
- die: changes the value of is_alive to False.
You can add any attribute or method you need to your class and format the docstring
the way you want to. Feel free to create other children of GotCharacter class.
### ex02
Objective
The goal of the exercise is to get you used with built-in methods, more particularly with
those allowing to perform operations. Student is expected to code built-in methods for
vector-vector and vector-scalar operations as rigorously as possible.
Instructions
In this exercise, you have to create a Vector class. The goal is to create vectors and be
able to perform mathematical operations with them.
- Column vectors are represented as list of lists of single float ([[1.], [2.], [3.]]),
- Row vectors are represented as a list of a list of several floats ([[1., 2., 3.]]).
The class should also has 2 attributes:
- values: list of list of floats (for row vector) or list of lists of single float (for column
vector),
- shape: tuple of 2 integers: (1,n) for a row vector of dimension n or (n,1) for a
column vector of dimension n.
Finally you have to implement 2 methods:
- .dot() produce a dot product between two vectors of same shape,
- .T() returns the transpose vector (i.e. a column vector into a row vector, or a row
vector into a column vector).
You will also provide a testing file (test.py) to demonstrate your class works as
expected. In this testing file, demonstrate:
- the addition and substraction are working for 2 vectors of the same shape,
- the mutliplication (mul and rmul) are working for a vector and a scalar,
- the division (truediv) is working with a vector and a scalar,
- the division (rtruediv) raises an Arithmetic Error (this test can be commented for
the other tests and uncommented to show this one),
You should be able to initialize the object with:
- a list of a list of floats: Vector([[0.0, 1.0, 2.0, 3.0]]),
- a list of lists of single float: Vector([[0.0], [1.0], [2.0], [3.0]]),
- a size: Vector(3) -> the vector will have values = [[0.0], [1.0], [2.0]],
- a range: Vector((10,16)) -> the vector will have values = [[10.0], [11.0],
[12.0], [13.0], [14.0], [15.0]]. in Vector((a,b)), if a > b, you must display accurate error message.
By default, the vectors are generated as classical column vectors if initialized with a
size or range.
To perform arithmetic operations for Vector-Vector or scalar-Vector, you have to
implement all the following built-in functions (called magic/special methods) for your
Vector class:
### ex03
#### Objective
The goal of the exercise is to discover the concept of generator object in Python.
#### Instructions
Code a function called generator that takes a text as input (only printable characters), uses the string parameter sep as a splitting parameter, and yields the resulting
substrings.
The function can take an optional argument. The options are:
- shuffle: shuffles the list of words,
- unique: returns a list where each word appears only once,
- ordered: alphabetically sorts the words.
You can only call one option at a time.
The function should return "ERROR" one time if the text argument is not a string,
or if the option argument is not valid.
### ex04
#### Objective
The goal of the exercise is to discover 2 useful methods for lists, tuples, dictionnaries
(iterable class objects more generally) named zip and enumerate.
#### Instructions
Code a class Evaluator, that has two static functions named zip_evaluate and enumerate_evaluate.
The goal of these 2 functions is to compute the sum of the lengths of every words of
a given list weighted by a list of coefficinents coefs (yes, the 2 functions should do the
same thing).
The lists coefs and words have to be the same length. If this is not the case, the
function should return -1.
You have to obtain the desired result using zip in the zip_evaluate function, and
with enumerate in the enumerate_evaluate function.
### ex05
Objective
The goals of this exercise is to discover new built-in functions and deepen your class
manipulation and to be aware of possibility to modify instanced objects.
In this exercise you learn how to modify or add attributes to an object.
Instructions
It is all about security. Have a look at the class named Account in the snippet of code
below.
```
# in the_bank.py
class Account(object):
ID_COUNT = 1
def __init__(self, name, **kwargs):
self.__dict__.update(kwargs)
self.id = self.ID_COUNT
Account.ID_COUNT += 1
self.name = name
if not hasattr(self, ’value’):
self.value = 0
if self.value < 0:
raise AttributeError("Attribute value cannot be negative.")
if not isinstance(self.name, str)
raise AttributeError("Attribute name must be a str object.")
def transfer(self, amount):
self.value += amount
```
Now, it is your turn to code a class named Bank! Its purpose will be to handle the
security part of each transfer attempt.
Security means checking if the Account is:
- the right object,
- not corrupted,
- and stores enough money to complete the transfer.
How do we define if a bank account is corrupted? A corrupted bank account has:
- an even number of attributes,
- an attribute starting with b,
- no attribute starting with zip or addr,
- no attribute name, id and value,
- name not being a string,
- id not being an int,
- value not being an int or a float.
For the rest of the attributes (addr, zip, etc ... there is no specific check expected.
Meaning you are not expected to evaluate the validity of the account based on the type
of the other attributes (the conditions listed above are sufficient).
Moreover, verification has to be performed when account objects are added to to Bank
instance (bank.add(Account(...))). The verification in add only check the type of the
new_account and if there is no account among the one already in Bank instance with
the same name.
A transaction is invalid if amount < 0 or if the amount is larger than the balance of
the account. Prior to the transfer, the validity of the 2 accounts (origin and dest) are
checked (according to the list of criteria above). A transfer between the same account
(bank.transfer(’Wiliam John’, ’William John’)) is valid but there is no fund movement.
fix_account recovers a corrupted account if it parameter name correspond to the
attribute name of one of the account in accounts (attribute of Bank). If name is not a
string or does not corresponded to an account name, the method return False.
Check out the dir built-in function.



## Module 02
The goal of this module is to tackle advanced notions of Python. You will learn more about decorators, lambda, context manager, build package,
### ex00
### Objective
The goal of the exercise is to work on the built-in functions map, filter and reduce.
### Instructions
Implement the functions ft_map, ft_filter and ft_reduce. Take the time to understand the use cases of these two built-in functions (map and filter) and the function
reduce in functools module. You are not expected to code specific classes to create
ft_map, ft_filter or ft_reduce objects, take a closer look to the examples to know
what to do.
Here the signatures of the functions:
You are expected to produce the raise of exception for the functions similar to exceptions of map, filter and reduce when wrong parameters are given (but no need to
reproduce the exact the same exception messages).
### ex01
#### Objective
The goal of the exercise is to discover and manipulate *args and **kwargs arguments.
#### Instructions
In this exercise you have to implement a function named what_are_the_vars which
returns an instance of class ObjectC.
ObjectC attributes are set via the parameters received during the instanciation. You will
have to modify the ’instance’ ObjectC, NOT the class.
You should take a look to getattr, setattr built-in functions.
### ex02
#### Objective
In this exercise, you will learn about decorators and we are not talking about the
decoration of your room. The @log will write info about the decorated function in a
machine.log file.
#### Instructions
You have to create the log decorator in the same file. Pay attention to all the different actions logged at the call of each methods. You may notice the username from environment
variable is written to the log file.
### ex03
Objective
The goal of this exercise is to implement a context manager as a class. Thus you are
strongly encouraged to do some research about context manager.
Instructions
Implement a CsvReader class that opens, reads, and parses a CSV file. This class is
then a context manager as class. In order to create it, your class requires a few built-in
methods:
- __init__,
- __enter__,
- __exit__.
It is mandatory to close the file once the process has completed. You are expected to
handle properly badly formatted CSV file (i.e. handle the exception):
- mistmatch between number of fields and number of records,
- records with different length.
CSV (for Comma-Separated Values) file is a delimited text file which uses a comma to
separate values. Therefore, the field separator (or delimiter) is usually a comma (,) but
with your context manager you have to offer the possibility to change this parameter.
One can decide if the class instance skips lines at the top and the bottom of the file
via the parameters skip_top and skip_bottom. One should also be able to keep the first
line as a header if header is True.
The file should not be corrupted (either a line with too many values or a line with
too few values), otherwise return None.
You have to handle the case file not found.
You are expected to implement two methods:
- getdata(),
- getheader().
### ex04
#### Objective
The goal of the exercise is to learn how to build a package and understand the magnificence of PyPi.
#### Instructions
You have to create a package called my_minipack.
It will have 2 modules:
- the progress bar (module00 ex10) which should be imported it via import my_minipack.progress- the logger (module02 ex02), which should be imported via import my_minipack.logger.
The package will be installed via pip using one of the following commands (both
should work):
```
pip install ./dist/my_minipack-1.0.0.tar.gz
pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
```
### ex05
#### Objective
Initiation to very basic statistic notions.
#### Instructions
Create a class named TinyStatistician that implements the following methods:
- mean(x): computes the mean of a given non-empty list or array x, using a for-loop.
The method returns the mean as a float, otherwise None if x is an empty list or
array. Given a vector x of dimension m × 1, the mathematical formula of its mean
- median(x): computes the median of a given non-empty list or array x. The method
returns the median as a float, otherwise None if x is an empty list or array.
- quartiles(x): computes the 1
st and 3
rd quartiles of a given non-empty array x.
The method returns the quartile as a float, otherwise None if x is an empty list or
array.
- var(x): computes the variance of a given non-empty list or array x, using a forloop. The method returns the variance as a float, otherwise None if x is an empty
list or array. Given a vector x of dimension m × 1, the mathematical formula of its variance is
- std(x) : computes the standard deviation of a given non-empty list or array x,
using a for-loop. The method returns the standard deviation as a float, otherwise
None if x is an empty list or array. Given a vector x of dimension m × 1, the
mathematical formula of its standard deviation is
All methods take a list or a numpy.ndarray as parameter.
We are assuming that all inputs have a correct format, i.e. a list or array of numeric type
or empty list or array. You don’t have to protect your functions against input errors




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


## Module 04
This fifth module is dedicated to the manipulation of Pandas library, widely used in datascience field.
### ex00
#### Objective
The goal of this exercise is to create a Fileloader class containing a load and a display
method.
#### Instructions
Write a class named FileLoader which implements the following methods:
- load(self, path): takes as an argument the file path of the dataset to load,
displays a message specifying the dimensions of the dataset (e.g. 340 x 500) and
returns the dataset loaded as a pandas.DataFrame.
- display(self, df, n): takes a pandas.DataFrame and an integer as arguments,
displays the first n rows of the dataset if n is positive, or the last n rows if n is
negative.
FileLoader object should not raise any exceptions (wrong path, file does not exist,
parameters different than a string ...).
### ex01
#### Objective
The goal of this exercise is to create a function that will return a dictionary containing
the age of the youngest woman and the youngest man who took part in the Olympics a
given year.
#### Instructions
This exercise uses the following dataset: athlete_events.csv.
Write a function youngest_fellah that takes two arguments:
- a pandas.DataFrame which contains the dataset
- an Olympic year.
The function returns a dictionary containing the age of the youngest woman and man
who took part in the Olympics on that year. The name of the dictionary’s keys is up to
you, but it must be self-explanatory.
### ex02
#### Objective
The goal of this exercise is to create a function displaying the proportion of participants
who played a given sport, among the participants of a given genders.
#### Instructions
This exercise uses the dataset athlete_events.csv.
Write a function proportion_by_sport that takes four arguments:
- a pandas.DataFrame of the dataset,
- an olympic year,
- a sport,
- a gender.
The function returns a float corresponding to the proportion (percentage) of participants who played the given sport among the participants of the given gender.
The function answers questions like the following : "What was the percentage of
female basketball players among all the female participants of the 2016 Olympics?"
### ex03
#### Objective
The goal of this exercise is to implement a function that will return a dictionary of dictionaries giving the number and type of medals for each year during which the participant
won medals.
#### Instructions
This exercise uses the following dataset: athlete_events.csv.
Write a function how_many_medals that takes two arguments:
- a pandas.DataFrame which contains the dataset,
- a participant name.
The function returns a dictionary of dictionaries giving the number and type of medals
for each year during which the participant won medals. The keys of the main dictionary are the Olympic games years. In each year’s dictionary, the keys are ’G’, ’S’, ’B’
corresponding to the type of medals won (gold, silver, bronze). The innermost values
correspond to the number of medals of a given type won for a given year.
### ex04
#### Objective
The goal of this exercise is to implement a class called SpatioTemporalData that takes a
dataset (pandas.DataFrame) as argument in its constructor and implements two methods.
#### Instructions
This exercise uses the dataset athlete_events.csv.
Write a class called SpatioTemporalData that takes a dataset (pandas.DataFrame)
as argument in its constructor and implements the following methods:
- when(location): takes a location as an argument and returns a list containing the
years where games were held in the given location,
- where(date): takes a date as an argument and returns the location where the
Olympics took place in the given year.
### ex05
#### Objective
The goal of this exercise is to write a function that returns a dictionary of dictionaries
giving the number and type of medal for each competition where the country delegation
earned medals.
#### Instructions
This exercise uses the following dataset: athlete_events.csv
Write a function how_many_medals_by_country that takes two arguments:
- a pandas.DataFrame which contains the dataset
- a country name.
The function returns a dictionary of dictionaries giving the number and type of medal
for each competition where the country delegation earned medals. The keys of the main
dictionary are the Olympic games’ years. In each year’s dictionary, the key are ’G’, ’S’,
’B’ corresponding to the type of medals won.
Duplicated medals per team games should be handled and not counted twice. Hint:
You probably guessed by now that we gave up providing real examples...
If you want real examples, you can easily look online. Do beware that some medals
might be awarded or removed years after the games are over, for example if a previous
medallist was found to have cheated and is sanctioned. The athlete_events.csv dataset
might not always take these posterior changes into account.
### ex06
#### Objective
The goal the exercise is to introduce plotting methods among the different libraries Pandas, Matplotlib, Seaborn or Scipy.
#### Instructions
This exercise uses the following dataset: athlete_events.csv
Write a class called MyPlotLib. This class implements different plotting methods,
each of which take two arguments:
- a pandas.DataFrame which contains the dataset,
- a list of feature names.
- histogram(data, features): plots one histogram for each numerical feature in
the list,
- density(data, features): plots the density curve of each numerical feature in
the list,
- pair_plot(data, features): plots a matrix of subplots (also called scatter plot
matrix). On each subplot shows a scatter plot of one numerical variable against
another one. The main diagonal of this matrix shows simple histograms.
- box_plot(data, features): displays a box plot for each numerical variable in the
dataset.
### ex07
#### Objective
The goal the exercise is to introduce plotting methods among the different libraries Pandas, Matplotlib, Seaborn or Scipy.
#### Instructions
This exercise uses the following dataset: athlete_events.csv.
Write a class called Komparator whose constructor takes as an argument a pandas.DataFrame which contains the dataset. The class must implement the following
methods, which take as input two variable names:
- compare_box_plots(self, categorical_var, numerical_var): displays a series of box plots to compare how the distribution of the numerical variable changes
if we only consider the subpopulation which belongs to each category. There should
be as many box plots as categories. For example, with Sex and Height, we would
compare the height distributions of men vs. women with two box plots.
- density(self, categorical_var, numerical_var): displays the density of the
numerical variable. Each subpopulation should be represented by a separate curve
on the graph.
- compare_histograms(self, categorical_var, numerical_var): plots the numerical variable in a separate histogram for each category. As an extra, you can
use overlapping histograms with a color code.

