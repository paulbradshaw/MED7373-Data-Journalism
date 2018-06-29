# SQL for journalists - Crina Boros

Download [DB Browser for SQLite](https://sqlitebrowser.org/) or [SQLite Database Browser New](https://sourceforge.net/projects/sqlitedbrowser/?source=typ_redirect).

To deal with larger datasets you could also try [Microsoft SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017).

Unlike Excel SQL analysis does not change the tables.

## Key commands and order:

```
SELECT
FROM
  JOIN ... ON
WHERE
GROUP BY
ORDER BY
HAVING
```

Any fields used in `SELECT` has to be used in `GROUP BY`

[Download Crina's data here](https://onedrive.live.com/?authkey=%21AHplD87l3Gj1AWY&id=9B67CCB99AFAEA95%21402728&cid=9B67CCB99AFAEA95)

## Start in DB Browser for SQLite

Click on *New Database*

A new window will appear marked *Edit table definition* - just **Cancel** this (this is for creating an empty table).

Click on *File > Import > Table from CSV file...* and select the CSV file you want to bring in as a table. Choose Dams.csv.

A new window *Import CSV file* will appear providing some options to customise how it is imported. For example, if your first row contains column names make sure you tick *Column names in first line*.

Click **OK**.

Switch to the *Execute SQL* tab across the top.

## Basic command to select all data

Type a basic command to show all records:

```
SELECT *
FROM Dams
/* Notes! */
```

Commands (e.g. `SELECT`) are not case sensitive, but table names are. Columns (fields) need to use quotations and commas.

Notes can be put inside `/*  */`, like HTML

You can run a single line by selecting it and pressing Enter.

The hazard field refers to the population near the dam, not dam safety - *never assume you know anything about the data: make sure you understand it*.

## Pivot table

Use `GROUP BY` to pivot. Curiously, DB Browser returns different results when using *single* quotes rather than *double* quotes - so if you only get a single result, try a different type of quotation mark:

```
/* show names */
SELECT "DAM_NAME"
FROM Dams
GROUP BY "DAM_NAME"
```

Or:

```
/* show types of owner */
SELECT "OWN_TYPE"
FROM Dams
GROUP BY "OWN_TYPE"
```

Add counts:

```
SELECT count(*), "OWN_TYPE"
FROM Dams
GROUP BY "OWN_TYPE"
```

Sort:

```
SELECT count(*), "OWN_TYPE"
FROM Dams
GROUP BY "OWN_TYPE"
ORDER BY count(*) DESC
```

We add `DESC` because it will default to ascending order (A-Z or small-to-large) otherwise.

You can also order based on column number:

```
SELECT count(*), "OWN_TYPE"
FROM Dams
GROUP BY "OWN_TYPE"
ORDER BY 1 DESC
```

## Using `DISTINCT`

You can use `DISTINCT` to [remove duplicates from the results](https://www.techonthenet.com/sql/distinct.php) - it can also be used to show unique values.

`SELECT DISTINCT (OWN_TYPE) FROM Dams`


## A more complex query

You can [see more about this story here](https://ire.org/resource-center/stories/24767/):

> "A Tennessee law allows old watershed dams to be downgraded to farm ponds from high-hazard dams, exempting them from state safety inspections. The reporter discovered 13 of these dams were downgraded in 2008. The lack of oversight poses serious consequences because fatalities are likely to occur should one of the dams fail."

Looking for privately owned damns where the hazard was high, show 4 fields:

```
SELECT "HAZARD", "YEAR_COMPL", "INSP_DATE", "DAM_NAME"
FROM Dams
WHERE "OWN_TYPE" != "PRIVATE" AND "HAZARD" = "HIGH"
GROUP BY "HAZARD", "YEAR_COMPL", "INSP_DATE", "DAM_NAME"
ORDER BY 2
```

## Importing multiple tables

Click on *File > Import > Table from CSV file...* and select the CSV files you want to bring in as a table. Choose the two files TennGive.csv (donations) and TnnCand.csv (candidates).

This time make sure you tick the box to treat them as *Separate tables*.

Scope it:

```
SELECT *
FROM TennGive
```

And:

```
SELECT *
FROM TnnCand
```

Let's count how many names there are in each district:

```
SELECT "DISTRICT", count("NAME")
FROM TnnCand
GROUP BY "DISTRICT"
```

Let's add state, and order:

```
SELECT "STATE", "DISTRICT", count("NAME")
FROM TnnCand
GROUP BY "STATE", "DISTRICT"
ORDER BY 3 DESC
```

How about finding out how many candidates each party has?

```
SELECT "PARTY1", count("NAME")
FROM TnnCand
GROUP BY "PARTY1"
ORDER BY 2 DESC
```

And adding a breakdown by year:

```
SELECT "PARTY1", count("NAME"), "ELECTYEAR"
FROM TnnCand
GROUP BY "PARTY1", "ELECTYEAR"
ORDER BY 2 DESC
```


What questions can we ask without joining?

* Which candidate got money from the largest number of donors?
* Types of occupations and donations?
* Multiple donation donors - top 3
* Largest donor?
* Total donations?
* What's biggest single donation?

Start with the last one:

```
SELECT "AMOUNT", MAX("AMOUNT")
FROM TennGive
```

Or:

```
SELECT "AMOUNT"
FROM TennGive
ORDER BY "AMOUNT" DESC
```

But note: these figures are *TEXT* - it only comes to because it starts with a 9. The biggest donation is $2,000 but there is no way in DB Browser to change to a number here (even `CAST` doesn't seem to work in this case).

Strangely, `SUM` does seem to work:

```
SELECT  "LAST", SUM("AMOUNT")
FROM TennGive
GROUP BY "LAST"
ORDER BY 2 DESC
```

Could you use `SUM` and a unique value to sort the maximum values?

Also try:

```
SELECT "AMOUNT"
FROM TennGive
ORDER BY "AMOUNT"
```

There are negative numbers: this indicates a donation has been refused.

* Types of occupations and donations?

```
SELECT "OCCUPATION", count(*)
FROM TennGive
GROUP BY "OCCUPATION"
ORDER BY 2 DESC
```

Example: [The Real ‘Housewives’ Of HSBC](https://www.icij.org/investigations/swiss-leaks/real-housewives-hsbc/)

* Largest donor?

```
SELECT "LAST", "REST", "OCCUPATION"
FROM TennGive
WHERE "LAST" = "HASLAM"
GROUP BY "LAST", "REST", "OCCUPATION"
```
### Wildcards and `OR`

Let's adapt the query to broaden it to names containing 'HAS':

```
SELECT "LAST", "REST", "OCCUPATION"
FROM TennGive
WHERE "LAST" LIKE "%HAS%" OR "REST" LIKE "%HAS%"
GROUP BY "LAST", "REST", "OCCUPATION"
```

### Cleaning data: `TRIM` and data types

To change the data type for a particular field, switch to the *Database Structure* tab and right-click on the table name.

Select **Modify table**.

A window should appear where you can change the type of each field using drop down menus.

You can also clean a little with `TRIM`:

```
SELECT TRIM("AMOUNT")
FROM TennGive
ORDER BY "AMOUNT"
```


## Joining data tables

Example: [How Florida ignited the heroin epidemic](https://www.ire.org/blog/extra-extra/2018/06/29/how-florida-ignited-heroin-epidemic/)

You join in the `FROM` command by adding `JOIN` after the first table, then `ON` to specify the fields you are matching on.

`FROM TnnCand JOIN TennGive ON TnnCand."ID" = TennGive."CAND_ID"`

Questions that need a join:

* Who are the Haslams sponsoring?
* Which candidate gets most money?

Note that we now need to include the table name in the fields that we request:

```
SELECT TnnCand."NAME", SUM(TennGive."AMOUNT")
FROM TnnCand JOIN TennGive
	ON TnnCand."ID" = TennGive."CAND_ID"
GROUP BY "NAME"
ORDER BY 2 desc
```

We can expand further (note you don't need quotation marks on the field names if they don't have spaces):

```
SELECT TnnCand."NAME", SUM(TennGive."AMOUNT"), TnnCand.PARTY1, TennGive.LAST
FROM TnnCand JOIN TennGive
	ON TnnCand."ID" = TennGive."CAND_ID"
  WHERE "NAME" LIKE "%Sasser%"
	GROUP BY "NAME", TnnCand.PARTY1, "LAST"
ORDER BY 2 desc
```

### Combining tables that have same fields but different periods or areas: `UNION`

If you have data from two different periods you can use `UNION ALL` to combine them like so:

```
(
    SELECT police_force_area, sex, year_of_appearance from crimjustice2016only
    UNION ALL
    SELECT police_force_area, sex, year_of_appearance from crimjustice2017only
)
```

Any `GROUP BY` commands need to be used *either side* of the `UNION`

```
(
    SELECT count(sex), sex, year_of_appearance from crimjustice2016only
    GROUP BY sex, year_of_appearance
    UNION ALL
    SELECT count(sex), sex, year_of_appearance from crimjustice2017only
    GROUP BY sex, year_of_appearance
)
```
