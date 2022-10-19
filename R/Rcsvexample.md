# Working with MPs' expenses to demonstrate R


This notebook takes you through working with expenses data. First, [download the latest MPs' expenses from IPSA](http://www.theipsa.org.uk/mp-costs/other-published-data/) - *make sure you select Individual Claims* to get the granular data.

## Import data

Now to read that CSV file into an object we can work with in R. Note: the CSV must be in the same folder as your R project.

```{r}
expenses1718 <- read.csv("Individual_claims_for_17_18.csv")
```

## Generate a summary

We can summarise the whole dataset like this:

```{r}
summary(expenses1718)
```

Note how numerical columns are summarised differently to text columns. We can get a summary of just one column like this:

```{r}
summary(expenses1718$Category)
```

Or a numerical one:

```{r}
summary(expenses1718$Amount.Claimed)
```

## Join data

[Download another year's data from IPSA](http://www.theipsa.org.uk/mp-costs/other-published-data/) - remember again to select *Individual Claims*.

Bring it into R in the same way:

```{r}
expenses1617 <- read.csv("Individual_claims_for_16_17.csv")
```

Because we want to add new *rows* with this join, we use `rbind` like so:

```{r}
expenses16to18 <- rbind(expenses1617,expenses1718)
```

## Export the results

That might be all we want to do, then export so we can work with it in Excel.

```{r}
write.csv(expenses16to18, "expenses2016to2017.csv")
```

## Create a subset

Now let's filter this to an MP from one constituency:

```{r}
expensesedgbaston <- subset(expenses16to18, expenses16to18$MP.s.Name == "Stephen Kinnock")
```

## Ask a question

You can ask all sorts of questions...

```{r}
totalexpensesclaimed <- sum(expenses16to18$Amount.Claimed)
totalexpensesclaimed
biggestexpenseclaimed <- max(expenses16to18$Amount.Claimed)
biggestexpenseclaimed
```

## Generate new data

We can also create a new column based on other columns. For example we could calculate a difference:

```{r}
expenses16to18$claimdifference <- expenses16to18$Amount.Claimed - expenses16to18$Amount.Paid
#Let's see what the biggest difference was
max(expenses16to18$claimdifference)
```
Likewise we could extract parts of data by using a text function like `substring`:

```{r}
#substring needs 3 ingredients: 
#a text object, a starting position to start grabbing characters from, and an end position
#The first two characters of each date is the day; the third character is a slash, and the 4th and 5th characters are used to indicate the month, so that's what we want
expenses16to18$month <- substring(expenses16to18$Date,4,5)
#Show the different entries in that new field
table(expenses16to18$month)
```

Another type of new data might be *categorisation*. For example performing a test will generate a series of TRUE/FALSE values:

```{r}
expenses16to18$above10k <- expenses16to18$Amount.Claimed > 10000
#See a table counting occurrences of each value in the field
table(expenses16to18$above10k)
```

Calculations can be used instead of raw numbers, for example:

```{r}
expenses16to18$aboveaverage <- expenses16to18$Amount.Claimed > mean(expenses16to18$Amount.Claimed)
#Note that 'average' doesn't mean halfway
table(expenses16to18$aboveaverage)
```

```{r}
#Only 17% of claims are 'above average'
32101/(156703+32101)
```

## Visualising 

We can use the `ggplot2` library to visualise data in different ways. First we need to initialise it:

```{r}
#ggplot2 should already be installed, but if you get a message that it isn't, uncomment this next line and run that first
#install.packages("ggplot2")
#Initialise the library
library(ggplot2)
```

Then this code generates a histogram:

```{r}
#use the ggplot function with our dataset
ggplot(expenses16to18) +
  geom_histogram(aes(x=Amount.Claimed), #specify a histogram, and the column Amount.Claimed
                 binwidth=1000, #specify how wide each 'bin' (column) is
                 fill="blue") #specify a fill colour
```

The code to generate a density plot is similar:

```{r}
#library(scales) #this allows us to add dollars to the numbers
#use the ggplot function with our dataset
ggplot(expenses16to18) +
  geom_density(aes(x=Amount.Claimed)) #specify a histogram, and the column Amount.Claimed
```


And for a column chart:

```{r}
#use the ggplot function with our dataset
ggplot(expenses16to18) +
  geom_bar(aes(x=Category)) #this needs to be a category, and entries will be counted
```


We can flip the axes by adding `+ coord_flip()` if we have a lot of categories and want a bar chart from the side - although with 650 categories it will still be difficult to read:

```{r}
#use the ggplot function with our dataset
ggplot(expenses16to18) +
  geom_bar(aes(x=MP.s.Constituency)) + coord_flip()

```


So we can add `theme` with arguments to specify the style:

```{r}
#use the ggplot function with our dataset
ggplot(expenses16to18) +
  geom_bar(aes(x=MP.s.Constituency)) + coord_flip() + theme(axis.text.y = element_text(size=rel(0.8)))
```



Let's try something else:

```{r}
#use the ggplot function with our dataset
ggplot(expenses16to18) +
  geom_bar(aes(x=MP.s.Constituency)) + coord_flip() + theme(axis.text.y = element_text(size=rel(0.8)))
```



