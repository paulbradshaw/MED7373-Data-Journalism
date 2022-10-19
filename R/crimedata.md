# Getting started - crime data

First we need to get the data from 2 CSV files into this R project.

```{r}
#import the data from CSVs in this folder
warks0818 <- read.csv("2018-08-warwickshire-street.csv", stringsAsFactors = FALSE)
wm0818 <- read.csv("2018-08-west-midlands-street.csv", stringsAsFactors = FALSE)
```

Check out the headings:

```{r}
colnames(warks0818)
```

And the first few rows:

```{r}
head(warks0818)
```


Now let's merge the two datasets:

```{r}
#rbind will merge the rows of multiple datasets
both0818 <- rbind(wm0818,warks0818)
```

Get a brief overview using 'table':

```{r}
table(both0818$Reported.by)
```

```{r}
table(both0818$Crime.type)
```

Create a subset:

```{r}
burglary <- subset(both0818,both0818$Crime.type == "Burglary")
```

