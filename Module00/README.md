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
