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
