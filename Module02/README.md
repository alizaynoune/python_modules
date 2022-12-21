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
