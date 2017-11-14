# Creating a map of areas (shapes) in Carto

If you want to create a map of *areas* (not points) in Carto then you need *two* sets of data: the data ou want to map; and data about the *shapes* of the areas you need to show. These are commonly called **shapefiles** after one common file format (.shp), but can also be called **KML** files, **boundaries**, **geometry** or similar terms. The files typically end in .shp, .kml, and .geojson, among others.

## Finding shapefiles

Shapefiles can be found in various places. Russian Sphinx [maintains a directory here](https://russiansphinx.blogspot.co.uk/2014/11/shape-file-directory.html), or you can use a search engine to search for the "shape files" and the area you need, or use the operators `filetype:shp` or `filetype:kml`. You can also [use Google Tables Search, select the 'Fusion Tables' option](https://research.google.com/tables?corpus=fusion&ei=c3gJWoWeConUpAP8zISYDQ), and search for your area plus the words "geometry" or "KML". Open up the resulting map and if it contains the shapes you need, select *File > Download as* and then *KML*.

You can [find shapefiles for UK boundaries on the ONS Open Geography Portal](http://geoportal.statistics.gov.uk/datasets?q=Latest_Boundaries), and this is a good place to start to get some experience of working with them.

First,   use the search box to look for the boundaries you're interested in, and then the filters on the left to drill down further.

For example, try searching for "constituencies" (you get [over 50 results](http://geoportal.statistics.gov.uk/datasets?q=constituencies&sort=name)) and then expanding the tags on the left and [selecting the tag 'Westminster Parliamentary Constituencies (22)'](http://geoportal.statistics.gov.uk/datasets?q=constituencies&sort=name&t=westminster%20parliamentary%20constituencies) and then [sorting the results by 'Most recent'](http://geoportal.statistics.gov.uk/datasets?q=constituencies&sort=-updatedAt&t=westminster%20parliamentary%20constituencies). The top result is [Westminster Parliamentary Constituencies (December 2016) Full Extent Boundaries in Great Britain](http://geoportal.statistics.gov.uk/datasets/westminster-parliamentary-constituencies-december-2016-full-extent-boundaries-in-great-britain). You can click on **Download** to get it as a spreadsheet, KML or Shapefile.

Note that the KML is a single file - a whopping 162MB - whereas the Shapefile download is a (smaller) zip file containing a number of files with different extensions. There is no need to unzip this file: note that Carto's [documentation on geospatial data formats](https://carto.com/docs/carto-engine/import-api/importing-geospatial-data/#supported-geospatial-data-formats) specifies that "Shapefiles must be imported as a single compressed file, in the .zip or .gz format."

The spreadsheet is useful to give you a list of the entities contained. You'll need this to make sure your other data matches the names in the shape files.

Another way to navigate the site is to use the *Boundaries* drop-down menu across the top to drill down to *Administrative boundaries* and then *Local authority districts* (for example) and [finally the latest ones (2016 at the time of writing)](http://geoportal.statistics.gov.uk/datasets?q=LAD%20Boundaries%202016&sort=name).

This gives you 5 different versions of what appears to be the same shapes. What's the difference? Mainly size: the KML file for the "Full Clipped" boundaries is over 150MB, but the "Ultra Generalised" version of the same shapes is a mere 1.3MB. If you want your map to load fast - and you don't need a lot of detail (which we typically don't) - then you'll want the smaller "Ultra Generalised" version.

Note that this is the same for the constituencies results: the smallest file is the ["Super Generalised Clipped Boundaries"](http://geoportal.statistics.gov.uk/datasets/westminster-parliamentary-constituencies-december-2014-super-generalised-clipped-boundaries-in-great-britain)

## Combining your shape file with your data to make a map

Create an account on Carto.com, and log in.

Click 'New map'

Click 'Connect dataset'

Click 'browse' and find the shapefile you downloaded (either the .kml or the .zip file containing the shapefiles). Upload it.

You should now have a map of the shapes - but they will all be the same colour. You now need to upload *another* dataset with some values for each area.

On the left hand side of your new map you should see a column with settings for this map. It includes a section towards the top saying *LAYERS (1/8)* and *WIDGETS*, then a button for **ADD**.

Click **ADD**, then browse to your second dataset with the values. Note that this dataset *must* have the names or (better still) codes of the areas in it too, so you can merge the two.

Once uploaded, you should now see two boxes on the left (one for each dataset) and the top part updated to say *LAYERS (2/8)*.

Click on the top dataset. You are now taken to a new area with 5 options across the top. It will defaut to the *Style* tab where it says "There's no geometry in your data that could be styled. Please georeference or manually add data to visualize."

Switch to the *Analysis* tab. It will say:

> "You have not added any analysis yet. Add an analysis to discover new things."

Click **ADD ANALYSIS**.

You will now be presented with a page full of different analyses you can add. Select **Join columns from second layer**, on the upper right, then click **ADD ANALYSIS** in the bottom corner.

You are now taken back to the *Analysis* tab with your map showing on the right. Underneath *Analysis* are two sections: *[1] Your workflow (0)* and *[2] Join columns from 2nd layer*

In the bottom section you need to specify what you want to join. The first box - *SOURCE* - is already filled in with the dataset you clicked on.

Now click on the second box - *TARGET* - and select the other dataset (it should be the first option).

A third area now appears: *[3] Key columns*. Click on *SOURCE COLUMN* and select the column from the source dataset which contains the name or code for the area (e.g. "Constituency" or "ONS code").

Click on 
