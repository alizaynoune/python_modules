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