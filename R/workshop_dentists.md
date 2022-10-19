# 10 things to do with R first: dentists example

This notebook walks through the process of starting to use R, using an example of looking at data on dentists in the UK. That [data can be found by following the link to the latest data on this page](https://digital.nhs.uk/data-and-information/publications/statistical/nhs-dental-statistics).

This data was used for a [BBC Shared Data Unit story on dentists](https://github.com/BBC-Data-Unit/NHS_dentists) which you can use as the basis for a new story! (Or pick a different dimension of the data)

We are following the steps in [10 things to do with R first](https://github.com/paulbradshaw/Rintro/blob/master/10thingstodofirst.md). The first two are:

1. Install R [on your PC](https://cran.r-project.org/bin/windows/base/) [or Mac](https://cran.r-project.org/bin/macosx/) first. Then [download RStudio from here](https://www.rstudio.com/products/rstudio/download/).
2. Open RStudio and create a new project. click on **File > New project...**. You can select a directory you've created for the project ('existing directory') or create a new one if you forgot ('new directory'). Either way, it's important to have a folder for each project.

Now for the next steps...

## 3. Import and store data: a CSV of dentist data

Make sure you have downloaded the CSV called 'Annex 3: Workforce Joiners and Leavers' and **placed it in the same folder as your project**.

Here is a code block with the code to import that CSV into a variable that we have called `joinersleavers`:

```{r download csv from url}
joinersleavers <- read.csv('NHS Dental Statistics for England 2021-22 Annex 3_Workforce Joiners Leavers csv.csv', stringsAsFactors = F)
```

That variable will be a **data frame** because that's the type of variable that `read.csv()` always creates. It is a type of variable we can perform analysis with. 

We can show the data frame by simply typing its name in a code block and 'playing' that block of code (each code block in a notebook has a play button in its upper right corner):

```{r show joinersleavers}
joinersleavers
```

It won't show all 18,156 rows - just the first 10, along with buttons to move through the next 10. 

Likewise it won't show all 10 columns - just those that fit, with an arrow to allow you to scroll right through the others. 


## 4. Generate summary statistics

To summarise an entire data frame, put its name in brackets after `summary()`:

```{r summarise data frame}
summary(joinersleavers)
```

### Generate summary statistics for one column

You can also summarise a single column. To specify a particular column type the data frame name, then a dollar sign and then the name of a column. Make sure there's no spaces in any of this:

```{r summary one column}
summary(joinersleavers$Dentist_Count)
```

We could now go on to create a pivot table of this data within R - [details on how to do that are here](https://github.com/paulbradshaw/Rintro/blob/master/10excelthings.md) and I'd recommend exploring these independently - but I'm going to explore some other more basic processes first.

Let's look at the data again - it has a couple of columns that refer to codes:

```{r show joiners data}
joinersleavers
```

It's always useful to look for a **data dictionary** on the page or website where you got the data from. [Here's the data dictionary for the dentist data](https://digital.nhs.uk/data-and-information/publications/statistical/nhs-dental-statistics/2021-22-annual-report/data-dictionary-2021-22). It tells us that:

The column 'Org_Code', it says, refers to "NHS England Sub Integrated Care Board Location (SICBL) Code"

If we search around for those codes we might find [this NHS page](https://www.nhsbsa.nhs.uk/sicbls-icbs-and-other-providers/organisation-and-prescriber-changes/sub-icb-locations) with a spreadsheet of codes and the names of the boards they refer to.

We can import that data in order to combine it with our first data frame.

### Importing an XLSX file with `readxl`

This data is in Excel format, however. So we will need to use a **package** to help us do that. (More on this in the ['10 more things to do in R'](https://github.com/paulbradshaw/Rintro/blob/master/10morethings.md) tips)

```{r import excel file}
#activate the readxl library
library(readxl)
#import the xlsx file into a variable - choose the first sheet
codeslookup <- readxl::read_excel('Website Names Lookup.xlsx')
#show the resulting variable
codeslookup
```

### Problem-solving: cleaning up the headings

We can see that the headings aren't quite right. Let's look closer by using the `colnames()` function to show the column names in a data frame.

```{r show column names}
colnames(codeslookup)
```

This is because the Excel file has the headings in row 4 (we can see by opening it in Excel).

We can also see that the spreadsheet has two sheets - and we actually want the second one. 

We can change our import code to specify this, by adding two extra *arguments*, or ingredients: `sheet =` and `skip = `

```{r re-import excel file}
#no need to activate the readxl library again
#import the xlsx file into a variable - choose the first sheet
codeslookup <- readxl::read_excel('Website Names Lookup.xlsx', sheet = 2, skip = 3)
#show the resulting variable
codeslookup
```
## 5. Join data with `merge()`

Now that we have the data cleaned up, we can merge it with the other data on those codes.

We do that with `merge()`. This needs a few ingredients: the names of the two data frames being merged (which we specify with `x =` and `y = `), and the names of the two columns that we want to use as the basis for matching them up (which we specify with `by.x = ` and `by.y = `).

Here's the code:

```{r merge on codes}
#merge the data and store in a variable called mergeddata
mergeddata <- merge(x = joinersleavers, y = codeslookup, by.x = 'Org_Code', by.y = 'Sub ICB Location ODS Code')
#show that
mergeddata 
```

### Problem-solving: missing rows

When merging pay attention to the size of the data frame before merging, and after.

```{r count rows in both datasets}
#count the number of rows in each data frame - and print the result
print(nrow(joinersleavers))
print(nrow(mergeddata))
```

We seem to have lost 5,000 rows along the way. Why? Well, by default `merge()` will only keep rows where there is a match. 

Our original data had lots of rows with no Org Code, so those have been removed.

If we want to stop that happening, we need to add another ingredient to the `merge()` function: `all.x = TRUE`. This specifies that we want to keep all of the rows from the 'x' dataframe (the one specified with `x = `).

```{r merge on codes}
#merge the data and store in a variable called mergeddata
mergeddata <- merge(x = joinersleavers, y = codeslookup, by.x = 'Org_Code', by.y = 'Sub ICB Location ODS Code', all.x = TRUE)
#show that
mergeddata 
```
Of course we may not want to do that: if we wanted to filter to those organisations only, this would be a good way to do that. 


## Export the data

Now that we've merged the two datasets we can export them. To do that we need to specify two ingredients: the name of the dataframe we want to export, and the name of the file we want to create. The name needs to be a *string* inside quotes.

We can call the CSV whatever we want, but make sure it ends in '.csv' so that it will be recognised as a spreadsheet file.

```{r export joiners with codes}
write.csv(mergeddata, "joinersleavers.csv")
```


## Another story: importing data directly from a URL

Let's look at another dataset from the same page: **Annex 3 (Activity)**. This is a big dataset - 149 MB - so perfect for working with in R as it may be tricky to deal with in Excel. 

It's also a good example to demonstrate a different way of importing data.

In some cases you will be able to read a CSV into RStudio without even downloading it - as long as it's online and the URL ends in .csv. 

You'll need to copy the URL *of the CSV* (note: *not* the URL of the webpage). 

To do this, right-click on the link and select 'Copy link'. Then paste the link into your code in RStudio where you import data (see below). 

Check that it ends in .csv - if it doesn't then it might be a redirection URL and it may not work. If it doesn't, just download it instead and import it that way instead.

Here's the code for that data:

```{r download csv from url}
activity2122 <- read.csv('https://files.digital.nhs.uk/EF/9430DB/nhs-dent-stat-eng-21-22-anx3-act.csv', stringsAsFactors = F)
```

You can tell by the time it takes that this is a big file. But eventually it should appear in the environment in the upper right corner of RStudio.

Let's summarise it too:

```{r summarise activity data}
summary(activity2122)
```

Some of these columns may need explanation. It's always useful to look for a **data dictionary** on the page or website where you got the data from. [Here's the data dictionary for the dentist data](https://digital.nhs.uk/data-and-information/publications/statistical/nhs-dental-statistics/2021-22-annual-report/data-dictionary-2021-22). It tells us that:

* COT is "Counts of courses of treatment"
* UDA is "Counts of units of dental activity"

You could google those phrases to find out more. For example a search for the latter phrase brings up a document from NHS England that explains: 

> "Units of Dental Activity (UDAs) are a measure of the amount of work done during dental treatment. More complex dental treatments count for more UDAs than simpler ones. For example, an examination is 1 UDA, fillings are 3 UDAs, and dentures are 12 UDAs"

## Seeing what unique values are in a column: `table()`

Another useful function for getting an overview of a column is `table()`: this is a sort of simple pivot table that tells you how many entries there are for each value in a column. 

We can use this to get an idea of the time frame covered by the data, as indicated by the column 'ACTIVITY_END_DATE':

```{r table end date}
table(activity2122$ACTIVITY_END_DATE)
```

We can see that there are four dates used in the data, with a roughly similar number of entries under each.

These dates might seem odd at first, but the more experience you get with data the more you'll start to see the same patterns appear. 

In this case what we are looking at is the end of each financial **quarter** of the year:

* April to June
* July to September
* October to December
* January to March

So the data is divided into quarters. 

Again, the data dictionary would have helped here, describing this column as "Date in which end of period covered falls, end date of each quarter"

Now we don't want just one year, so we're going to need to import more data to join together.

## Joining data horizontally from different periods: `rbind()`

To get the previous year's data we will need to find that on the [NHS Dental Statistics page](https://digital.nhs.uk/data-and-information/publications/statistical/nhs-dental-statistics/2020-21-annual-report)

This time it's in a zip file so we'll need to download it and unzip it first. (There are ways to import directly from zip files, but we won't get distracted by that here)

Once you've unzipped the CSV file, make sure it's in the same folder as your project, and import it like you did before with code like this:

```{r import activity for previous year}
activity2021 <- read.csv('nhs-dent-stat-eng-20-21-anx3-act.csv', stringsAsFactors = F)
```

Now you should have two data frames, one for each year.

We can combine those into one long data frame by using `rbind()`. To do that you specify the names of all the dataframes you want to combine, inside the brackets.

But we will get an error here:

```{r rbind}
activity_allyears <- rbind(activity2021, activity2122)
```

### Problem solving: different column names

The error message gives us a clue to the cause: the column names don't match.

We can use the function `colnames()` to show the column names for a dataframe.

Because we're trying to show the results of two different functions, we'll use a `print()` function too, otherwise only the last one will show.

```{r print colnames} 
#fetch the column names from each dataframe and print them
print(colnames(activity2021))
print(colnames(activity2122))
```

You'll need to look closely to see the difference: in one data frame column 4 is called CCG_CODE and in the other it's SUB_ICB_CODE. Similar differences can be seen in the next two column names too.

The result of using `colnames()` is a vector - a type of list. We can access an individual item in that vector by putting square brackets after it, with the number of an item's position inside those, like this:

```{r print colname 4} 
#show the fourth item in that vector of column names
colnames(activity2021)[4]
```

Let's do the same with the other column names:

```{r show 4th column of other data}
colnames(activity2122)[4]
```

Not only can we *show* the column name at that position (4th) but we can *change* it too.

```{r change column names}
#change the 4th column name in each data frame
colnames(activity2021)[4] <- 'CCG_or_SUBICB_CODE'
colnames(activity2122)[4] <- 'CCG_or_SUBICB_CODE'

#fetch the column names from each dataframe and print them
print(colnames(activity2021))
print(colnames(activity2122))
```

And we can repeat that for the other problematic columns too.

```{r change other column names}
#change the 5th column name in each data frame
colnames(activity2021)[5] <- 'CCG_or_SUBICB_ONS_CODE'
colnames(activity2122)[5] <- 'CCG_or_SUBICB_ONS_CODE'
#change the 6th column name in each data frame
colnames(activity2021)[6] <- 'CCG_or_SUBICB_NAME'
colnames(activity2122)[6] <- 'CCG_or_SUBICB_NAME'

#fetch the column names from each dataframe and print them
print(colnames(activity2021))
print(colnames(activity2122))
```

Now with those columns cleaned up to be consistently named, let's try that `rbind()` code again.

```{r rbind attempt 2}
activity_allyears <- rbind(activity2021, activity2122)
```

## Export merged data

And we can export the results

```{r export activity all years}
write.csv(activity_allyears, "activity_allyears.csv")
```

