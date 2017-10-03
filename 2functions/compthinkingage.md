# Computational thinking: calculating someone's age based on their birth date

*This is adapted from a chapter in the book [Telling Stories with Spreadsheets](http://leanpub.com/spreadsheetstories)*

Marion Urban is a French journalist with decades of experience. In 2014 she was preparing for the General Election the next year - and focusing on the data others would need to be able to report quickly.

In order to do this Marion had downloaded details on the candidates who had stood successfully in the previous election. "It was a very young intake," she noted. "But it wasn't easy to calculate their ages".

Indeed. You would think that calculating ages in Excel would be easy. But there is no off-the-shelf function to help you do so. Or at least, no easy-to-find function.

Instead there are a range of different approaches: some of them particularly, and unnecessarily complicated.

## Some data to work with: how old are Guantanamo prisoners?

At [this link you'll find a spreadsheet containing details on almost 800 individuals detained by the US Department of Defense at Guantanamo Bay, Cuba](https://drive.google.com/file/d/0B5To6f5Yj1iJa0xmbVNRZTdyQk0/edit?usp=sharing).

The spreadsheet was found on the site for the [Center for the Study of Human Rights in the Americas](http://humanrights.ucdavis.edu) by using the advanced search `"Date of Birth" Guantanamo filetype:xls`.


## Breaking down the problem - decomposition

If your spreadsheet problem isn't solvable with a single function, the best approach is often to break it down into smaller problems which, individually, can. What do we have, or need?

* Someone's birth date
* Now
* The difference between the two, in years (their age)

Here's one approach using *pattern recognition*:

1. Find out what year it is today
2. Find out the person's birth year
3. Find out the number of years elapsed between the birth year and this year (e.g. 2017-1970 = 47 years)
4. Check if their birthday hasn't taken place this year
5. If it hasn't taken place, subtract 1 from the number of years (e.g. 47-1 = 46 years old)

Here's another approach

1. Find out what date it is today
2. Find out the person's birth date
3. Find out the number of *days* elapsed between the birth date and today
4. Divide that total by the *average* number of days in a year
5. Round the total down to a whole number

## Abstraction

Depending which way you have decomposed the problem, you will need to abstract in different ways: the first series of steps requires you to 'abstract' a year from today's date; the second steps require you to abstract a period of time into days.

In the latter case abstraction is made easier if you understand more about how days are stored in Excel: they are actually stored as numbers that represent the quantity of days since January 1 1900, and that number is only *formatted* as a date. You can format it in any way you want, including an integer (whole number).

Likewise abstracting the 'average' year is important: this is not 365 days, but 365.25 - because leap years need to be factored in. (If you want proof of this, try dividing the number of days between Feb 28 1970 and Feb 27 2017 by 365)

## Pattern recognition

We've already used pattern recognition to break down the steps. Now you can try to find functions which achieve each abstraction:

1. A function that *returns* today's date
2. A function that extracts a year from a date
3. A function that rounds a number down to a whole number

Other challenges just require calculations: one number (a year, or number of days) minus another, or divided by another (days by 365.25, etc.), or compared to another (is this date greater than another).

## Algorithm

Next to encode those steps in a formula or piece of code...

## Different ways this has been done

Marion Urban's solution can be found [in this blog post](https://onlinejournalismblog.com/2014/11/19/how-to-find-out-the-ages-of-people-using-excel/).

A different approach is [noted by Ian Balboa](http://www.happy.co.uk/excel-hints-tips-calculating-age-from-date-of-birth/) involving a function that Excel *used* to have for calculating the difference between two dates: `DATEDIF`. "The bad news is that for some reason Microsoft no longer supports this function in Excel" but the `DATEDIF` function *will* work in Excel (the software just won't suggest it, or help you write it very much). The `DATEDIF` function is much better supported in Google's own spreadsheets tool, [Google Sheets](http://sheets.google.com), however.

Yet another method for calculating ages comes from journalism professor Steve Doig, who uses the following formula:

`=(DATE(2014,4,24)-B2)/365.25`

## The Guantanamo data

The data mentioned above has six fields (columns): a simple index number, most likely added by the creator of the sheet; a date of birth; a name; an 'ISN' code (you'd have to find out what this means); citizenship details; and their place of birth.

1. Firstly, check that the date of birth is being treated as a number by Excel. How would you do this?

2. Insert a new column between current columns B and C which gives us the age of each individual based on their date of birth. What formula will you use? Do you need to use more than one column?

3. What sort of error checking might you need - whether in the sheet itself or through follow up phonecalls?

4. Now that you have their ages what stories might you tell about those?
