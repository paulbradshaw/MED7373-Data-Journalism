# Asking questions (or allowing users to), SQL-style: `QUERY`

*This is an extract from [Finding Stories in Spreadsheets](https://leanpub.com/spreadsheetstories)*

One of the most useful functions only available in Google Sheets is `QUERY`. If you've ever used Structured Query Language (SQL) then `QUERY` will be very familiar to you: it allows you to form questions of your data like: '*Select all the lines in this data where the first name is Alice and the age is over 25* or: *Group all the data by city, and count how many entries there are in each*'.

If you *haven't* used SQL then you may be excused for thinking "Well, I can do all of that with other functions and pivot tables". And of course, you can.

There are two major advantages to using `QUERY`, however:

1. Firstly, it allows you to quickly perform a number of calculations and filters all at once
2. And secondly, it allows you to *dynamically generate versions of your data* which answer particular questions.

That second part will bear some further explanation. But let me put it like this: if your data is published, `QUERY` allows you to create as many different URLs as the number of questions you can come up with. Each URL will show a different view on your data which answers that question. The user writes the query (either literally in the URL, or by entering criteria on a form), not you.

## Forming the question: `Select`, `Where` and `Order by`

`QUERY` has two required parameters, plus a third, optional, parameter. These are:

1. The **range of cells** containing the data you want to run your query on
2. The **query** itself, expressed as a string inside quotation marks
3. Optionally, the *number of header rows you want* on the result. If you don't specify this, the formula will take an educated guess. Most of the time you have no need to use this (it results in some odd formatting if you specify fewer or more columns than you're getting)

The **range of cells** you specify is likely to be the cells containing a table, somewhere in your workbook. In many cases it's going to be on another sheet entirely, in order to keep your results separate.

The **query** is where the real work is done. Here you will need to know a number of special commands, called **clauses**.

These **clauses** are taken from the [Google Visualization API Query Language](https://developers.google.com/chart/interactive/docs/querylanguage) - but you really only need to know five. And these work exactly the same way as they do in SQL:

* `Select` is used to identify which columns you want to **show** (not necessarily the ones you're questioning)
* `Where` is used to specify **conditions**, such as 'Where this column has this value' or 'Where that column is below this value'
* `Group by` is used to **aggregate** results, in the same way as a pivot table might group payments by company. For example you might group results (for example totals or averages) by each country listed in column D, or each category in column E.
* `Order by` is used to **order** the results: for example by a numerical column (highest to lowest, or lowest to highest), or by a text column (alphabetically A to Z or Z to A)
* `Pivot` is used to turn values into new column headings. For example if you wanted a column for every year or location in the data.

As you can see, most of these clauses use simple language and are pretty intuitive to use.


### Selecting which columns you want to show in the results

By way of example, here's a very simple `QUERY` formula:

`=QUERY(A1:D200,"select C,D")`

The first ingredient, `A1:D200` specifies where the data is contained.

The second ingredient is the query: `"select C,D"`

There is one clause in that query: **select**.

All that this does is use `select` to say that it only wants to show two columns of results from that range specified in the first parameter: C and D.

Note that these are separated by a comma and not a semi-colon.

**You can put those columns in any order**. So, for example, we could say `"select C,D,A"` and the result would show column C, then D, then A in that order.

But **you must use upper case letters to identify columns**: "`select c,d`" will generate a `#VALUE!` error.

We've not added any more clauses such as conditions, ordering or grouping. So all that this does at the moment is grab two columns from the original data, and show the contents. So we have 200 results.

### Specifying a criteria for which results are shown

Now let's take that formula and add an extra clause like so:

`=QUERY(A:D,"select C,D where B='Aintree'")`

Now there are *two* clauses in the query: **select** and **where**: `"select C,D where B='Aintree'"`

The `where` clause sets a condition: it now doesn't want *all* cells in C and D; it only wants those *where* the value in B is 'Aintree'.

Note that because this value is *also* a string, we need to use **single quotes** to identify it: otherwise it would be confused with the double quotes inside which this whole query sites.

A> If your criteria involves numbers rather than strings then you do not need quotes at all, for example:
A>
A> `=QUERY(A:D,"select C,D where E>5000")`
A>
A> Remember that dates are stored as numbers too, so you just need to know the number for the date you want to use as your criteria. So for example dates after March 12 2011 would be 'greater than 40614'. See the chapter on dates for more on how to find this number and work with it.

Our 200 results have now been narrowed to just 22 which match the query. And the query still only fetches the details in columns C and D.

![](images/horsedeathswhere.png)

You can create multiple criteria or alternative criteria (i.e. data which meets this criterion *or* that criterion), but we'll come onto that below.

### Ordering the results

Fancy upping the ante to three clauses? OK, then: let's **order** the results by name of horse, which is column D:

`=QUERY(A1:D200,"select C,D, A where B='Aintree' order by D")`

This third clause is `order by` and all it needs is the column letter you want to order by.

By default it will order **in ascending order**: from A to Z or, in the case of numbers, from lowest to highest.

To order it **in descending order** - from Z to A or largest to smallest - add `desc` like so:

`=QUERY(A1:D200,"select C,D,A where B='Aintree' order by D desc")`

You can specify ascending order too, with `asc`:

`=QUERY(A1:D200,"select C,D, A where B='Aintree' order by D asc")`

And you can order by multiple columns in order. For example:

`=QUERY(A1:D200,"select C,D, A where B='Aintree' order by A asc, C desc")`

The formula above first orders by A (the date, earliest first) and then by C (the cause of death, in descending order).

Where there is more than one entry with the same date, then, those entries are further sorted by cause of death.

Note that in this clause, there is a **comma** after `A asc` and before `C desc`.

T> ### Showing only the top few results: `limit`
T>
T> One extra clause which can come in useful is `limit`: this specifies that you only want a certain number of rows of results. For example, you could limit results to the top 3, or the bottom 5, or the top 10.
T>
T> As you can imagine this is best combined with `order by`. So if we wanted to show the five biggest amounts in column C we would specify somewhere in our query `order by C desc limit 5`.


A> ### How is `QUERY` different from SQL?
A>
A> `QUERY` is a great way to get started on Structured Query Language, which you'll need if you want to question large and/or multiple datasets.
A>
A> The one main difference is that SQL uses `FROM` to identify what table or tables it is fetching data from (by the table's name), e.g. `SELECT * FROM Horsefatalities`. The `QUERY` function, however, just specifies the source data as its first parameter, and by referring to the cells rather than the name of any file.
A>
A> A second difference is that SQL is often used to grab data from more than one table, [using `JOIN` to combine data from each](http://www.w3schools.com/sql/sql_join.asp) into a new table. Sadly [Google's query language](https://developers.google.com/chart/interactive/docs/querylanguage) does not include a `JOIN` clause.
A>
A> Finally, SQL's big advantage is that it is querying *files* (flat spreadsheets in CSV format, for example), rather than running *within* a spreadsheet. This means large datasets which you *could* query with SQL would be too big for Google Sheets, or constantly crash or freeze Excel.
A>
A> Those differences aside, however, there's not much in it. Once you've used `QUERY` on smaller datasets it should be relatively easy to pick up SQL.

## More complex clauses: `group by` and `pivot`

The `group by` clause is not quite as simple as other clauses. This is because it needs to be combined with a calculation such as `SUM`, `AVG`, `MAX` or `COUNT`.

These are called **aggregation functions** and are very similar to similarly-named functions in Excel or Google Sheets (with some key differences I'll come on to).

I> A list of **aggregation functions** is [available in the documentation for Google's Query Language](https://developers.google.com/chart/interactive/docs/querylanguage#aggregation_functions)


Here's an example of what I mean. In the chapters on `GOOGLETRANSLATE` and averages I mentioned [a dataset from the European Investment Bank](http://www.eib.org/projects/loans/list/) which shows details on every loan issued by the bank. When opened in a spreadsheet it has the following columns:

> A: Name of recipient
>
> B: Region
>
> C: Country
>
> D: Sector
>
> E: Date of signature
>
> F: Signed amount
>
> G: Description

If we wanted to query that data to **group** it into total amounts for every region, we would write the query like so:

`=QUERY('Sheet 1'!A1:H211,"select B, sum(F) group by B")`

In that formula above we are grabbing the data from another sheet, called 'Sheet 1': specifically cells A1 to H211 on that sheet (for the sake of simplicity I'm not going to select thousands of rows).

The *query* we are running on that data is to `select` B (the region). Note that we need a **comma** immediately before we move on to the `group by` clause.

We then use `SUM` to specify that we want to total up the values in column F (the loan amounts) *and* group those sums by B (the region).

It might sound like we're doing the same thing twice but that's one of the quirks of `QUERY`: [the documentation specifies](https://developers.google.com/chart/interactive/docs/querylanguage#Group_By) that "every column listed in the `select` clause must be listed in the `group by` clause" (with some exceptions).

And we don't actually get *just* column B in the end result: we also get a second column, which has a name that prefixes the column we are summing with the word `sum`: in this case `sum Signed Amount (euro symbol)`.

![](images/eibquery.png)

If you want to pull in more than just the column you are grouping by, you'll still have to list it under `group by`.

See, for example, what happens when I change `select B` in the formula above to `select B,C`, so that the formula reads `=QUERY('EIB loans 200rows'!A1:G211,"select B,C, SUM(F) group by B")`

![](images/queryvalueerror.png)

You get a `#VALUE!` error.

Making sure we *also* change `group by` to refer to the same columns - `group by B,C` - solves the problem.

![](images/eibgroupbyBC.png)

And you can do more than grouping by sum: you can group by `MAX` (maximum amount for each country, region, etc.); by `MIN` (minimum amount for each); `COUNT`; or average.

Notably, **the average is not calculated using AVERAGE**. Instead you must use `AVG`, like so:

`=QUERY('Sheet 1'!A1:H211,"select B, avg(F) group by B")`

### Adding more than one calculation column

Using `AVG` or `SUM` will generate a table with a column specifically containing the averages or sums grouped by the column you specified.

But what if you want to do both? Well, you can.

All you have to do is add a **comma** between the two calculations. Here, for example, is a formula which groups by region (column B) the average loan values and the total amount of loans (F):

`=QUERY('Sheet 1'!A1:H211,"select B, avg(F), sum(F) group by B")`

You can add more and more columns by adding another comma and the calculation you want to use.

T> ### Labelling your columns
T>
T> You can change the headings in the results of your query by using the `label` clause.
T>
T> The `label` clause should be followed by the letter of the column and the label you want to use for that, in inverted commas, like so: `label B 'Total loans'` or for more than one: `label B 'Part of the world', C 'Part of the region'`.


### Calculations with text data

Two of these functions - `AVG` and `SUM` - only work with numerical data. But curiously the other three - `MAX`, `MIN` and `COUNT` - will work with text data too, unlike the functions of the same name in Excel/Google Sheets, which only work with or count numbers.

When used with text `MAX`, for example, will give you the entry which is **alphabetically last**. So, 'zebra' rather than 'ant'.

Conversely, `MIN` will give you the entry which comes first alphabetically: 'aardvark' rather than 'zonkey', then (a zonkey is a cross between a zebra and a donkey! And don't get me started on zedonks...)

`COUNT` will count numbers *or* text. So, for example, if B contained the region for each loan and we simply wanted to know how many loans there were to each region we could try the following:

`=QUERY('Sheet 1'!A1:H211,"select B, count(C) group by B")`

In this case the query counts how many entries there are in column C, and groups them by region (column B). So if there are 52 entries in C for the region 'South Africa', and 4 for 'European Union', then the resulting table will show that, and so on for all other regions.

W> ### Why we don't count the same column
W>
W> Why don't we just `count` the same column we're selecting and grouping by, as we might in a pivot table? Well, using *any* column that we're selecting/grouping will generate an error. Sorry, that's just the way it is.
W>
W> So, the following formula will generate an error:
W>
W> `=QUERY('Sheet 1'!A1:H211,"select B, count(B) group by B")`
W>
W> And so will this:
W>
W> `=QUERY('Sheet 1'!A1:H211,"select B,C count(C) group by B,C")`
W>
W> You just need to make sure you're counting a column which doesn't have any empty cells.



### The `pivot` clause: adding new columns

Adding the `pivot` clause to your query is a little like using the `TRANSPOSE` function or command: it will effectively switch columns and headings from how they might have looked otherwise.

The key difference is that `pivot` allows you to specify what headings you want to use. If, for example, you had regions in column B then adding `pivot B` to your query would create a heading for each region. If you had years in column C then using `pivot C` would likewise create a heading for each year.

As with `group by`, `pivot` works best with some sort of **aggregate function** like `SUM`, `COUNT`, and so on. Here's one relatively simple example:

`=QUERY('Sheet 1'!A1:G211,"select count(C) pivot B")`

Here the query part of the formula is counting the values in column C, and using `pivot` to specify that it wants the results split into columns based on the values in column B.

![](images/pivoteg.png)

In many ways `pivot` is similar to `group by`: automatically the results of that `COUNT` are aggregated (grouped) by whatever is in column B.

The difference, of course, is that you get a very wide table rather than a tall one. Which one you want depends on what you need to do with it, but in most cases a tall one is easier to interpret.

## Writing queries with multiple or alternative criteria

Until now I've only talked about `where` clauses with only one criterion. But often you want to set multiple criteria, for example:

* You only wanted results in one particular category AND above a certain value.
* You wanted results from this category OR this category OR that category.
* You wanted results from this category OR below a certain value.

If you wanted to run a query like those which sets multiple criteria then you will need to use **parentheses** with the `where` clause.

Here is an example:

`=query(A1:D200,"select C,D,A where (B='Aintree' OR B='Wolverhampton')")`

The key part to look at is right after `where`: now we open a parenthesis, start our original criterion `B='Aintree'` then add `OR` and a second criterion, before closing the parenthesis.

If you want the criteria to *all* apply then you need to add `AND` instead of `OR` like so:

`=query(A1:D200,"select C,D,A where (B='Aintree' AND C='Broke Neck')")`

And of course remember you can do this with numeric criteria too:

`=query('Sheet 1'!A11:G221,"select B,C,D,F where (F>5000000 AND D='Energy')")`

## Generating 'hackable' URLs which allow users to see the data their own way

This last part is perhaps the most exciting element of the `QUERY` function - but also the most difficult to explain.

It involves creating what's called a **hackable URL**.

A> A hackable URL has nothing to do with hacking in the popular sense of 'hacking into a system'. Instead, 'hackable' means that an individual can construct their own URL to get different results. ('Hacking' is often misrepresented in media reports as being something illegal. In fact, programmers use the term 'hacking' or 'hack' to refer to any sort of quick fix or workaround).
A>
A> Search results are one of the most common types of hackable URL. Here, for example, is the URL for results from Twitter's search tool:
A>
A> `https://twitter.com/search?q=excel`
A>
A> The URL shows the search query: `q=excel`
A>
A> You can 'hack' that URL to show results for any search term. For example, replace `q=excel` with `q=spreadsheets` and you'll get a webpage showing results for the search query 'spreadsheets'.
A>
A> These sorts of hackable URLs allow you to conduct multiple queries quickly. In fact, we've used them already: in the chapter on `GOOGLETRANSLATE` we generated search URLs in other languages by adding terms to the end of the URL `https://www.google.co.uk/search?q=`

You will need three ingredients to make up this URL. I'll explain each in turn below:

1. A **'base URL'** including your spreadsheet's **'key'**
2. Your **query** in URL form
3. And a little extra part of your URL to make it display in HTML

In addition, if your spreadsheet has more than one sheet and you want to specify which one, you will also need a **GID** parameter


### The 'base URL' for public spreadsheets

The '**base URL**' is the term for the part of the URL which always forms the basis of our full URL.

In the examples above, the base URLs are `https://twitter.com/search?q=` and `https://www.google. co.uk/search?q=`

When it comes to public Google spreadsheets that base URL is:

`https://docs.google.com/spreadsheets/d/`

But your specific spreadsheet will have a longer base URL that also includes the **key** for your spreadsheet. To get this, you will need to share your Google spreadsheet publicly.

Open your spreadsheet and click on the **Share** button in the upper right corner.

![](images/sharebutton2.png)

A new window should open. Click on the grey link in the upper right corner of *that* window that says **Get sharable link**.

![](images/getsharablelink.png)

Copy the sharable link and paste it into your browser address bar or, better still, a text editor like Notepad (Windows) or TextEdit (Mac).

![The key in this URL is highlighted](images/spreadsheetid.png)

In the middle of that URL should be your spreadsheet **key**. It comes *after* `https://docs.google.com/ spreadsheets/d/` but *before* any further backslashes like this: `/pubhtml?gid=1535563184&single=true`

The key will be made up of a random collection of letters and numbers - something like this: `1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0`

In full, then, your specific spreadsheet's base URL should look something like this:

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0`

Copy that part of the URL into another browser or into a text editor - but don't press Enter yet, because **you'll need another part of the URL** too.

### Adding some code to use the Google Visualisation API Query Language

Now this next part might throw you a bit, but bear with me on this.

*At the end of the URL you have so far*, add the following:

`/gviz/tq?`

This should give you a URL which looks like this (your key will be different):

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0/gviz/tq?`

If you are using a browser like Chrome (not all browsers will support this stage) and pressed Enter now you would get a page full of JSON code.

![An example of the JSON generated when you add /gviz/tq to a Google Sheet sharable URL](images/gvizjson.png)

This is your data represented as JSON code. That can be quite useful in itself if you wanted to use that as a feed for a dynamic visualisation. But that's not what we're doing. We need to do two more things:

1. add a query to drill down into that data; and
2. add a parameter to display that as HTML, not JSON.

### Formatting a query for a URL - and escaping special characters

To add a query to our URL we need to add the characters `tq=` followed by the query as we would write it in a formula - but **with all spaces, operators and inverted commas 'escaped'**.

**'Escaping'** a character means representing it with a special symbol or code. This is generally done for characters which would otherwise be interpreted as *commands* or which can cause problems.

For example, as mentioned earlier in this book, browsers can not handle **spaces** in web addresses, so they are replaced by ('escaped with') either `%20` or `+`.

In our case we will need to replace spaces with `%20`, but that's not all.

Some of the characters which might be similarly problematic in a query include the equals operator, 'greater than' and 'less than' operators, plus operator, and inverted commas.

The 'codes' for those are as follows:

* Inverted comma (`'`): `%27`
* Less than (`<`): `%3C`
* Equals (`=`): `%3D`
* Greater than (`>`): `%3E`
* Plus sign (`+`): `%2B`

Here's an example of a query using some of those escaped characters to show you what I mean:

`tq=select%20A%20where%20C%3D%27Poland%27`

This means `select A where C='Poland'`

Here's the same code with the non-escaped elements in bold:

tq=**select**%20**A**%20**where**%20**C**%3D%27**Poland**%27

The spaces are easy to spot. There are three of those before the equals sign (`%3D`) which comes immediately before the first of two inverted commas (`%27`).

**You don't need to remember all of these codes**. Helpfully, [the reference page for Google's Query Language](https://developers.google.com/chart/interactive/docs/querylanguage) includes a [section](https://developers.google.com/chart/interactive/docs/querylanguage#Setting_the_Query_in_the_Data_Source_URL) with a tool to "encode or decode a query string".

![Google's encode/decode tool](images/encodedecodetool.png)

All you need to do is type your query into the box on the left, click **Encode >** and the box on the right will give you an 'escaped' version which you can paste into your URL.

**Remember to prefix that query with `tq=`**

Once you've generated your query your URL so far should look something like this:

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0/gviz/ tq?tq=select%20A%20where%20C%3D%27Poland%27`

When you put that URL into a JSON-friendly browser like Chrome and press Enter your page of JSON should look much shorter - because now this is not *all* data, but only **the data generated by your query**.

![](images/sqlqueryjson.png)`

Again, this can be useful if you're working with a developer or a piece of script which requires a JSON input.

But if you *do* want a HTML page showing your results, you just need to add one last parameter to your URL.

### Presenting the results as a HTML table

The extra bit in your URL that you need is this:

`&tqx=out:html`

This specifies the **output**: HTML is just one option; CSV is another.

When you add that to the end of your URL it should look something like this:

`https://docs.google.com/spreadsheets/d/1AI8u3TgWnytsngAX0CoWh9mGWT-cSudNvZLyBa79aG0/gviz/ tq?tq=select%20A%20where%20C%3D%27Poland%27&tqx=out:html`

And the page should change from confusing JSON code to a plain old HTML table like this:

![](images/htmloutput.png)

T> Tony Hirst identified some of these processes way back in 2009. His post on [Using Google Spreadsheets as a Database with the Google Visualisation API Query Language](http://blog.ouseful.info/2009/05/18/using-google-spreadsheets-as-a-databace-with-the-google-visualisation-api-query-language/) and [Using Google Spreadsheets Like a Database - The QUERY Formula](http://blog.ouseful.info/2010/01/19/using-google-spreadsheets-like-a-database-the-query-formula/) are well worth reading if you want to explore this further - although note that some of the processes have now changed, so you'll need this chapter too.

A> ### More than one sheet? Add the GID parameter to specify which sheet
A>
A> So far we've assumed that your data is on the first sheet of your Google Sheets workbook. But if you want to use these techniques to query different sheets you'll need to add something called the **GID parameter**: a sort of 'ID number' used to identify each specific *sheet* in your workbook.
A>
A> To find this GID look in your sharable URL, after the key but also after `/pubhtml?`. It will be prefixed by the characters `gid=`.
A>
A> ![The GID parameter highlighted in one Google Sheets sharable URL](images/gidparameter.png)
A>
A> Copy this parameter, including the `gid=` part. It should look something like this:
A>
A> `gid=1535563184`
A>
A> Now you just need to add it to the end of the URL, **prefixing it with the equals operator**, like so:
A>
A> `&gid=1535563184`
A>
A> The query will now be applied to that sheet in the workbook identified by the spreadsheet key.

## Using a form to allow users to generate their own results pages

So far we've generated the queries ourself. But what if we want users to be able to query the raw data?

One option would be to explain how to first write those queries in Google Query Language, and then encode it into a URL, as we have here.  

But that's going to exclude a lot of users. A better option would be to create a form which allows users to enter or select criteria, and then be taken to a URL which encodes those criteria.

There are a number of ways of doing this with HTML, JavaScript, PHP or other languages. Those processes are beyond the scope of this book but if you are familiar with coding, or want to use this as an opportunity to code, the key principles are that you need to take the values being entered or selected in the form, encode those so they work in a URL (in other words, escape special characters and spaces), and then insert them into the URL with the other ingredients described in this chapter.

## Examples of `QUERY` being used in code

Tony Hirst's experiments with the `QUERY` function show the potential of these 'hackable URLs' in making it easier for users to explore your data.

In [the 'Guardian Datastore Explorer](http://ouseful.open.ac.uk/datastore/gspreadsheetdb4.php) he created an interface which allowed users to select one of The Guardian newspaper's public Google spreadsheets (or directly enter a spreadsheet ID):

![](images/tonyhirstexplorer1.png)

...and then enter a query in a form:

![](images/tonyhirstexplorer2.png)

The background to that is [explained here](http://blog.ouseful.info/2009/05/22/first-steps-towards-a-generic-google-spreadsheets-query-tool/)

Of course rather than require users to enter the query into the form you could provide them with a drop-down menu or more narrow query (such as 'contains'). The possibilities are as wide as your imagination - and of course what you can learn about code!




## Recap

* `QUERY` allows you to **form questions of your data**. These often include terms like 'Select', 'Group by', 'Order by' and 'Where'. When put together a query might mean something like: '*Select all the data from these four columns where the first name column contains "Alice" and the age is over 25* or: *Group all the data by city, and count how many entries there are in each*'.

* Because Google Sheets is web-based, `QUERY` allows you to *dynamically generate versions of your data* which answer particular queries from users.

* `QUERY` has two required parameters, plus a third, optional, parameter. These are: the **range of cells** to query; the **query** itself, and how many header rows you want (optional and generally unnecessary).

* The query itself **uses clauses to filter, sort, pivot, group and display** results.

* **The `select` clause determines what columns you want to show in your results**.

* **You must use upper case letters to identify columns**: "`select c,d`" will generate a `#VALUE!` error.

* **The `order by` clause determines what columns you want to order the results by**.

* By default it orders in ascending order, but **you can specify that it order in descending order by adding `desc`**.

* **You can order by more than one column**, in order.

* **You can put those columns in any order**.

* **The `where` clause determines what criteria you want to set for showing results**: for example that they be above or below a particular number, or contain or start with particular text.

* **You can combine multiple criteria, or set alternative criteria**.

* **The `pivot` clause is used to turn values into new column headings**. For example if you wanted a column for every year or location in the data.

* Although the `QUERY` function allows you to use SQL-style commands in powerful ways, **it is worth exploring SQL itself** if you want to work with big datasets or join datasets together. The [SQLite plugin for Firefox](https://addons.mozilla.org/en-us/firefox/addon/sqlite-manager/) allows you to get started with that without having to download any standalone software.

* **The `group by` clause allows you to aggregate numbers instead of having a row for each one**: for example showing the *total* of all loans for each company (i.e. grouped by company), or the average, or maximum, minimum, or count.

* To use the `group by` clause **you need to indicate how you are aggregating by using an aggregate function** with the value being averaged in parenthesis, e.g. `SUM(F)`. The aggregate functions include `SUM`, `MAX`, `MIN`, and `COUNT`, but for an average you must use `AVG`.

* **Your `group by` clause must specify the same columns as your `select` clause** - otherwise the formula will generate a `#VALUE!` error.

* **The `limit` clause allows you to limit results to a specified number**, e.g. `limit 5` would only show the first 5 results of the query. When combined with `order by`, this allows you to limit results to the top 3, or the bottom 5, or the top 10.

* **The `label` clause allows you to replace the default headings with your own choice**.

* **A hackable URL is one that an individual can change in a meaningful way to get different results**.

* **The 'base URL' is the term for the part of the URL which always forms the basis of our full URL**.

* You can **create a hackable URL by combining your base URL with extra details** such as the key of your particular spreadsheet and parameters which specify that you want to run a query on that spreadsheet, that you want to output in HTML, and the query itself.

* **To get a key for your spreadsheet you must first share it** (publish it) using the *Share* button.

* **You can also specify a particular sheet in that spreadsheet by using the `gid=` parameter**.

* **When you encode a query in the URL you must escape special characters** like spaces, inverted commas, and operators such as 'equals', 'greater than' and 'less than'.

* **You can use a tool on the reference for Google Query Language to encode your query** so that it works in the URL

* **To specify that you want to query the spreadsheet, add `/gviz/tq?` to the URL**.

* When you do this, **by default the spreadsheet - or results of a query - will be displayed in JSON format**.

* **To specify that you want to see the results in a HTML table, add `&tqx=out:html`** to your URL

* Because the URL is hackable, **you can also write HTML or other code which turns users' inputs into new URLs that show the results on applying their criteria**.
