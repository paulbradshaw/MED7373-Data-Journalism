# Notes on QGIS

*Download the [country shape files from Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/) - [Download countries](https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip) and unzip to your working folder first.*

## Adding points

In QGIS go to *Layer > Add Layer > Add Delimited Text Layer...* then on the window that appears click *Browse* and find the `.csv` file containing your locations (lat and long). Click *Open*.

Now in the window make sure that **CSV (comma separated values)** is selected - if it is a preview should be visible in the bottom part of the window.

Make sure that **Point coordinates** is selected if you have latitude and longitude in your data.

Look for the **X field** drop-down menu - this will automatically select fields called 'Longitude' or similar, but if your data doesn't have that then you can select your longitude column there.

The same applies to the **Y field** drop-down menu, which should have your latitude column selected.

## Adding shape files

In QGIS go to *Layer > Add Layer > Add Vector Layer...* then on the window that appears click *Browse* and find the `.shp` file in the unzipped folder. Click *Open*.

(Alternatively you can click and drag the `.shp` file into QGIS)

You should see the shapes of all the countries now in QGIS.

On the left hand side, in the *Layers Panel*, you should see the name of the file you've just added.

Right-click on that layer and select *Open Attribute Table* to see the data for the countries in a table.

Right-click on that layer and select *Properties* to see information on styles, legends and other elements that you can customise.

## Joining data to shape files (for colouring)

In QGIS go to *Layer > Add Layer > Add Delimited Text Layer...* then on the window that appears click *Browse* and find the `.csv` file containing your quantitative data for the locations. Click *Open*.

Now in the window make sure that **CSV (comma separated values)** is selected - if it is a preview should be visible in the bottom part of the window.

This time you need to make sure that **No geometry (attribute only table)** is selected. Click **OK**.

Both your shape files layer and the new layer need to have some data in column: typically this would be codes for each area, or possibly names (this can be tricky as some names may differ slightly and will not be matched).

Right-click on the shape layer and select **Properties**.

On the window that appears click on the **Joins** button on the left. Now click the + sign to add a new join. Select the *Join field* from one dataset that you want to match, and the corresponding *Target field* from the other dataset. Click **OK**.

The data from the CSV is now in the shape file, and can be used to colour it accordingly.

## Styling shapes for choropleth maps

Right-click on the shape layer and select **Properties**.

Select the **Style** (in some versions of QGIS) or **Symbiology** (in others) option on the left.

The drop-down menu at the top will say something like 'Single symbol' - this means all country shapes are the same colour. Change it to **Graduated** to specify that we want to use different colours based on a particular variable.

In the *Column* drop-down menu underneath, specify the column containing the data you want to use to colour code by. Note that this data needs to be in the shape file dataset, so you'll need to have joined it from your other dataset first (see above). Typically joined data will be at the end of the list.

There are some extra options below this, which you can customise later, then an area with 'Classes' and 'Histogram' tabs. This will show you what classes it is going to be using to categorise - and therefore colour code - different countries. At the moment it is empty, so...

Click **Classify** underneath that area. It should automatically fill the area above with classes for your data based on the field you selected.

Note the *Mode* drop-down menu above: this specifies the way that it is classifying. 'Equal interval' means it will break up the values into equal intervals (each class covers the same range of numbers). Other options will class differently: quantiles, for example, will break up your items so there is a same number in each class.

To the right there is a *Classes* drop-down menu: this can be changed to increase or decrease the number of classes.

You can click **Apply** to see the effect on the map behind this window.

Now it's time to look at the colour scheme, and ask if it's appropriate: you can change it in the *Color ramp* drop-down. Note that some options here use more than one colour: 'PuOr' for example runs from purple to orange. This is a *diverging colour scheme* and is appropriate for maps where you want to show a *divergence* from a baseline - the most obvious example is showing temperates above or below zero (they diverge from zero), but you might also want to show divergence from a national average, or regulatory requirement etc.

You might be tempted by fancy schemes such as 'Inferno'. Be careful here: chances are you are adding visual information that means nothing. Keep it as simple as possible, just like news writing.

When you're happy, click the **OK** button to return to the map.

## Styling borders for choropleth maps

Right-click on the shape layer and select **Properties**.

Select the **Style** (in some versions of QGIS) or **Symbiology** (in others) option on the left.

Next to *Symbol* is a button that says **Change...**. Click this.

A new *Symbol selector* window should open.

Select **Simple fill** in the window at the top.

In the *Outline* (or *Border color* in some versions) option underneath, you can click the box to change the colour of outlines (white is often used as a preference to black).

Click **OK** to confirm, then back in the main window click **Apply** to see the effect.

## Editing maps

You can edit maps to create new ones - for example focusing on particular parts of the world or a country. However, you need to make sure you don't change the original shape file that you downloaded.

To avoid this, first duplicate the layer that you are using: right-click on the layer and select **Duplicate**.

Now you should see two layers with very similar names. To avoid confusion, right-click on the new duplicate layer and select **Rename** - give it a name that distinguishes it.

Now, make sure that you have that layer selected. Untick the other layers so you can only see this one.

To edit maps (remove countries etc.) select the *Select* button in the menu: it's a white arrow against a yellow square which is itself inside a dotted line square, towards the right.

Select what you want to remove. It will be highlighted yellow.

To select the inverse of this, look for a similar button to the right. If it is part yellow and part white and says 'Invert Feature Selection' when you hover over it - that's it. If it's got a curly E (backwards 3) on it, click the drop-down menu on the button to find the 'Invert Feature Selection' button described and click on it.

Click the *Edit* button in the menu's second row: it is a pencil icon to the left. The edges of the countries should become thick and red.

Now you can press your Delete key to delete what is selected.

Click the *Edit* button (the pencil button) again to exit editing mode. You will be asked to confirm this. Click **Save**.

Now right-click on the layer and select **Export** (or **Save As...** in some versions).

A window will appear where you can specify how this is going to be saved. Next to *File name* type a name, and click the **Browse** button to find a place where you can save it - it is a good idea to create a new folder because this will save 5 different files all together so you want them to be in their own folder.

Click **OK** when you're finished and you should now have a new set of shape files that you can use in other maps too.

## Creating a dot density map

A dot density map creates dots *inside* a shape file to represent the density of some value associated with that shape. The most obvious example is population, but it could be crimes, incidents of disease, employment, and so on.

Click on the **Vector** menu, then select **Research Tools > Random points inside polygons (variable)**.

A window will open for you to specify how you want this done. Firstly, you need to specify the layer containing the shapes you want to place the dots in. Second, you need to specify which *column* is going to be used to control the density of these dots: in other words the column containing population, or crimes, etc.

There are other options, too, but these are the main two. Once those have been specified, click **OK** to create the dot density map.

On the left now you should be able to see the new layer, to save it, and to export it as a shape file in its own right.

## Counting points in polygons

Once you have some points on a map, go to the **Vector** menu, and select **Analysis Tools > Count points in polygon**.

The top half of the new window allows you to select the layer with polygons in it - this would be the layer for country shapes, regions etc. - whatever you want to use as a measure.

Underneath that you select the layer containing the points, e.g. crimes, accidents, etc.

Click **Run**.

You should see a new layer appear in your document. This might be called *Count*.

Right-click on that new layer and select **Open Attribute Table**.

This has the areas from the shape file but go to the far right of this table and you should see a new column/field called *NUMPOINTS*. This specifies the numbers of points within each of the specific shapes (polygons).

This can be used to colour-code the shapes: right-click on the Count layer and select **Properties**, then in the *Style* area, change it from single symbol to **Graduated**, and pick the *NUMPOINTS* as the *Column* to colour code by, and finally use the **Classify** button to classify the colours based on *Equal interval* or another scheme. Click **Apply** to see the results, then **OK** if you're happy.

## Datasets

* [Hospitals in the US](https://hifld-geoplatform.opendata.arcgis.com/datasets/hospitals) - click on Download and select Spreadsheet.
