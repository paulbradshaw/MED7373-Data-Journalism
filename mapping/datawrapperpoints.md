# Creating a map of points in Datawrapper

Create an account on Datawrapper.de.

Click **Create new...** at the top of the screen, and select **Map** - or go to https://app.datawrapper.de/create/map

There are three choices: you need the **Symbol map**.

You will be asked to select which map you want to create. Pick an area relevant to your story and the scope of your data. For example, if your data is UK-wide then choose one of the UK maps (if you are mapping crime you might pick *United Kingdom » Police Force Areas*), but if it's limited to the West Midlands then choose a West Midlands map (the MSOA option is probably best as it's split into fewer areas). 

Click **Next**.

You are now at the 'Add your data' stage. Click on **Click here to upload a CSV file**

You will be asked whether your data contains addresses, or latitude and longitude. Click the one that applies - remember that lat/long is always better (addresses will be geocoded, which may create some errors).

You can now start to add your points. This can be done manually, adding each point yourself, but more likely you'll need to upload data of all the points. If you need some data to try it out, you can use a CSV of crimes from [the data.police downloads page](https://data.police.uk/data/).

Click **Import your dataset**. You will be asked to specify if your data contains addresses/place names, or if it uses latitudes and longitudes. Lat/longs are always better because with addresses Datawrapper will have to 'geocode' those to convert them to lat/longs - and it may get some wrong.

Click whichever applies to your data (police data uses lat/longs).

You can now either click the link to upload the data (it will need to be in CSV format). Alternatively, if it is a small dataset you can copy and paste it into the table on screen.

*Tip: it helps to move your lat and long columns to the start of the dataset before importing, as this makes it easier to correctly select during the import process. You should also remove any columns you don't intend to use as this will help it to load more quickly both as a dataset and, later, as a map.*

You will need to specify which columns contain latitude, and then latitude, if that's the option you selected. Look out for the **Next** button at the bottom to proceed after each step - you may need to scroll down.

When it is done click **GO!** to create the map. It may take a while so be patient (look for the *Loading... 50%...* in the bottom of the browser to get an indication of progress).

It will automatically map the lat/long columns (on the right).

Once your data has uploaded check it has the columns right, then click **Proceed**.

Now you are in the 'Visualize' section. Here you can specify:

* Axes - Size: if you want each point to be sized based on a third variable (apart from lat and long), e.g. number of crimes, incidents etc.
* Color: if you want points to be coloured differently (e.g. by a category such as age or type of business)
* Symbol shape: the default is a circle but you can choose other options here
* Appearance - Size: this is the default when all are sized the same
* Symbol colors: here you can colour-code as well, but also click on a particular colour to customise that more closely
* Clustering/binning: turning this on allows the map to indicate *concentration* of points rather than displaying them all individually. The number of points represented is normally indicated by a label as well as colour
* Tooltips: here you can specify what details appear when someone hovers over, or clicks on, a point

Once you're happy with these settings, click **Proceed**.

In the 'Annotate' section you can add a title, description, notes, data source and a byline.

Add these. Click **Proceed** to go to the 'Design' section - turn on *Enable social sharing* to add buttons to share to social platforms.

Now click **Publish**.
