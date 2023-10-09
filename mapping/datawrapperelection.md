# Creating an election map in Datawrapper

Create an account on Datawrapper.de.

Click 'New map' at the top of the screen - or go to https://app.datawrapper.de/create/map

There are three choices: you need the **Choropleth map**.

You will be asked to select which map you want to create. Pick *United Kingdom » Constituencies (hexagons)* - this will allow you to create a hex tile map for an election where each constituency is sized the same (rather than rural areas looking larger than the numbers of people they represent, and densely-populated urban areas being harder to see)

Click **Next**.

You are now at the 'Add your data' stage. Click on **Click here to upload a CSV file**

Your CSV file will need a column of constituency codes, or names. Codes are easier to match so go for that option if possible.

Click **Upload data** and find the data that you want to import.

You can use a CSV from this repository. Use [Election turnout by constituency (2017)](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/mapping/datasets/2017electionturnout.csv) or if you want more recent results, the [House of Commons Library has results here](https://commonslibrary.parliament.uk/research-briefings/cbp-8749/).

Alternatively, if it is a small dataset you can copy and paste it into the table on the screen, or the area where it says '*Paste your data here*'.

*Tip: it helps to move your ONS code column to the start of the dataset before importing, as this makes it easier to correctly select during the import process. You should also remove any columns you don't intend to use as this will help it to load more quickly both as a dataset and, later, as a map.*

Switch to the **Match** tab to specify: 

* What you are matching on (e.g. names of areas, or codes for areas) - this is called the *matching key*
* Which columns contain the *code* or *name* (whichever you specified) for each area, and 
* The *values* you want to colour code by. 

There is also a **Check** tab to check it all makes sense to Datawrapper. 

When it is done click **Proceed** to create the map. It may take a while so be patient (look for the *Loading... 50%...* in the bottom of the browser to get an indication of progress).

It should automatically map the values (on the right). That's not always going to be the case - if there are gaps this may be where codes or names don't match the list that Datawrapper is using (you can always copy it and paste it into your own spreadsheet to check).

Now you are in the 'Visualize' section. Here you can specify:

* Colour palette: choose a diverging palette (different colours on the left and right of the scale) if your numbers diverge from a central point (e.g. votes to remain below 50%, or to leave above 50%)
* Colour type: 'steps' will limit the number of colours that can be used; 'continuous' will not.
* Legend: turn this on or off if you want a legend explaining the colouring

Once you're happy with these settings, click **Proceed**.

In the 'Annotate' section you can add a title, description, notes, data source and a byline. Don't forget the alternative description for people who are using screen readers.

You can also add **annotations** to draw attention to particular elements.

And you can customise the '**tooltips**' that appear when someone hovers over an element. 

Add these. Click **Proceed** to go to the 'Design' section - turn on *Enable social sharing* to add buttons to share to social platforms.

Now click **Publish**.

## Creating a category map

If you import data it insists on you having a numerical column to match as 'values'. However, if you copy and paste your data directly into Datawrapper, it *will* allow you to map categories such as 'Lab' and 'Con' (Labour and Conservative). Try this with [Winning party by constituency (2012)](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/mapping/datasets/electionwinners2012.csv).


## Creating a geographically accurate election map

Elections are about votes, rather than geographical space, which is why the hex tiles approach above is a better way to communicate the distribution of votes in a country. However, you can also [use the geographical map of constituencies](https://blog.datawrapper.de/new-uk-election-maps-in-datawrapper/).
