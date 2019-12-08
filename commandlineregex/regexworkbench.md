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

## Add the regex extractor

Click on **Add step**. You will be asked to select the next step from a long list of options. Use the search box to look for *regex* and you should be able to select **Regex extractor**.

You will need to specify the *Target column* that you wish to use regex on. This will be the text of the tweet, so select **Text** from the dropdown menu.

Next you need to type the regular expression formula.
