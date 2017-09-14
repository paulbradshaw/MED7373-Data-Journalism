# Data journalism's 3 chords

Here's a quick activity to get to grips with data journalism's '3 chords': sorting, filtering, and calculating percentages (change and proportions).

With just those 3 tools you can find and tell the most basic data journalism stories: who's top and bottom; what's changed; and what's of interest.

## Some data to play with

First, you'll need some data to try out these techniques. Here are 3 useful datasets I'll refer to:

* [Local authority spending above £500 (Birmingham)](https://data.birmingham.gov.uk/dataset/payments-to-suppliers-over-f500) (the most recent release is at the bottom)
* [Stop and search data](https://data.police.uk/data/) (tick *West Midlands* and *Include stop and search data*)
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
* **Dates** *should* be stored as numbers - in other words, they should be right-aligned. The date that you see (for example "07/08/2017") is actually just the way the number is *formatted*. You can format a date in all sorts of ways, but the important thing to remember is that they can be sorted, and used in calculations (for example the number of days between dates). If what appears to be a date is actually left-aligned, and doesn't sort properly, then that means you have **DIRTY DATA!** and you'll need to come up with tricks if you want to work with that data in some way.

The type of data dictates what you can do with it. For example, you can perform calculations with numbers (including dates), but not with text. However, you can *measure* text (its length), *test* it (whether it contains certain words), *filter and sort* it, and *extract* information from it, among other things.

Now you've got to grips with the data, let's dig into it.

## Sorting

Commonly when presented with data we want to know who or what comes top and bottom. We can do this quickly using the sorting buttons. 

1. First, select one of the cells in the column you want to sort. Don't worry about selecting the whole column - you only need to select one cell.
2. Next, go to the *Data* toolbar in Excel 
3. Now, click one of the *small* buttons with the A-Z icon - don't click the big A-Z button or you'll start the advanced sorting wizard, and you don't need that. Both those small buttons will sort your data by the column you are in - the top one will sort from smallest to largest (or A to Z, or oldest to newest), and the other one will sort from largest to smallest (or Z to A, or newest to oldest). 
4. Try both so you can see the smallest entries and the largest ones - and try it in other columns too.

That's it! The toolbar and the small buttons are the quickest way to sort - but you can also do a more powerful sort by clicking the large A-Z button or selecting the *Data* menu and then *Sort...* in Excel. This will bring up a wizard where you must specify which column to sort by, and which order to sort it in. In Google Sheets, there is no button: instead click the *Data* menu and then the relevant sort option.

## Filtering

## Calculating percentages


## Data context: sense-checking

I said that each dataset had its own qualities. Here are some key points:

* The local authority data and stop and search is only one month. Remember that data like this may suffer from *seasonal variation*. For example, spending in April will be skewed by the fact that it is at the end of the financial year and some bills will only be settled in that month. Certain types of crime may increase at certain times of the year. Try to compare year-on-year rather than month-on-month to get a better comparison.

* The European Investment Bank data covers a long period of time, so loans made early in the time period will not be worth the same as loans of the same amount made later. In other words, you need to *account for inflation* if making long term comparisons.
