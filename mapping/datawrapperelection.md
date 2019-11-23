# Creating an election map in Datawrapper

Create an account on Datawrapper.de.

Click 'New map' at the top of the screen - or go to https://app.datawrapper.de/create/map

There are three choices: you need the **Choropleth map**.

You will be asked to select which map you want to create. Pick *United Kingdom » Constituencies (hexagons)* - this will allow you to create a hex tile map for an election where each constituency is sized the same (rather than rural areas looking larger than the numbers of people they represent, and densely-populated urban areas being harder to see)

Click **Next**.

You are now at the 'Add your data' stage. Click on **Click here to upload a CSV file**

Your CSV file will need a column of constituency codes, or names. Codes are easier to match so go for that option if possible.

Click **Upload data** and find the data that you want to import.

You can use a CSV from this repository. Use [Election turnout by constituency (2017)](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/mapping/datasets/2017electionturnout.csv)

Alternatively, if it is a small dataset you can copy and paste it into the table on screen.

*Tip: it helps to move your ONS code column to the start of the dataset before importing, as this makes it easier to correctly select during the import process. You should also remove any columns you don't intend to use as this will help it to load more quickly both as a dataset and, later, as a map.*

You will need to specify which columns contain the code, and then the values you want to colour code by, if that's the option you selected. Look out for the **Next** button at the bottom to proceed after each step - you may need to scroll down.

When it is done click **GO!** to create the map. It may take a while so be patient (look for the *Loading... 50%...* in the bottom of the browser to get an indication of progress).

It should automatically map the values (on the right). That's not always going to be the case - if there are gaps this may be where codes or names don't match the list that Datawrapper is using (you can always copy it and paste it into your own spreadsheet to check).

Once your data has uploaded check it has the columns right, then click **Proceed**.

Now you are in the 'Visualize' section. Here you can specify:

* Color palette: choose a diverging palette if your numbers diverge from a central point (e.g. votes to remain below 50%, or to leave above 50%)
* Tooltips: here you can specify what details appear when someone hovers over, or clicks on, a point
* Map labels: turn these on to appear when zoomed in to a particular level (and specify that level)
* Map key: turn this on or off if you want a legend explaining the colouring

Once you're happy with these settings, click **Proceed**.

In the 'Annotate' section you can add a title, description, notes, data source and a byline.

Add these. Click **Proceed** to go to the 'Design' section - turn on *Enable social sharing* to add buttons to share to social platforms.

Now click **Publish**.

## Creating a category map

If you import data it insists on you having a numerical column to match as 'values'. However, if you copy and paste your data directly into Datawrapper, it *will* allow you to map categories such as 'Lab' and 'Con' (Labour and Conservative). Try this with [Winning party by constituency (2012)](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/mapping/datasets/electionwinners2012.csv).


## Creating a geographically accurate election map

Elections are about votes, rather than geographical space, which is why the hex tiles approach above is a better way to communicate the distribution of votes in a country. However, you can also [use the geographical map of constituencies](https://blog.datawrapper.de/new-uk-election-maps-in-datawrapper/).
