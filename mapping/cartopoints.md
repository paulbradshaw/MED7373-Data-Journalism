# Creating a map of points in Carto

Create an account on Carto.com, and log in.

Click 'New map'

Click 'Connect dataset'

Click 'browse' and find the CSV of crimes you downloaded from [the data.police downloads page](https://data.police.uk/data/). What? You haven't yet. Go on then. I'll wait here...

Once your data has uploaded to Carto you can either 'Take a tour' or edit your map. Edit it.

Because the columns are called 'latitude' and 'longitude' it automatically maps them (on the right). That's not always going to be the case.

On the left you can see a 'layers' column with the data there. Click on it to open it.

A new menu appears with 5 options:

* Data
* Analysis
* Style
* Pop-up
* Legend

You should be in 'Style'. This has 2 sections: [1] is *Aggregation*. This has a series of types of map types (individual points, squares, hexagons, heatmap, torque, etc.). [2] is Style (again). We'll focus there first.

Click on the size/colour box, and a window should appear. At the top it has 'SOLID' selected, but next to that is 'BY VALUE'. Click that. You can now select the column that you want to colour code the points by. Once you do, you can then customise colours by category or numerical range.

Try the other aggregation options above. How does that change the type of story you might tell?

## Pop-ups

The Pop-up menu allows you to customise what information is displayed when someone clicks on, or hovers over, one of your points or areas. Switch between 'Click' (on the left) and 'Hover' to customise the options for each: first [1] is the style of the box that appears, and underneath that is [2] *Show items* where you can specify what data is displayed. At the bottom is a toggle switch where you can change from *Values* (a basic list) to *HTML* (customisable code which allows for more control over how the values are integrated)

## When you don't get a map immediately (latitude and longitude are not recognised, or you have postcodes/etc. instead)

A warning symbol will appear next to the data. If you hover over this it will tell you "Layer doesn't have geometry". If you click on the data it will say even more clearly:

> "There's no geometry in your data that could be styled. Please georeference or manually add data to visualize."

Click the **Georeference** button. This will open the *Analysis* tab with 3 areas underneath: [1]: Your workflow; [2] Georeference and [3] Parameters.

In the *Georeference* section there should be two boxes: *INPUT* and *TYPE*. The latter will show *Longitude and latitude*. You can click on this to select other types of geo information: cities, countries, administrative regions, postal codes, IP addresses, and street addresses.

If you have longitude and latitude in your data, move to section [3] with the *Parameters*. Click on *LATITUDE* and select the field (column) with latitude in. Click on *LONGITUDE* and repeat the process for that column.

If your data does not have two separate columns like this, you'll need to split them first before uploading the data.

If your data has postcodes, select *Postal codes*. The area underneath - [3] Parameters - should adjust to reflect this, with boxes for *POSTAL CODE* and *COUNTRY*.

Click the *POSTAL CODE* box and select the field from your dataset which contains postcodes.

Click the *COUNTRY* box and select the field which contains the country. Quite often there isn't one, because the creator of the dataset assumed everyone knows where the locations are. So you may have to start again - go back to your dataset and add a country column with the same country in every cell - before re-uploading your data and starting again.

The same process can be followed for other types of geographical information. Remember that this process - *geocoding* - is not exact, and can result in incorrect placing of data records where an address is misunderstood, etc. So be careful, and of course check your map whatever the case.

You may also get a warning that *"We're sorry the current quota is insufficient to enrich your data"*. This means that you have used up your free account's allocation of geocoding using Carto's Data Services API - [more details on Carto](https://carto.com/docs/carto-engine/dataservices-api/quota-information/). You may want to geocode using a different API (such as postcodes.io), or mapping tool (such as Google Fusion Tables, before exporting as KML) first, before bringing data into Carto.
