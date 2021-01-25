# Extracting text that matches a pattern: regular expressions in Google Sheets

![This story used regex to explore data on art](images/ukart.png)

The story was an unusual one: the BBC Data Unit had been given access to a dataset on more than 200,000 works of art in galleries across the UK. What patterns could we find in the data that would allow us to tell a story about the nature of the nation's paintings?

Some of the data was straightforward to work with: the 'artist' column was relatively clean, and allowed us to identify the most common male and female artist. It turned out that the latter - the Victorian botanist Marianne North - was relatively unknown. So, that was one story we could tell.

But other parts of the data were more problematic. The date column, for example, contained inconsistently formatted data: in the majority of cases a specific year had been entered, but in many others the data contained text such as "18th century" or "1900-1920" or "1800s".

We also noticed that monarchs featured heavily in the art - but understandably there was no column that was specifically dedicated to classifying those. If we were to identify the most-painted monarchs we would have to create new data that somehow extracted those names from the paintings' titles.

These problems - extracting data from existing data, particular text data - is what **regular expressions** are designed for. In this chapter I will explain what regular expressions are, and how to use them in spreadsheets.

## What are regular expressions

A regular expression is a way of describing a series of characters - they might be key words or phrases, names or addresses, or a code such as a telephone number - that follow a particular pattern.

This is often done in order to extract those collections of characters (for example pulling email addresses out of some data) or replace them (for example removing what you *don't* want).

They are especially useful in *unstructured data* such as free text fields where some sort of description has been entered (e.g. "£300 was spent on food" or "The goal was scored by Marie Smith from 30 yards"), and also for *textual data* where the text has been automated and you want to split it up into its different parts.

Regular expressions are one of the areas where Google Sheets is definitely preferable to using Excel. Although you can technically use regular expressions in Excel, the [process is complicated](https://stackoverflow.com/questions/22542834/how-to-use-regular-expressions-regex-in-microsoft-excel-both-in-cell-and-loops), involving activating special plugins and using scripts of code. Google Sheets, on the other hand, has built-in functions.

## Scenarios when you might use a regular expression

Common uses of regular expressions include:

* Extracting telephone numbers
* Extracting postcodes or ZIP codes or similar codes
* Extracting company registration numbers or invoice codes
* Extracting the names of people or places
* Extracting specific parts of an address, such as the country or street name
* Identifying links, or email addresses, or hashtags, @names etc.
* Identifying amounts of money
* Extracting addresses

Before we get into the technicalities of regular expressions here are a few examples to demonstrate how you might use them.

Firstly, imagine you have a dataset on hockey and you want to tell a story about who created the most shooting opportunities for their team mates. The data contains a line for every shot but there's no column for the person who made the pass that led to the shot. Instead it has a column with a description of what happened.

You look at that column and see that those descriptions are written in a relatively consistent way. Normally it includes a part that says "Receiving a pass from Poppy Singh" or "Following a pass from Eve Hill".

A regular expression would allow you say 'Get me the one or more words that follow "pass from" and start with a capital letter followed by one or more lower case letters'.

In this example you are describing a combination of specific words ('pass from'), character patterns (names start with capital letters), and position (coming after 'pass from').

Here's a second example: you have a column in some data on spending that contains the full address of the company receiving the money. You don't want the full address, however - you want the code that comes at the end of the address (normally called a postcode or ZIP code - or CAP in Italy, CEP in Brazil, PLZ in Germany and Austria, and PIN in India).

Your regular expression this time might say 'Find me any text that has a certain number of capital letters followed by a number, then a space, then a capital letter and two digits' (different countries' postal codes follow different patterns so you would use the description that fit the one being used by your data).

A final example: let's say in the same data there's a column which says how much money was spent, and on what - "£3000 was spent on clothes for the actors".

In this case you might use one regular expression to find the amount of money: it might say something like 'a currency symbol followed by one or more digits'. You might find that there are commas or decimals in the figures that you need to factor into your description as well ('a currency symbol followed by one or more digits and/or commas or periods'). You might use a variation of the same regular expression to grab the thing being bought: 'any text that comes *after* a currency symbol followed by one or more digits', for example.

It's worth pointing out that sometimes the same results can be achieved without resorting to regular expressions. For example, addresses are often separated by commas so using the ['Text to Columns' option](https://support.microsoft.com/en-us/office/split-text-into-different-columns-with-the-convert-text-to-columns-wizard-30b14928-5550-41f5-97ca-7a3e9c363ed7) in Excel (splitting on commas) might split out addresses in the way you need without having to resort to regular expressions.

Likewise if what you want is always at the start or end of a cell then you could use a function like `LEFT` or `RIGHT` to grab it (a more powerful formula might combine this with `SEARCH` or `FIND` to identify how many characters to grab) - or use `SUBSTITUTE` to remove all the text you *don't* want.

## Google's REGEX functions

To actually *form* a regular expression you need to use particular characters in a particular way. This is often called **regex** (a short way of saying 'regular expression').

Google has three functions that use regex:

* [`REGEXEXTRACT`](https://support.google.com/docs/answer/3098244?hl=en-GB) will extract text from a cell if it matches the pattern you describe
* [`REGEXMATCH`](https://support.google.com/docs/answer/3098292) will tell you *if* a cell contains the pattern you describe (`TRUE/FALSE`)
* [`REGEXREPLACE`](https://support.google.com/docs/answer/3098245) will *replace* text that matches the pattern you describe

All take two main ingredients:

1. The cell you want to extract text from, check for text, or replace, and
2. The regular expression describing what you want to extract, check for, and replace

The `REGEXMATCH` function has a third ingredient: what you want to replace the matched text with.

Here's one formula to demonstrate:

`=REGEXMATCH(A2,"hello")`

This looks in cell A2 for the expression "hello". If it finds that anywhere, it will return `TRUE` (that is, the cell where you type this formula will show `TRUE`). If it doesn't, it will return `FALSE`.

Here's another, using a different regex function:

`=REGEXREPLACE(A2,"hello","goodbye")`

In this case, the formula will fetch the contents of cell A2, and replace any parts that match that expression ("hello") with some different text ("goodbye"). So if A2 contained "I said hello to her and she said hello to me" the cell where you typed your formula will (once you've moved out of it) contain "I said goodbye to her and she said goodbye to me"

`=REGEXEXTRACT(A2,"hello")`

If A2 contains the characters "hello" anywhere, then the cell where you wrote the formula will simply say "hello" - in other words, it will have extracted the text matching the expression. If A2 doesn't contain "hello" then we will get an `#N/A` error.

This might not sound very useful - and indeed, it isn't. To really make the best use of this function, we will need to create an expression which is less specific - and that's where the *real* power of regular expressions becomes apparent.

## Regular expressions as a language: regex

In the examples at the start of the chapter I explained some ways in which we might describe a *pattern* of characters ('Find me any text that has a certain number of capital letters followed by a number, then a space, then a capital letter and two digits'). To do this we need a language that can describe those patterns.

**Regex** is that language. It can describe each character *literally*, as in the expression `"hello"`, but it can also use *special* characters, such as brackets, asterisks, dollar signs and others, to be less specific.

**Square brackets**, for example, can be used to mean 'any of these characters'

Here's an example of an expression that does just that:

`[A-Z]`

This means 'any upper case letter'.

To say 'any lower case letter' you would use `[a-z]`. And to say 'any digit' you would use `[0-9]`.

These can be strung together like so:

`[0-9][A-Z][A-Z]`

That expression means 'a number followed by an upper case letter followed by another upper case letter' (one way of describing part of a postcode).

Square brackets can also be used to indicate more specific ranges of characters, e.g. `[aeiou]` to indicate 'any lower case vowel'.

A series of letters or numbers in square brackets can be combined with normal (what is normally called 'literal') letters or numbers to match different variations in spelling, like so:

`[Hh]ello`

In this case the expression is saying 'an upper or lower case H, followed by the characters e, l, l, o in that order'

Here's another example with numbers:

`01[0-9][0-9]`

This expression specifies that the first two numbers should be 0 and 1, followed by two numbers of any value (this might be used to match a UK telephone area code).

We could also adapt the previous expression to read like this:

`0[12][0-9][0-9]`

That would mean 'a zero followed by either 1 or 2, followed by two more numbers' (UK area codes, for example, can begin either '01' or '02': this now accounts for that).

Square brackets are just one of a number of characteristics of regex as a specific language. For example, instead of repeating `[0-9]` nine times to indicate 'nine numbers' you might want to be able to indicate this in another way - and you can. Likewise there are ways to specify a *range*, such as 'three to five numbers' or 'one or more' (we will come onto both of these later).

There are ways of indicating *position* in regex too (whether the text is at the start or end), and negative matches like 'a non-numeric character' or 'non-space character'. But before we get into how to do those things in regex, I want to work through an example of using it in practice.

## Putting this into practice with election tweets

Regex is best understood through playing with it yourself. It is a language that often involves **trial and error** - trying different expressions until you find one that does what you need. For this reason you can find a number of 'regex playgrounds' online that make it easier to try out different expressions against example text and see how they perform.

![RegExr is one playground for trying out expressions](images/regexrscreenshot.png)

[RegExr](https://regexr.com/) is one of these playgrounds: in the top part of the page you can type an expression, and in the 'text' box underneath (which you can change to your own text) it will highlight the parts that are matched by the expression. On the left you'll also find a cheatsheet, reference and other resources.

I'm going to demonstrate how to use regex with some tweets from [the @BBCelection Twitter account](https://twitter.com/bbcelection). This is a good dataset to demonstrate regex because the tweets themselves are automated and so follow a predictable pattern that we can effectively reverse engineer with the regex.

![](images/bbcelectiontweets.png)

You can [dowload the data from this link](https://docs.google.com/spreadsheets/d/e/2PACX-1vSGthRci_vLp_GoQDtV2PuvCIxgrgqwhuA1e5md-lrWAEkSWADxYxTPeWqbcxDdj8W5rxOkPGhwimcg/pub?gid=482820707&single=true&output=csv). It's been simplified to 5 columns:

* The screen name of the account (bbcelection)
* A datestamp: `created_at`
* The text of the tweet
* A 'source': for example, whether the tweet was posted using the Twitter web app, Twitterfeed or the BBC Election Bot
* And the ID number of the tweet

We will only be using one of those columns: the text of each tweet.

First, we need to decide what *pattern* of text we want to match. For that, we need to look at the tweets themselves. What patterns can we identify? And which ones do we want to match (that might be in order to extract matching patterns - or use them to exclude tweets)?

One obvious pattern is that the most recent tweets appear to focus on the overall national result of the election, with text like this: "RESULT: National result for #BBCElection #GE2019. Full results: https://t.co/tFoMAGcFsq https://t.co/CkDxxFFbDa"

Let's decide that we are *not* interested in tweets about the "national result". We can use `REGEXMATCH` to detect tweets that match that pattern, and then filter on those TRUE/FALSE matches.

Give column F a title (in cell F1): "national_results". Underneath, in cell F2, type this formula:

`=REGEXMATCH(C2,"National result")`

![](images/regexmatchscreenshot1.png)

This very simple regex - basically, a literal match of the string of characters `"National result"` - will return `FALSE`. That's because C2 doesn't contain that string of characters. Copy that formula down, however, and it should return `TRUE` when it looks in cell C4, C6, C7 and others where that string occurs.

Try changing the formula in cell F4 (where it currently returns `TRUE`) so that the upper case N is now *lower case* like so:

`=REGEXMATCH(C4,"national result")`

The formula should now return `FALSE`. This is because regex is case sensitive: it's looking for 'national result' with a small 'n' and the tweet text in cell C4 contains 'National result' with an upper case 'N'.

It's not important to ask: is the case of that letter important?

If it doesn't matter whether the 'n' is upper or lower case, then our regex should not specify that either.

So let's delete the formulae that we typed before and start again, starting in cell F2, by typing this:

`=REGEXMATCH(C2,"[Nn]ational result")`

...and then copy down the whole column again.

Now we are looking for a match where the 'n' at the start can be either upper or lower case.

That should give us a column full of TRUE and FALSE values that we can use to filter out those tweets that relate to national results (TRUE).

That's a very basic application of regex: one thing it doesn't do, for example, is specify whether any characters come before or after that string `"[Nn]ational result"` (which you normally have to do when using regex in coding). But Google Sheets assumes you are looking *anywhere* in the cell unless you specify otherwise by using special characters.

Now let's move on to another function and explore some more advanced regex.

## Using `REGEXEXTRACT` with more advanced regex

Once again, it's best to start with a piece of text that represents the sort of pattern that you're trying to match. Let's say we are interested in tweets announcing the result in a particular *area*. Those tweets look like this:

> "St Ives: CON HOLD #BBCElection #GE2019. Full results: https://t.co/XhpPKd29Lq https://t.co/ewVXioRbVo"

And this:

> "Colne Valley: CON GAIN FROM LAB #BBCElection #GE2019. Full results: https://t.co/WQ2Cp80wKX https://t.co/onDZ6ff3K0"

What patterns can we pick out that are common to both examples?

I'm going to leave a pause here so you can grab a piece of paper and write some down: see how many patterns you can describe that the two pieces of text have in common.

Think not only about specific words that are the same, but about the use of upper and lower case, punctuation and position (start, end, middle) that are similar, even when the specific words are different.

Have you finished?

OK. Here are some that I can see:

* The first word or words start with an upper case letter followed by lower case letters (what's called [title case or headline case](https://en.wikipedia.org/wiki/Title_case), i.e. the way that the titles or names of things are normally written with the first letter in upper case). That's because they are the names of places, of course.
* That is followed by a colon
* And a space
* We then have a collection of three upper case characters that refer to a political party (e.g. CON for Conservative Party)
* And a space
* Then four upper case characters that refer to the type of result (gain or hold)
* After either a space or more upper case characters, these characters: "#BBCElection #GE2019. Full results: https://t.co/"
* After the start of that link, however, there are a series of alphanumeric characters (both upper and lower case, text and numeric) followed by a space and "https://t.co", then more alphanumeric characters (both upper and lower case, text and numeric)

There's plenty to go on here. In particular it's worth emphasising that spaces are just as important as letters and numbers, and punctuation is important too.

We are going to try to create a column that extracts the party which was announced as the winner of the election in that particular area.

Give column G the name "winning_party"

There's no point testing our formula in cells G2, G3 or G4 because the tweet text in the corresponding cells in column C don't relate to winning parties.

So skip to cell G5, and type this formula:

`=REGEXEXTRACT(C5,"[A-Z]{3}")`

The regex here specifies *three upper case characters*. Or, more specifically, it says "any upper case character: three of them".

### Modifiers in regex

The number in curly brackets - `{3}` - is what's called a **modifier**.

A modifier is a special character in regex that modifies whatever comes before it. Examples include "one or more [of what was described]" and "three [of what was described]".

In this case the modifier `{3}` is modifying `[A-Z]` (any upper case character).

Here are some other modifiers that can be used in regex:

* To specify 'one or more of' use `+`
* To specify 'none or more of' use `*`
* To specify 'zero or one of' use `?`
* To specify a particular range of instances, such as 'between 5 and 10 of' you put the lowest and highest number in curly brackets with a comma like so: `{5,10}`
* To specify a minimum number of instances, such as 'at least 7' you put the number in curly brackets followed by a comma like so: `{7,}`

![](images/regexextractscreenshot1.png)

Of course you could equally write this regex like so:

`=REGEXEXTRACT(C5,"[A-Z][A-Z][A-Z]")`

And that would be fine. The modifier just exists as another way to describe it - as well as a way to more flexibly describe potential variations in length, which we will need later.

Either regex works for our test cell - extracting "CON".

Copy that formula down, however, and you'll find that it extracts "RES" from the tweets that being "RESULT:".

![](images/regexextractscreenshot2.png)

How can we stop that happening?

A very simple way is to add the *space* that comes after "CON" but does *not* come after "RES". A formula in row 6 with that space in it would look like this:

`=REGEXEXTRACT(C6,"[A-Z]{3} ")`

When this formula is used instead, you should see `#N/A` results for the "RESULT:" tweets because it doesn't find a match.

There's one odd exception: in one tweet it extracts "TWL". Here's the tweet:

RESULT: National result for #BBCElection #GE2019. Full results: https://t.co/qE0yxz5TWL https://t.co/kFyHWZXvuJ"

Finding the match is tricky: it's actually from one of the URLs: that random collection of letters and numbers in the first link ends with TWL - and then there is a space.

How can we exclude random matches like this? Well, we might decide that we can just clean those rare issues out later, during data cleaning. But we could expand our regex again.

This time, we can look to the left of the text string we wanted to match: while "CON" is followed by a space to the right, it's also *preceded* by a space to the left.

Some regex to match that would look like this:

`=REGEXEXTRACT(C12," [A-Z]{3} ")`

Using spaces in our regex creates a small problem: we just want the three-letter party symbol, not the spaces around them.

Again, we can just decide to tidy that afterwards - or we can wrap the whole of our formula in a `TRIM` function that [strips out any space at the start and end of a cell](https://exceljet.net/excel-functions/excel-trim-function), like so: `=TRIM(REGEXEXTRACT(C12," [A-Z]{3} "))`

But we will put that to one side for now. Instead, let's ask a question: are all the parties represented by three-letter codes? No. Some parties are actually two character codes: the Liberal Democrats are LD and Sinn Fein is SF.

This is where our modifier becomes especially useful.

We can adjust the expression so it captures *either* a series of two or three upper case letters, like so:

`=REGEXEXTRACT(C5," [A-Z]{2,3} ")`

*(Note that this is the formula in row 5, looking at C5 in that row)*

When copied down, it not only extracts the "CON" text in tweets that contain it, but also, in row 15, "SF" for the party Sinn Fein.

![](images/regexextractscreenshot3.png)

### Using the pipe symbol for 'OR' matches

Now let's try to extract whether the tweet says that a party 'gained' a seat (took it from another party that won in the last election), or held it.

Give column H the title 'hold_or_gain'.

The pattern of text that we want to match is *either* "HOLD" or "GAIN". This allows us to use another special character in regex that means 'or': the pipe symbol, `|`.

Again the text in row 2 doesn't contain what we want to match, so it's quicker to test out our regex in row 3. In cell H3, then, type this formula:

`=REGEXEXTRACT(C3,"HOLD|GAIN")`

The regex here means 'look for the sequence of characters "HOLD" *or* the sequence "GAIN"'. More pipe symbols can be added to increase the number of options. For example we could expand it to look for 'WIN' or 'LOSE' too, like so: `"HOLD|GAIN|WIN|LOSE"`.

Once applied and copied down, the formula should extract either of those words if they exist in the tweet.

![](images/regexextractscreenshot4.png)

If *both* words are in the text, it will grab the *first* match against either of those.








***DOWNLOAD**




We will use the data from the story on unduly lenient sentences. This is [available on GitHub](https://github.com/BBC-Data-Unit/unduly-lenient-sentences/blob/master/ULS%20FINAL%20-%20June%202019.xlsx)

A> ## Sometimes hard work ends up left out of the story
A>
A> Despite all this work to extract the numbers from the data, in the end it was decided to leave this dimension out of [the eventual story](https://www.bbc.co.uk/news/uk-47879288), as it became clear that the article was going to focus on the proportion of requests which were not eligible for review.
A>
A> It's important to mention this because often in journalism — and not just in data journalism — you have to be prepared to leave out material because the focus of your story has changed, regardless of the work that went into it. Ultimately it doesn't matter how much work something involved: if it's not central to the story, then it shouldn't be there.


## Key points

*
