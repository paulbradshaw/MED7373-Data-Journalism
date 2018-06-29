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

Click on *File > Import > Table from CSV file...* and select the CSV file you want to bring in as a table.

A new window *Import CSV file* will appear providing some options to customise how it is imported. For example, if your first row contains column names make sure you tick *Column names in first line*.

Click **OK**.

Switch to the *Execute SQL* tab across the top.

Type a basic command to show all records:

```
SELECT *
FROM Dams
/* Notes! */
```

Commands (e.g. `SELECT`) are not case sensitive, but table names are. Columns (fields) need to use quotations and commas.

Notes can be put inside `/*  */`, like HTML

The hazard field refers to the population near the dam, not dam safety - *never assume you know anything about the data: make sure you understand it*. 
