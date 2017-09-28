# Data journalism's 3 chords

Here's a quick activity to get to grips with data journalism's '3 chords': sorting, filtering, and calculating percentages (change and proportions). 

With just those 3 tools you can find and tell the most basic data journalism stories: who's top and bottom; what's changed; and what's of interest. And the good news is that two of them require no maths at all.

## Some data to play with

First, you'll need some data to try out these techniques. Here are 3 useful datasets I'll refer to:

* [Local authority spending above £500 (Birmingham)](https://data.birmingham.gov.uk/dataset/payments-to-suppliers-over-f500) (the most recent release is at the bottom)
* [Stop and search data](https://data.police.uk/data/) (tick *West Midlands* and *Include stop and search data*). There's a [GitHub repo for the data used in a story on Birmingham Eastside](https://github.com/Birmingham-Eastside/stop-and-search) which you can use too - this has totals for two months that can be compared.
* [European Investment Bank: projects financed database](http://www.eib.org/projects/loan/list/index.htm) (conduct a search and there will be a link to download the data)
* [Oscar winners](https://drive.google.com/file/d/0B5To6f5Yj1iJVGJTekloX0o1dG8/view) (click the download button in the upper right corner)

Each has its own qualities that are useful to talk through as you work with the data and consider stories.

## Upload and familiarise yourself with the data

Open one of the datasets in Excel, or in Google Sheets (make sure it's converted to a Google Sheet by uploading to Google Drive and then right-clicking and selecting *Open with > Google Sheets*).

First, take a look at the column headings. Think about what stories each of those pieces of information might provide. 

There might also be information that you don't quite understand - for example, what does 'Cost Centre' mean (in the local authority spending data)? And what do the codes in that column refer to? You may need to do some extra research (including phonecalls) to understand jargon, and you might need extra data to make sense of it (for example what codes refer to).

It's also useful to think about the type of data in each column. I want to highlight a few things in particular:

* **Numbers** will normally be right-aligned in Excel and Google Sheets
* **Text** will normally be left-aligned
* **Dates** *should* be stored as numbers - in other words, they should be right-aligned. The date that you see (for example "07/08/2017") is actually just the way the number is *formatted*. You can format a date in all sorts of ways, but the important thing to remember is that they can be sorted, and used in calculations (for example the number of days between dates). If what appears to be a date is actually left-aligned, and doesn't sort properly, then that means you have **DIRTY DATA!** and you'll need to come up with tricks if you want to work with that data in some way (the European Investment Bank data suffers from this problem).

The type of data dictates what you can do with it. For example, you can perform calculations with numbers (including dates), but not with text. However, you can *measure* text (its length), *test* it (whether it contains certain words), *filter and sort* it, and *extract* information from it, among other things.

Now you've got to grips with the data, let's dig into it.

## Sorting

![](http://pad3.whstatic.com/images/thumb/a/a7/Use-AutoFilter-in-MS-Excel-Step-4Bullet1.jpg/670px-Use-AutoFilter-in-MS-Excel-Step-4Bullet1.jpg)

Commonly when presented with data we want to know who or what comes top and bottom. We can do this quickly using the sorting buttons. 

1. First, select one of the cells in the column you want to sort. Don't worry about selecting the whole column - you only need to select one cell.
2. Next, go to the *Data* toolbar in Excel (see image above)
3. Now, click one of the *small* buttons with the A-Z icon - don't click the big A-Z button or you'll start the advanced sorting wizard, and you don't need that. Both those small buttons will sort your data by the column you are in - the top one will sort from smallest to largest (or A to Z, or oldest to newest), and the other one will sort from largest to smallest (or Z to A, or newest to oldest). 
4. Try both so you can see the smallest entries and the largest ones - and try it in other columns too.

That's it! The toolbar and the small buttons are the quickest way to sort - but you can also do a more powerful sort by clicking the large A-Z button or selecting the *Data* menu and then *Sort...* in Excel. This will bring up a wizard where you must specify which column to sort by, and which order to sort it in. In Google Sheets, there is no button: instead click the *Data* menu and then the relevant sort option, and click *OK* to apply your sort.

Simply sorting data in this way can give you a lead which you can follow up through a phonecall.

## Filtering

![](http://blog.contextures.com/wp-content/uploads/2012/05/autofilterribbon01.png)

Filtering can be done like this: 

1. First, select any of the cells in your data
2. Next, go to the *Data* toolbar in Excel 
3. Now, click the *large* Filter button with a funnel icon (don't click the small one or you'll start the advanced filter wizard). Alternatively (and in Google Sheets), you can click the *Data* menu and select *Filter* from there.

At the top of each column you should now be able to see a drop-down menu. If you click on any one of these the menu will allow you to filter the whole dataset to just show the rows with the value that you select. You can also use the search box to look for particular words, and the filter will only show entries where the column contains that word.

Note, by the way, that you can also use this filter box to *sort* the table by this column.

Different types of data can be filtered in different ways. Look, for example, at how the filter drop-down menu differs when you click on 3 different types of column:

* **Text column** filters will show you a list of all the values in the column, and a search box - but you can also use the *Choose one* drop-down menu above that to search for entries that 'begin with' or 'end with' particular strings of characters, 'contain' or 'does not contain' text and so on.
* **Numerical column** filters will also show a list of all the values - but this time the *Choose one* drop-down menu presents options like 'greater than', 'less than', 'does not equal', 'between' (certain numbers) and even 'Top 10', 'Bottom 10', and above or below average.
* **Date column** filters show a list of values which is *nested*: so for example years are at one level, the months within each year are slightly indented, and the dates within each month are then further indented still. This means that you can select or deselect a whole year without having to untick each month. The *Choose one* drop-down menu includes some of the numerical filter options like 'greater than', etc., but it also includes date-specific ones like 'Next week', 'Last week', 'This quarter' and so on.

Try using the filter to look for any companies with 'taxi' in the name, or 'consult' (note this will catch both consulting and consultants). 

## Calculating percentages

One of the most useful calculations you'll need to make is a percentage - and it's important to get it right. A percentage is always a part of a whole, and that's the best way to think of it:

`percentage=parts/whole`

In Excel you always begin a calculation with an equals sign, and either type the numbers directly like so...

`=1/10`

...Or use cell references, like so (the letter refers to the column, and the number to the row, so `A1` means the cell in the first column, first row, and `B1` means the cell in the second column, first row):

`=A1/B1`

...Or a combination of both:

`=A1/35`

Anything beginning with an equals sign like this is called a **formula**

When you press enter you will get a result in the same cell as you typed the formula. This will normally be a decimal, like `0.5` or `0.364`. 

That decimal is Excel's basic way of expressing a percentage. `0.5`, for example, means 50%, and `0.364` means 36.4%. This makes sense: after all, `1` is 'whole' - it is 100%. But split 1 in half (50%) and you get `0.5`.

If you want to convert your decimal to *look* like a percentage there's a very easy way to do so in Excel: the *percentage* button. This is in Excel's *Home* menu and is the button with a percentage symbol on it. Just select the cell or cells containing the numbers you want to format as percentages, and click that button. (Another way to get the same effect is to go to *Format > Cells* and select the *Percentage* option from the window that appears)

One thing to watch for when calculating percentages and proportions: check the column heading for any indication that the numbers shown actually represent thousands or millions. If the heading has something like `(000)` then you'll need to multiply all numbers in that column by 1000 to get the real number(s) that you should be using.

*Tip: if you need to add up all the values in a column select them all and click the Autosum button, which is a Greek E, or Sigma, icon. A total should appear at the bottom of that column.*


### Calculating change

Change is a particular type of percentage which needs further explanation. Remember that when reporting percentage change you are talking about change *from its starting position* - so that's the figure you should be dividing by. Here's a concrete example:

Let's say the number of crimes in 2016 was 200, and in 2017 it was 250. First we need to calculate the increase: new figure minus old figure. That's an increase of 50 crimes - but what is that as a *percentage* increase?

If we divide 50 by the 2016 figure of 200 we would get `0.25`, or a 25% increase. But if we divided 50 by the 2017 figure of 250, the result is `0.2`, or a 20% increase.

Of course the increase is *from* 2016, so we should be dividing by the earlier figure. In 2016 there were 200 crimes; it increased by a quarter of those crimes: 50, making 250 crimes in total.

As a formula it might look something like this:

`=(new minus old)/old`

But we need to replace those words with actual numbers or cell references like so:

`=(250-200)/200`

Or so:

`=(B2-A2)/A2`



## Data context: sense-checking

I said that each dataset had its own qualities. Here are some key points:

* The local authority data and stop and search is only one month. Remember that data like this may suffer from *seasonal variation*. For example, spending in April will be skewed by the fact that it is at the end of the financial year and some bills will only be settled in that month. Certain types of crime may increase at certain times of the year. Try to compare year-on-year rather than month-on-month to get a better comparison.

* The European Investment Bank data covers a long period of time, so loans made early in the time period will not be worth the same as loans of the same amount made later. In other words, you need to *account for inflation* if making long term comparisons.
