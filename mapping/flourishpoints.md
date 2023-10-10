# Creating a map of points in Flourish

Create an account on [Flourish](https://flourish.studio/)

Click 'New visualisation' at the top of the screen - or go to https://app.flourish.studio/templates

Scroll down to the *3D map* section. Select the **Simple point map**.

All the maps in Flourish come with some example data that you will need to delete, but which give you an idea of the structure of the data that you need.

Switch from the *Preview* tab to the *Data* tab (just above the map in the middle).

This visualisation has four sets of data, or tables:

* Regions
* Points
* Lines
* Inset map regions

The *Regions* table is used to draw areas on the map. Ignore that.

The *Points* table is the one with the main information, and where you need to start.

The *Lines* table is used to add any lines - again, we can ignore that.

The *Inset map regions* table is used to draw an area in the bottom right corner. Ignore that too!

Click on the *Points* tab to look at that data.

You can either select all the data, delete it, and then paste your own instead - or you can click **Import your data**.

## Import the data

Click **Import your data** and find the data that you want to import.

You can use a CSV of crimes from [the data.police downloads page](https://data.police.uk/data/).

*Tip: If the tool struggles to visualise a lot of points, try a sample of 100 or so rows so that you can work with it quickly.*

Once it's loaded, you will get a window saying *Next, select the columns*. Click on this and look to the right hand side, in the *Select columns to visualise* area.

Here you will need to specify which columns contain latitude, and then latitude.

It will still be set to columns C and D, but you will need to see which columns have lat and long in your new data. In the case of the crime data, it's probably **F** for latitude, and **E** for longitude (but check this - it's the other way around for stop and search data).

Scroll down further to see other settings for the map:

* *Scale* can be used if you have a column with values that you want to use to size each point (e.g. a number of events)
* *Color* can be used to specify the column you want to use for colour-coding 
* *Start time* and *End time* can be used if you have columns with timestamps that can be used for animating the points map to show change over time
* *Counter category* can also be used to specify the column you want to use for colour-coding
* In *Description* you can specify a column with a description of the place or event.
* *Metadata for popups* allows you to specify any other columns you want to use for popups. For example you can put **D-F, J** to bring in columns D, E, F and J.
* In *Label* you can specify a column with the name of the place or a description of the event.
  
In this example you can leave most of these empty, apart from:

* *Color*: in the crime data you could choose to use column **J** for type of crime, or **K** for outcome, depending on what you want to show. (You can always put the other column in *Metadata for popups*)

* *Label*: you may want to use the same information so it's easy to hover over each point and see what it is.

If you switch back to the *Preview* view now, you should see a series of dots scattered across the region you downloaded.

## Customising the map settings

In the *Preview* view, to the right of the map, you should see a series of sections where you can customise your map.

*Base map* allows you to change the type of map being used as a background. The default is *Fiord* which is quite dark - you might want to try a brighter option like *OSM Bright*.

You can also turn various elements of the map on and off, such as transport and place labels, in order to make it clearer: water and land use, for example, can probably be turned off to make for a simpler map.

*Points* allows you to change the default settings for points

*Popups* allows you to customise the information window that appears when someone clicks on a point. By default this will be the information from the columns that you selected in the data view for 'Name' and 'Description'.

Click on **Custom** to specify what appears in the information window and customise it.

For example, if you write something like:

`<strong>{{Location}}}}:</strong> there was a {{Crime type}}. The last outcome was {{Last outcome category}}.`

Then anything in `{{}}` will be pulled from the column of that name.

Note that any columns you name here *must* be added to the 'Name', 'Description', or 'Extra info for popups' boxes in the data view. You also need to make sure that you spell it the same way - including upper and lower case letters and spaces.

*Header* allows you to add a title, subtitle and text to your map.

*Footer* allows you to add information about the source of the data, a byline, and any caveats or disclaimers about the data quality etc.


## Other considerations

If you have a lot of categories you may want to consider creating new super-categories for your data. For example, in the crime data you may want to create a 'Public order and anti-social behaviour' category that includes both those types of crime. Or you may create an 'other' category for the five or so categories that appear least frequently. You will need to create a new column in your data for these super-categories and re-import. But the advantage is that your map will use fewer colours and be simpler and clearer for it.
