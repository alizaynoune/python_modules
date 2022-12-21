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

