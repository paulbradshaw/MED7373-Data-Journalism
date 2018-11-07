# Fusion Tables shape files walkthrough

If you want to map some data in Fusion Tables but you want the data to be mapped to regions rather than placemarks, you’ll need to do some preparation, and some fiddling around with what are called shape files. This tutorial walks through the steps involved.

You can [find the first 4 steps in this shared Google doc](https://docs.google.com/document/d/e/2PACX-1vQRKsh1xy3TlkJfSOX_A6UoP1acXqe_jYnBH-ZGH5nW2M0dDaku0junt73GSiTLsErNR0IXqxRytL6P/pub)

## Step 5: Customising the new, merged Fusion Table

When it is finished merging those tables you should get a link to the new, merged table. Click on that link to open up the new table. It should have a tab with a map already in it - and that may already have mapped your data to regions.

If it’s not, click on the drop-down button on that tab and select Location > change to change the column on which the map geocodes. You need to select the *column containing the `kml...`* data.

*Note: sometimes when zoomed out from the map the shapes will appear as points*. Zoom into the map to check if those points change to region shapes.

So you now have shapes. At the moment, however, all those shapes are the same colour. You need to customise this so that each region is colour-coded based on a value in your data.

To do that, click on the drop-down button on the tab again (or you can find it in `Tools`) and select `Change map styles`

In the window that appears, select the **Polygon** option on the left, and then the **Buckets** tab. This allows you to specify more than one ‘bucket’ into which data will fall, and the shapes coloured accordingly. Tick the circle at the top of this window, and from the drop-down menu underneath, select the column that your ‘buckets’ will be based on.

Under that is the area where you specify how many buckets you have; what values they fall into; and what colours are used for each.

For example, you might have 3 buckets: one for those with a value of zero to 10; another for those above 10 and up to 20; and a third for those above 20. Click in the boxes to change the values at which a value falls into one bucket or another.

Next to those values are the colours for each bucket - again, click on these to change them. Ideally you should work out your categories beforehand (the function `=QUARTILE` can help you here - it finds the points between each quarter portion of data)

![](https://lh4.googleusercontent.com/OWhBZmVGcNjj8FtTunNEcn1EGagiK8tRAHXIniix6VWEP2gBzZHWySi3i_dEZWEjAcy0Eh3HPGvRuem8CecFbRwIkH7w5fXx_R3YdGLOXiZ824qLE6t4v9HcYkpA_9_81w)

Once you’ve done all this and saved, you should be able to see the effect on the map.

Buckets aren’t the only way to colour your region shapes. The next tab along on the same window offers you the option of using gradients instead, for a smoother variation between regions.

![](https://lh6.googleusercontent.com/894k1bbgm4BqMzuYrvC3s7470e2ap7nRCa5E6VIDkY6i3AsgmJUqx6a0iFAf15hdBDC4b0TiHiribtF36cXAfvJLmQk32tImDLqsi3sUwgixSVqoHvAutymfu-NCMIbapg)

And if you prepare ahead, you could also add an extra column to your original data with a colour code for each value (the Colorbrewer tool is useful for generating these). This has to be done before the merging process of course, but if you’ve done that you can select those colours on the Column tab in the same window:

![](https://lh6.googleusercontent.com/Fj1cE4f2bAPCsV7cGpqrtgDszPTkQZiSBtjRFoJYwV9OGoqWz3FqtQF9xvcHn8KUbBqhA_BaQ4ei5A3EVwswpvixhGkOkCAgdGQ-oV6FWtK1j3Jh0yWwMje4JGcai3OLdw)

To further customise your colours and specify the opacity, see this guide:
[https://support.google.com/fusiontables/answer/2681556?hl=en](https://support.google.com/fusiontables/answer/2681556?hl=en )

## Step 6: Customising the pop up info window

Finally, you will probably want to customise the info window which appears when someone clicks on any region. At the moment this will probably contain the name of every field in your merged table (including any that you kept from the one with the shape files), and the value.

To simplify it, click on the drop-down menu on the tab or `Tools` menu and select `Customise info window`.

The window that appears has two tabs: **Automatic** and **Custom**.

On the first tab, untick any fields you don’t want on your info window.

Then click on the **Custom** tab.

This will have a chunk of HTML for the info window which looks something like this:

`<div etc...>`

`<b>FIELD TITLE</b> {FIELD TITLE}`

`<b>FIELD2 TITLE</b> {FIELD2 TITLE}`

`</div>`

Ignore the `<div>` tags at the top and bottom and focus on the other lines. These consist of two parts:

* The title of a column, normally inside the tags `<b>` and `</b>` which make it bold.
* The same title, but this time in curly brackets.

The first part is static HTML text. You can change it to anything you like.

The second part is more important: this is the actual data for that column. For example, something that says `{COUNTRY}` in this window will actually say ‘Spain’ on one region, and ‘Italy’ on another, and so on.

A quick piece of customisation, then, might involve you changing the first part to something more meaningful (if your column headings aren’t already a meaningful label), or at the very least a label which includes a colon or similar.

Or you might delete that label entirely if the data itself is self-explanatory. For example, you might decide that ‘Spain’ doesn’t need to be preceded by the label ‘Country:’.

Make a simple change like this, save it, and look at the results (you’ll have to click on a region to see the info window).

But then repeat the process to customise the label further. For example, you might want to write something more free-flowing like so:

`<b>The country of {COUNTRY} has a population of {POPULATION}</b>`

Or this:

`<b>{AGE}-year-old {NAME}</b> from {HOMETOWN} carried the torch in {LOCATION} on {DATE}.`

You can also pull in images and create links if your data contains URLs like so:

`<a href=”{URL}”>Here is the linked text</a> and here is an image: <img src=”{IMAGEURL}” alt=”{NAME}” />`

## Step 7: exploring Fusion Tables further

These are just some of the basic techniques in creating a region map in Fusion Tables with shape files and customised colouring and info windows. There’s more you can do, such as embedding charts within information windows and various other tricks. Search for Fusion Tables on YouTube or explore the Help documentation on Fusion Tables to find out more.

### Recommended links:

* [Thematic maps with Google Fusion Tables (PDF)](https://www.google.com/url?q=http://www.peteraldhous.com/CAR/Making_a_thematic_map_with_Google_Fusion_Tables.pdf&sa=D&ust=1456427139756000&usg=AFQjCNEisa1sI7hwea1Kgd_sdwMEv-veEw) (Peter Aldhous)
* [Video: How to create thematic data maps with Google Fusion Tables](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DReUAlZsJxP4&sa=D&ust=1456427139756000&usg=AFQjCNF50ch8L_hIL64BNz6eZ1zYh7tdEA) (Jack Dougherty)
* [How to make a map with Google Fusion tables](https://www.google.com/url?q=http://simonrogers.net/2013/01/27/how-to-make-a-map-with-google-fusion-tables/&sa=D&ust=1456427139757000&usg=AFQjCNGEr2oRxe3NhL1-5aRuOlHjceJ__w) (Simon Rogers)
* [How to make a choropleth map with Google Fusion Tables](https://www.google.com/url?q=http://www.interhacktives.com/2013/12/02/how-to-make-a-choropleth-map-with-google-fusion-tables/&sa=D&ust=1456427139757000&usg=AFQjCNEwrKfkxyK3EdT4g8YAddlHpXNQag) (Sophie Murray-Morris)
* [Borders and boundaries: 16 Google Fusion border files for you to use](https://www.google.com/url?q=http://simonrogers.net/2013/01/28/borders-and-boundaries-16-google-fusion-border-files-for-you-to-use/&sa=D&ust=1456427139758000&usg=AFQjCNGbMrKJLm-r5sH-at6H--_pPn1M0Q) (Simon Rogers)
* [Scottish local authorities KML](https://www.google.com/url?q=https://www.google.com/fusiontables/data?docid%3D1Mjnnet6Un_HjVSGoOAcsphCfBhSA2bjN9n6V5iU%23map:id%3D4&sa=D&ust=1456427139758000&usg=AFQjCNHqd9gZ7OoNyH_XRE-jLfBzvrdhqA) (fusion table - with Eilean Siar)
* Video tutorial on creating a point-based map:  [https://www.youtube.com/watch?v=ok7gz4nAnFE](https://www.youtube.com/watch?v=ok7gz4nAnFE)
