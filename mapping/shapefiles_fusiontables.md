# Fusion Tables shape files walkthrough

If you want to map some data in Fusion Tables but you want the data to be mapped to regions rather than placemarks, you’ll need to do some preparation, and some fiddling around with what are called shape files. This tutorial walks through the steps involved.

## Step 1: Preparation: find a Fusion Table with shape files

For Fusion Tables to draw the shapes of your regions correctly it needs to have shape files. These are basically descriptions of the shape of each region. Assuming you’re not going to create them yourself, you have two options:

1. Find a public Fusion Table already containing shape files
2. Download shape files and convert them into a Fusion Table

We’re going to cover the first option - but if that fails, follow [this tip on Fusion Tables Help](https://www.google.com/url?q=http://support.google.com/fusiontables/answer/2592829?hl%3Den&sa=D&ust=1456427139721000&usg=AFQjCNE6Pe1jk7enM93jNt2jXc66E0FBhw).

To find public Fusion Tables, use the specialist search engine at [research.google.com/tables](research.google.com/tables) to look for something like “country borders kml” or “country borders geometry”

![](https://lh5.googleusercontent.com/HW5QcsOKvCIZF5l2BbD9UFP9Chn2SCPwOGKtImyEbvyuly56_5AmuhPWKTR-pWgG_4fGG_Bw6Dsm_7v8V1miuDZDTWAB9sk9kBMkn2hmstCh4fDE8wQxrLnIRfCMfZpPIg)

KML stands for Keyhole Markup Language, a language used to describe geographical data. You want some results like this -

![](https://lh6.googleusercontent.com/mpZmksTjPq7Cxv7WL8gTnTvFYUp0eOWIEkxk0U3SHEgvoac5coRTcinibzQ722hdM59nU2vjVVPdIq6b2KStg-NIFPxP04zT0MdUoFG_uTrt2S09T7u7mDGDy6sLbpJcKA)

Once you find a result which you think covers the regions you’re looking for, click on the table to see what’s inside.
You need to make sure the table has two things:

1. A list of the regions which matches those in your own data (e.g. country names; counties, etc.)
2. A column (it may be called ‘geometry’) which is filled with nothing but this: `kml...`

*Note that Fusion Tables only shows the first few columns* and you may have to click on the **arrow** on the right hand edge of the title row to see further columns.

You can also try a search without ‘KML’, but you want to make sure that the table you eventually use includes that column.
Once you do find a table with both those things, you need to download TWO copies to your computer: one in CSV format, and another in KML format.

The CSV format data can be downloaded from the normal table view: click on `File > Download...` and select the CSV option. You will notice that the KML option is greyed out...

![](https://lh3.googleusercontent.com/yYIqeBN7U86Rzl7TeFO9Q-127zJKLAavAD9MxRco6QlCR1GrPkXvzaX2XIUzv16YyYOD2jXB-l0IHs_ZsLH6KbIXXtEZLjz7ayOe1HS2D2C_fwF1TKmqF7quUBxcPaCGqg)

...but this fusion table should also have a tab which says '**Map of Geometry**'. Click on that to see the data shown on a map - but on this view you can also download the KML file of the data. So, while you are on the map view, click on `File > Download...` again and select the **KML** option. 

This KML file can be used wherever you need shapes - including other mapping tools such as CartoDB - but you need the CSV file to check that the list of entities (such as area names) matches your own.

## Step 2: Match your region names to those in the shape file table

Open the CSV file in a spreadsheet package such as Excel or Google Docs. The geometry/KML column will not make any sense, but ignore that - it’s the list of regions that you need.

![](https://lh4.googleusercontent.com/MFQPR-oOeLBa6WKCc4YnJiufe-RTiM2sScH3C4_q-yuifLAzuwMaHcs-6eu57uwSIbNnBamBA5EIaSlIoCBO2rZ8IozZhuK22z2fUoyVSTIZ3wvWIiLn7dlfH78vxgvshQ)

You need to check that your list of regions matches those in this list. To do that, copy that column into a spreadsheet containing your original data (the data you want to map)...

![](https://lh5.googleusercontent.com/J5SklIKpzNUmchkfxZ27lW5CZUAUmBUfZXVfLmFi9n2SD0ndioGWEtUWhjSwn9kOk7HrVXhyEs4VxifRgmwzs_mi9bNwX_6bq0ZXoCfBuP9IgjNmca7FZ1kQCw58xPThYA)

And use the `VLOOKUP` function to check for matches like so:

![](https://lh3.googleusercontent.com/c3cHIwaqXDX39X0s_r7Tm94uAr9IthVstt6eiQKA8XzWlrjlrqLw7cRp3HAljTqfVkpcjEEQoZE_rscJTg70zMYh_Bch0ZuVrxYDXrYdkjdnZBjSAKbCUAl8R5WfcDVP8Q)

(In the example above, replace `A2` with the cell containing your first region, and shapefileNames with the name of the sheet containing your list of regions from the shape file table. Change `A:A` to the column containing that list.)

Where your region name does not match the name in the shape file table, you will see `#N/A`

Sort your data so those entries come to the top, and clean your data so that it matches. You might have to do this manually.

Now you’re ready to combine the two datasets in Fusion Tables itself.

## Step 3: Create the first Fusion Table

Log in to Google Drive and click on `Create > More > Fusion Table`

(If that option isn’t available, click on ‘Add app’, find Fusion Tables and click `Create table`)

![](https://lh5.googleusercontent.com/pT3xvllJdAGY55PbIBeB20Ph_fapmXwijMtT4wQYidfpft1oMafrYm-Ly6eJek1R-c1UyQnEN7lzTdSpXqFH4rKG6_PlHFu5Xu5Or0667KfEFDaEq_cELxUJUqtIpWjB7A)

You can choose to create a table from a spreadsheet already in Google Drive, or upload one from your computer. Depending where your original data is (not the KML one), find it and **upload** it - uploading from your computer is more reliable, I find.

![](https://lh4.googleusercontent.com/YKrIPIj2DeXYUAkV2m8ew8K3OzBDKXACgeKJu6OHWQWhKmkM4Q86bP1zW9C6qVXA1Zfsa0gLu5KaOxGXaV3GoItfq6bBzNTuZ8BUE7qxypE5F9_PRw4YLo-jfFHvT_5-QA)

## Step 4: Merge with a shape file Fusion Table

Now you have the data you want to map - you need to merge this with the shape file data in order to map it.

There are two ways you can do this. The easiest is to click on `File> Find a table to merge with...`

This will open up a new window where you can once again search public Fusion Tables for one with the data you want to merge with.

![](https://lh6.googleusercontent.com/YbVR461llMVWs67mkGD_JhLsOdQU-ZIF0f6guONqpjdeehJzjgX9T_kcpoJNaRKkEV6HfW7BnedIRwOZs-mEvR3vnzWJqeITdSD07o14I_UQu5KjPbxvw6Lf-Y6iIyJiMA)

You’ve already done this, so you can search for that table again here. The search will use your existing data to help it find results that have a close match, so make sure the drop-down menu at the top of the search window - ‘**Suggest public tables matching on**’ - has the column with your region in selected.

![](https://lh3.googleusercontent.com/i4RQUdDK5vBLdKrZz4wTuaRD7FcKdiHE3icrdHcaXVGCfZdHoDO7JuWSjAoFixv6TJMst16kCzm32X1OdExKO4ZrztoyLh9uVQAJfj0S-PC0Z2qsKqabjrELo2lu6_5yQg)

Once you’ve found the table that you used before, tick it and go ahead with the merge. If, however, you cannot find it at all, you can click on `File > Merge...` and locate the file you’re merging with by copying and pasting a link to it in the box at the bottom.

You will be given the option of which fields you want the new table to keep. The main ones are those we’ve been dealing with so far, but it doesn’t matter if you just keep them all.

**Troubleshooting**: if you cannot find a matching public table this way, but you know one exists, then go back to the specialist search engine at research.google.com/tables and repeat the process in reverse: open the table with your shapes in, and select `File> Find a table to merge with...`

At the bottom of the window that appears is a link to ‘**select a table from Google Drive**’. Click on this to find your own table and merge them this way instead.

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
