# SQL

This folder contains resources on using SQL queries in data journalism.

* I have written a [guide to SQL for journalists here](https://docs.google.com/document/d/e/2PACX-1vQQzSM5scsn2wjrL02o-rf9gHaiBQ2GcGoc2QBAXPxq12cKGtH6jFrGVmUt_rUfqtmo41Gq4J1luzkE/pub)
* I have written [this guide to SQL queries in Carto](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/sql/cartosql.md) too
* Codecademy [has a SQL course](https://www.codecademy.com/learn/learn-sql)
* [SQL Teaching](https://www.sqlteaching.com/) allows you to learn about different commands and try them out
* [A Gentle Introduction to SQL Using SQLite](https://github.com/tthibo/SQL-Tutorial#readme) by AP's Troy Thibodeaux


## Places you can use SQL

You can use SQL queries in a range of contexts, including:

* In **Google Sheets** you can query ranges of cells [using the function QUERY](https://www.sheetgo.com/query-formula-google-sheets/)
* **Carto**: it is possible to generate maps based on SQL queries of datasets (look for the SQL toggle switch at the bottom of the data view - older tutorials will show it in a different place), and [to query data stored in Carto using their API](https://carto.com/docs/carto-engine/sql-api/making-calls/). [Here, for example, is a URL which queries one of my public datasets](https://paulbradshawbcu.carto.com/api/v2/sql?q=SELECT%20outcome,object_of_search%20FROM%20table_2017_09_west_midlands_stop_and_search%20limit%2010) - the query is at the end of the url after `q=` with `%20` for spaces.
* Scrapers in [Quickcode](https://quickcode.io/) (formerly Scraperwiki): once a scraper is running you can run SQL queries on that data, and query the JSON API using SQL queries
* Data.world is a service for hosting and sharing data - and you can query that data using SQL. They have [a series of tutorials to help](https://docs.data.world/tutorials/dwsql/#sql-on-dataworld)
* Within **R** you can use SQL queries with the package `sqldf`. The [documentation](https://cran.r-project.org/web/packages/sqldf/sqldf.pdf) states "The sqldf() or read.csv.sql() functions can also be used to read filtered files into R *even if the original files are larger than R itself can handle*" (my emphasis). You can find an R notebook with guidance on how to use the sqldf package in this folder.
* **Databases**: [Franchise](https://franchise.cloud/app/) allows you to run SQL queries on databases from within the browser. It supports a number of different SQL databases including SQLite, PostgreSQL, and MySQL.
* The Firefox extension [SQLite Manager](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/) allows you to create a SQLite database on your own computer and query it using the browser.
* The tool [Sequel Pro](http://www.sequelpro.com/) allows you to connect to and query MySQL databases. You'll also need to install MySQL. [Read the installation guide first](https://sequelpro.com/docs/ref/mysql/install-on-osx)
* Google Cloud Platform allows you to query a MySQL database - [documentation here](https://cloud.google.com/sql/docs/mysql/quickstart) and [for postgreSQL here](https://cloud.google.com/sql/docs/postgres/). Google BigQuery, which handles larger datasets, also [allows SQL queries](https://cloud.google.com/bigquery/quickstart-web-ui#load_data_into_a_table)
