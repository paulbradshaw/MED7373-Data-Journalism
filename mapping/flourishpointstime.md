# Creating a timelapse map of points in Flourish

The 'Point map' on Flourish allows you to create a tilted map which 'plays' events as they occur across a particular time period. While maps are useful for telling stories about distribution across space (clusters and deserts, north-south divides etc.) this type of map is useful for showing the distribution of events across time too (flurries of activity, quiet periods, etc.)

I have created [an example of a point map which shows stop and search by police in Octover 2019](https://public.flourish.studio/visualisation/1012666/)

This is how you make it...

Create an account on [Flourish](https://flourish.studio/)

Click 'New visualisation' at the top of the screen - or go to https://app.flourish.studio/templates

Scroll down to the *Point map* section. Select the **Point map**.

All the maps in Flourish come with some example data that you will need to delete, but which give you an idea of the structure of the data that you need.

Switch from the *Preview* tab to the *Data* tab (just above the map in the middle).

This visualisation has two sets of data, or tables:

* Data
* Inset Map Regions

The *Data* table is the one with the main information, and where you need to start.

The *Inset Map Regions* table is used to draw an area in the bottom right corner. It's empty and unused by default, so you can ignore that.

Click on the *Data* tab to look at that data.

You will notice that as well has having columns with latitude and longitude, the data has a start time and end time. This is needed to create the timelapse effect.

We now need to check that our data has that information - and in the right format...

## Prepare the data

Download a CSV of stop and search data from [the data.police downloads page](https://data.police.uk/data/) - make sure you tick the box for *stop and search*, and the police force that you want to look at (I have used West Midlands Police).

The timestamps in the stop and search data are in the 'Date' column. They look like this:

`2019-09-30T23:01:00+00:00`

The timestamps on Flourish look like this:

`2019-10-28T05:00:23.405Z`

Notice the slight difference at the end. While our data ends in `+00:00` the Flourish version ends with `.405Z`.

For this reason, if we import the data as it is it will not work: we will get a map but it will not animate.

To fix this, we need to create a new column where we can create a working timestamp. This will take part of our date column and replace those last six characters so that Flourish will be able to recognise the timestamp and animate the points.

In your spreadsheet, right-click on column C and insert a new column.

In the first cell (C1) of that new column, call it 'timestamp'.

In the cell underneath (C2), type this formula:

`=LEFT(B2,19)&".000Z"`

The formula takes the contents of the cell next to it, in the 'Date' column, and extracts the first 19 characters. In other words, all the characters before that troublesome `+00:00`. It uses the `LEFT()` function to do this.

It then adds, using `&`, some *new* characters to the end of those 19 characters: `".000Z"`

Those new characters don't change anything - they just make the timestamp recognisable to Flourish.

Copy the formula down the entire column so that you now have a new working timestamp for every row.

Save the data. You're now ready to import it into Flourish.

*You can [find out more about timestamps here](https://help.sumologic.com/03Send-Data/Sources/04Reference-Information-for-Sources/Timestamps%2C-Time-Zones%2C-Time-Ranges%2C-and-Date-Formats)*

## Import the data

Return to Flourish and make sure you are on the *Data* tab.

You can either select all the data, delete it, and then paste your own instead - or you can click **Import your data**.

Click **Import your data** and find the data that you want to import.

Once it's loaded, you will get a window saying *Next, select the columns*. Click on this and look to the right hand side, in the *Select columns to visualise* area.

Here you will need to specify which columns contain latitude, and then latitude.

It will still be set to columns E and F, but you will need to see which columns have lat and long in your new data. In the case of the crime data, it's probably **D** for latitude, and **E** for longitude, but check.

Next you come to the box specifying *Start time*. Type **C** in that box - if that's the column where you put your new timestamp data (don't put the column containing the 'Date').

The *End time* box can be left blank (unless you are dealing with data that has both).

Scroll down further to see other settings for the map:

* *Info for popups* allows you to specify any columns you want to use for popups. For example you can put **A, F-M** to bring in columns A, F, G, H, I, J, K, L and M.
* *Category* can be used to specify a column you want to use for colour-coding and/or other decoration such as marker icons. We might use **A** if we want to tell a story about the type of stop (vehicle, person or both) or we might pick **G** if we want to tell a story about ages, **H** about ethnicity, and so on. Bear in mind that some columns (including G and H) are missing data and so those stops will be missing from any counts in the resulting animation.
* If you want each marker to be a different size depending on a column in your data (for example a number of events), specify which column using the *Value (scale)* box.
* *Value (colour)* can be used if you have a column with values that can be used to colour-code the spots. For example, high values will result in deeper colours and low values in lighter ones. The stop and search data doesn't have any values that could be used for that.

If you switch back to the *Preview* view now, you should see a series of dots scattered across the region you downloaded.

## Customising the map settings

In the *Preview* view, to the right of the map, you should see a series of sections where you can customise your map.

*Events* allows you to specify whether the event in each row is shown by a 'pulse' (radiating out) or a circle (slightly sharper). You can also change the *Blend mode* so that overlapping points are indicated by colour ('Additive' will create white spots; 'Subtractive' will create black overlaps). *Scale type* allows you to specify that you want a colour scheme which is Categorical (for category data), Sequential (for numerical values that go up from a base) or Diverging (values that spread out from a mid-point)

*Timeline* allows you to turn on or off the timeline under the map, and customise it.

*Counter* allows you to turn on or off a counter that keeps track of the events being shown, customise its location and appearance, and specify whether it counts a running total, or a rate.

*Animation* allows you to control how long the overall animation lasts and how long pulses stay on (if you haven't got an end time). I set the overall animation to 30 seconds, and the pulse duration at 0.3 seconds.

*Base map* allows you to change the type of map being used as a background. The default is *Fiord* which is quite dark - you might want to try a brighter option like *Positron*.

You can also turn various elements of the map on and off, such as transport and place labels, in order to make it clearer: water and land use, for example, can probably be turned off to make for a simpler map.

And there are options for setting the viewport (the area that the map occupies) so that it starts centred at a particular latitude and longitude, and a particular zoom level.

*Inset map* allows you to add a contextual map (e.g. showing the shape of the area as a whole) in the bottom right off by switching **Display map** to on. If you choose this, you will need to upload the data describing that shape (a shape file) to the Inset Map Regions table in the Data view.

*Popups* allows you to customise the information window that appears when someone clicks on a point. This only appears to work when the map is **not animated**. By default it will use the information from the columns that you selected in the data view for 'Info for popups'.

Click on **Custom content** to specify what appears in the information window and customise it.

For example, if you write something like:

`<strong>{{Type}}}}:</strong> there was a stop and search on {{Date}}. The recorded outcome was {{Outcome}}.`

Then anything in `{{}}` will be pulled from the column of that name.

Note that any columns you name here *must* be added to the 'Info for popups' boxes in the data view. You also need to make sure that you spell it the same way - including upper and lower case letters and spaces.

*Localizaton* provides some extra options if you want to format numbers in a particular way (e.g. currency is formatted differently in different countries)

*Layout* allows you to change the order of elements (header, map, etc.).

*Header* allows you to add a title, subtitle and text to your map.

*Footer* allows you to add information about the source of the data, a byline, and any caveats or disclaimers about the data quality etc.


## Other considerations

If you have a lot of categories you may want to consider creating new super-categories for your data. For example, you may want to create broader ethnicity categories that combine figures for multiple sub-categories, and a new category for 'unspecified' where there is no data. Or you may create an 'other' category for the five or so categories that appear least frequently. You will need to create a new column in your data for these super-categories and re-import. But the advantage is that your map will use fewer colours and be simpler and clearer for it.
