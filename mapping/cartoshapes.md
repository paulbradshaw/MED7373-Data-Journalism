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

Click 'browse' and find
