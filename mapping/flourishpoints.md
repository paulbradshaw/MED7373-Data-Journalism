# Creating a map of points in Flourish

Create an account on [Flourish](https://flourish.studio/)

Click 'New visualisation' at the top of the screen - or go to https://app.flourish.studio/templates

Scroll down to the *Marker map* section. Select the **Category dot map**.

All the maps in Flourish come with some example data that you will need to delete, but which give you an idea of the structure of the data that you need.

Switch from the *Preview* tab to the *Data* tab (just above the map in the middle).

This visualisation has three sets of data, or tables:

* Categories
* Data
* Regions

The *Categories* table is used to colour-code and/or decorate your points. Leave that for now.

The *Regions* table is used to draw an area in the bottom right corner. Ignore that.

The *Data* table is the one with the main information, and where you need to start.

Click on the *Data* tab to look at that data.

You can either select all the data, delete it, and then paste your own instead - or you can click **Import your data**.

## Import the data

Click **Import your data** and find the data that you want to import.

You can use a CSV of crimes from [the data.police downloads page](https://data.police.uk/data/).

*Tip: This is quite a big dataset and Flourish can struggle to visualise a lot of points, so when you first use the tool it's worth trying a sample of 100 or so rows so that you can work with it quickly.*

Once it's loaded, you will get a window saying *Next, select the columns*. Click on this and look to the right hand side, in the *Select columns to visualise* area.

Here you will need to specify which columns contain latitude, and then latitude.

It will still be set to columns E and F, but you will need to see which columns have lat and long in your new data. In the case of the crime data, it's probably **B** for latitude, and **A** for longitude.

Scroll down further to see other settings for the map:

* *Marker* can be used if you have a column with image URLs (the image needs to be the right size) or emojis or Font Awesome icon names - these will then be used instead of the default marker.
* In *Name* you can specify a column with the name of the place. In the crime data, this could be column **C**.
* In *Description* you can specify a column with a description of the place or event.
* *Photo* can be used if you have a column with image URLs (the image needs to be the right size) that you want to appear in popups
* *Link* can be used if you have a column with URLs for links that you may want to use in popups
* *Category* is especially important: this needs to be used to specify the column you want to use for colour-coding and/or other decoration such as marker icons
* *Colour* can be used if you have a column with hexadecimal codes or colour names that are "web-safe" (in other words, recognised in HTML). That colour is used only if you have set a Font Awesome icon for a marker.
* If you want each marker to be a different size depending on a column in your data (for example a number of events), specify which column using the *Size* box.
* *Extra info for popups* allows you to specify any other columns you want to use for popups. For example you can put **D-F, J** to bring in columns D, E, F and J.

In this example you can leave most of these empty, apart from:

* *Category*: in the crime data you could choose to use column **E** for crime type, or **F** for outcome, depending on what you want to show. (You can always put the other column in *Extra info for popups*)

If you switch back to the *Preview* view now, you should see a series of dots scattered across the region you downloaded.

However, all of those dots will be the same colour - and you still have a legend showing a colour scheme for Apple, Cherry and Pear, and the shape of London in the bottom right corner.

If you don't want to colour-code each point, you can simply turn off the legend and shape by customising the map settings (see the section below). If you do, however, this is how to do it...

## Creating the category table

Switch back to the *Data* view and go to the *Categories* table.

You will see that this is where 'Apple', 'Cherry' and 'Pear' are being pulled from: they are in column A.

You now need to change this data to reflect the categories in your data.

If your data only has a few categories, you can delete the fruit names and enter your own manually. If you do this, make sure that they match *exactly* the words used in your data: the easiest way to ensure this is to copy and paste each category from the other data sheet.

If your data has too many categories to enter manually, then you can generate a list using a pivot table in Excel, and then copy that list.

The rest of the table allows you to specify how each category is represented on the map.

The *Icon* category can be a simple shape (use [Font Awesome icon names](https://fontawesome.com/icons?d=gallery&m=free)), but can also contain emojis, or image URL links (make sure they are the right size).

If you look to the right and continue to scroll down, you will see that the *Select columns to visualise* column has a *Categories* section which specifies the columns in this table to use to draw each point on the map. You can leave these as they are unless you have moved any columns.

Now that you have finished specifying the data for the map, switch back to the *Preview* view.

The legend should now show those categories that you added.

The points should also now be colour-coded to reflect the categories.

If you have any data with a category that *isn't* in that list, then it will be formatted differently using the default settings. The best way to solve this is to find out what categories thoes points fall into, and add that category to the list in the *Data > Categories* view.  

## Customising the map settings

In the *Preview* view, to the right of the map, you should see a series of sections where you can customise your map.

*Base map* allows you to change the type of map being used as a background. The default is *Fiord* which is quite dark - you might want to try a brighter option like *OSM Bright*.

You can also turn various elements of the map on and off, such as transport and place labels, in order to make it clearer: water and land use, for example, can probably be turned off to make for a simpler map.

*Inset map* allows you to turn that map in the bottom right off by switching **Display map** to off.

*Markers* allows you to change the default settings for markers - this will affect any that aren't in a category, or all points if you are not using categories.
  * The *Scale* box here specifies how much it changes the size of the points. If the size of each point is set at 0.3 in the Categories data table, for example, and *Scale* is set to 2, it will scale that measurement up to be twice as big, or 0.6.
  * The *Icon* box can be changed to any [Font Awesome icon names](https://fontawesome.com/icons?d=gallery&m=free) or you can upload an image or type an emoji
  * The *Opacity* box is useful in making spots semi-transparent if they are overlapping and you don't want spots to be hidden by other spots on top.

*Legend* allows you to turn the legend off if you are not using categories. Give it a title to make it clear what the category is that's being used.

*Popups* allows you to customise the information window that appears when someone clicks on a point. By default this will be the information from the columns that you selected in the data view for 'Name' and 'Description'.

Click on **Custom content** to specify what appears in the information window and customise it.

For example, if you write something like:

`<strong>{{Location}}}}:</strong> there was a {{Crime type}}. The last outcome was {{Last outcome category}}.`

Then anything in `{{}}` will be pulled from the column of that name.

Note that any columns you name here *must* be added to the 'Name', 'Description', or 'Extra info for popups' boxes in the data view. You also need to make sure that you spell it the same way - including upper and lower case letters and spaces.

*Header* allows you to add a title, subtitle and text to your map.

*Footer* allows you to add information about the source of the data, a byline, and any caveats or disclaimers about the data quality etc.


## Other considerations

If you have a lot of categories you may want to consider creating new super-categories for your data. For example, in the crime data you may want to create a 'Public order and anti-social behaviour' category that includes both those types of crime. Or you may create an 'other' category for the five or so categories that appear least frequently. You will need to create a new column in your data for these super-categories and re-import. But the advantage is that your map will use fewer colours and be simpler and clearer for it.
