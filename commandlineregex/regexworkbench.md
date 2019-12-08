# Using regex in Workbench

[Workbench](https://workbenchdata.com/) is a tool for data scraping, cleaning, analysis and visualisation. Among its features is a **regex extractor**. This makes it a particularly good place to use, and learn about, regex (regular expressions).

This tutorial uses the example of scraping tweets to explain how to use regex to pull out text from tweets that matches a particular pattern (e.g. which party won an election, and in which constituency).

First, log in to Workbench and create a project by clicking on **Create Workflow** in [the workflows view](https://app.workbenchdata.com/workflows/)

## Create the scraper

You will be asked to *Choose a data source*. Scroll down and click the box for **Twitter**.

A new untitled project will be created with the Twitter module inserted as the first 'step'. To get the scraper do the following:

* Click **Connect account** and authenticate the scraper with your Twitter account, then wait to be returned to the workbench project
* Leave *User tweets* in the first dropdown menu
* In *@Username* type **bbcelection**
* Make sure *Accumulate tweets* is ticked - this ensures that new scrapes don't overwrite old scrapes
* Click on *Manual* and on the window that appears change it to an **Auto** update. Set the frequency to every week, or a higher frequency if you are scraping tweets by an account which publishes prolifically. Click **Apply** and **Close**.
* Click **Update** to run the scraper

After a while, you should see the results of the scrape appear in the project - around 3,000 of them. This is the limit that Twitter allows you to scrape.

## Add a filter

We're only interested in general election results, so we need to add a filter to get rid of the EU election tweets. 

Click on **Add step**. You will be asked to select the next step from a long list of options. Use the search box to look for *filter* and you should be able to select **Filter by condition**.

The module that appears starts with *IF* and *select column*. Because we are selecting on the text of each tweet, select **Text** from the dropdown menu.

Now you should see a new dropdown menu which says *Select condition*. Click on this and select **Text contains**.

In the box underneath, specify `#EUElections2019`

In other words, you are specifying *IF* the *text* column meets the condition *text contains* "#EUElections2019" you want to filter it in some way.

Underneath you can specify whether you want to keep, or delete, tweets that meet that condition. 

Tick **Delete** and click the 'play' button the run that filter.

The table of data on the right should now update so that #EUElections2019 tweets are removed.


## Add the regex extractor

Click on **Add step** again. Use the search box to look for *regex* and you should be able to select **Regex extractor**.

You will need to specify the *Target column* that you wish to use regex on. This will be the text of the tweet, so select **Text** from the dropdown menu.

Next you need to type the regular expression formula. We want to grab the text after 'RESULT:' to let's try this expression (you will get an error - don't worry: that's intentional!):

`RESULT:`

You will get a pink error in the same box saying *Your regex needs a capturing group. Add (parentheses).*

Try to put the parentheses around `RESULT:` like so:

`(RESULT:)`

And run it again.

Now we don't get the error - and a new column is generated called 'expression output' (scroll to the far right of the data to see it).

It should be full of cells that say 'RESULT:' - it's worked, but it's grabbed the text not what came after it.

Let's amend our regex. Try this:

`RESULT:(.*)`

Now we are saying look for the characters `RESULT:` followed by any characters (indicated by the period `.`) - specifically 'none or more' of those (indicated by the asterisk `*`)

Because the 'none or more of any character' is in parentheses -  `(.*)` - that's what will be grabbed.

Run this and we will get everything *after* 'RESULT:' in each tweet. Great. That's progress.

As with a lot of regex, this is a process of continual refinement. We've now got what we wanted, but also some extra text we want to omit.

So let's refine it further again. We want to *stop* grabbing when it gets to a dash, because that seems to mark the end of the place name and the start of other information. We can put that dash *outside* of the parentheses to indicate this:

`RESULT:(.*)-`

Now we get the constituency.

You can rename the column (currently 'expression output') as 'constituency' now. 

And move on to the next regex.

## Another column of regex extraction: the winning party

Click on **Add step** again, select **Regex extractor** and choose the same 'text' column. 

This time we want to extract the winning party. What regex can we use? 

How about this:

`RESULT:.* - ([A-Z]{3})`

This means RESULT: followed by none or more of any character, followed by a dash, followed by (and this bit is captured in parentheses), 3 capital letters.

There are flaws in this - what are they?

## Another column of regex extraction: hold or gain

Using the same logic we can extract whether the tweet says 'HOLD' or 'GAIN':

`RESULT:.* - .*([A-Z]{4})`

But we could also use pipes to indicate 'OR' and write:

`RESULT:.* - .*(HOLD|LOSE|GAIN|WIN)`

## Other exercises

Try this on a less 'regular' account like @BBCcareers. What are the challenges?
