# Computational thinking test 2: converting dates

Here's another problem to get you thinking computationally: let's say you have some data which appears to contain dates like so: "30/10/2017". However, these are not proper dates (which should be stored as numbers) but actually *strings* of characters.

This is a problem for a number of reasons:

* Firstly, it means you cannot properly *order* your data by date: instead, because these are actually text strings, it will order alphabetically: 01/10/2017 will come before 02/01/2017
* Secondly, it means you cannot *calculate* using the dates (days elapsed between dates, for example)
* And thirdly, it means you cannot *extract* information from the dates - such as which day of the week that date fell on (let's say this was a dataset about emergency calls, for example, and we wanted to identify the day when most calls were made)

## Stage 1: Decomposition

Break down this problem ('Convert dates-as-strings into dates-as-dates') into separate problems. It may help to work backwards: what elements make up a date?

My approach to this was as follows (there will be other ways of breaking this down):

1. Split the string into its constituent parts: first the year...
2. ...Then the month...
3. ...Then the day of the month
4. Convert each part into a number
5. Recombine the three parts into a date

## Stage 2: Abstraction

Now, *for each problem*, abstract to what is the core element you are focusing on. For example:

* Challenge 1: I need a function to extract the specified portion of a string
* Challenge 4: I need to find a function which converts a string to a number
* Challenge 5: I need to find a function which will treat 3 numbers as a single date

## Stage 3: Pattern recognition

Look for patterns in the data and/or problems. Dates are very structured - there's an obvious pattern there.

You might also notice a pattern in the names of the functions that you find.

## Stage 4: Algorithm

Now to encode that process in a formula that can be repeated (an algorithm). There are many ways of doing this: you could separate each step into its own column, with each new column building upon the last. Or you could *nest* your formulae inside of each other so that the results of one forms the basis for another. Or you could do something in between those two (more than one column, with some containing nested formulae).
