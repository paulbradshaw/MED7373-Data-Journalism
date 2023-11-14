# Creating a sortable table

[Watch a video walkthrough of this tutorial](https://www.youtube.com/watch?v=4G37OQHv-Lc)

This tutorial explains how to add some JavaScript (and CSS) to a webpage to turn a basic HTML table into something a bit more interactive (and better-looking).

## Using the `sortable` JavaScript library

[Sortable](http://github.hubspot.com/sortable/docs/welcome/) is a very simple JavaScript library which helps you turn a basic HTML table into one that people can sort on any column.

*(A library, by the way, is just a collection of commands that someone else has written to solve a common problem)*

To use it, you only need to make sure your webpage has a HTML table, and do 3 things:

1. Add a link in your HTML to the `sortable.min.js` JavaScript library (this creates the interactivity)
2. Add a link in your HTML to the `sortable-theme-light.css` style sheet (or one of the other style sheets published by the creators) (this creates the style)
3. Add `class="sortable-theme-light" data-sortable` to the `<table>` tag in your HTML (this means your table is 'targeted' by the libraries above)

Below I've outlined each step. 

You can follow these steps in a 'code playground' like Codepen.io, which allows you to preview the page and see it working instantly, as well as exporting the HTML file so it can be published on the wider web. GitHub Pages, for example, allows you to host HTML pages and other files. I've [explained more about that here](https://github.com/paulbradshaw/tables/blob/master/githubpages.md).

Alternatively, you can create HTML pages directly in GitHub and publish it on GitHub Pages using the same steps (there is a delay between updating your files and seeing the results working 'live', however).

## Step 1: Create a HTML table (you can use Tableizer)

HTML tables can be coded by hand, but it's much easier (and more common) to find a tool that will do it for you. 

[Tableizer](http://tableizer.journalistopia.com/) is one widely-used web-based tool which will take data pasted from a spreadsheet, and turn it into a HTML table (note: it may crash if you try to paste too much data into it). *If you need a table of data, you can [try the table shared here](https://docs.google.com/spreadsheets/d/1QecM3UWioAgpYPFg9bbnxMHtTROYMrqP_jzlpkUZKNo/edit?usp=sharing).*

1. Copy your data from Excel, Google Sheets, or anywhere else
2. Paste it into the box at [tableizer.journalistopia.com](http://tableizer.journalistopia.com/) - and tick the 'No CSS' box
3. Click the *Tableize It!* button

You will then be taken to a new page with a box full of HTML code that you can copy and paste into webpage HTML (plus a handy button saying 'Copy HTML to Clipboard' which does just that).

Copy that code and paste it into your HTML webpage (e.g. the HTML window on Codepen). 

Once you've pasted the HTML, check that it hasn't got any extra styling information. If you remembered to tick 'No CSS' it shouldn't, but just in case:

* Delete any style information between the tag `<style type="text/css">` all the way to `</style>` (if you can't see any, that's even better)
* If the table starts with `<table class="tableizer-table">` delete `class="tableizer-table"` so you just have `<table>` (if you just see `<table>` then that's already fine)
* Likewise, if in the next row you see the tag `<tr class="tableizer-firstrow">` delete the class attribute and its value so all that remains is `<tr>` (and again, if there is no `class=` attribute, you don't need to clean this up)

We need to delete those stylings because we will be adding our own.

## Step 2: Add attributes to your table

Now we need to add a new attribute which can be targeted by some JavaScript and CSS.

Change the `<table>` tag so that it now reads `<table class="sortable-theme-light" data-sortable`>

This means that the table will be affected by any style sheet or JavaScript that targets those attributes. Let's now add those.

## Step 3: Create script links to the JavaScript & CSS 

The JavaScript and CSS files are hosted on a website called [CDNJS](https://cdnjs.com/). CDNJS hosts JavaScript libraries and CSS files so they can be served more quickly, and so that you don't have to host them yourself. Whenever you are using JavaScript libraries it is a good idea to look for a version on CDNJS. Specifically, [here is the page for the sortable files](https://cdnjs.com/libraries/sortable).

**If you are using Codepen** it will generate the script links for you. To do this, click on **Settings**. 

In the window that appears you should see options on the left for the three views: HTML, CSS and JS (JavaScript). 

Select the **JS** view. In the *Add External Scripts/Pens* section (*below* the search box) paste this URL: 

`https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/js/sortable.min.js`

Switch to the section headed **CSS** and again scroll down to *Add External Stylesheets/Pens* then paste this URL into the empty box underneath the search box: 

`https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/css/sortable-theme-light.css`

Click **Save & Close**. You should see the table now looks different in the preview, and you can click on the heading of any column and it will sort the table by that column.

If you click **Export** in the bottom right corner, then choose *Export .zip*, it will export a zipped folder which, when unzipped, should contain a folder called 'dist' with a HTML file containing the HTML for your table *and* the links to the external CSS and JS files which it will use to make that table interactive. You can now upload this to GitHub Pages or another web hosting platform.

Note that changes do not show immediately live at your github.io address - you may have to wait a few minutes.

### Where to find the script links

JavaScript and CSS script links are normally inserted between the `<head>` and `</head>` tags in your webpage HTML. If you look at the raw HTML of the page you exported, you should see this code:

`<script src="https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/js/sortable.min.js"></script>`

`<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/css/sortable-theme-light.css" />`\

The first of those two links grabs the `sortable` JavaScript library, and the second grabs the CSS file for the 'light' theme, from that website CDNJS.

If you were editing the HTML directly in GitHub, rather than in Codepen, this is where you would put the links to the two libraries.

### Further tips

Tip 1: There is actually more than one theme - you could link to a different one to style the table differently. If you are going to try a different one, remember you will need to change both the CSS file being imported, and the `class` attribute of the table that it affects.

Tip 2: The article [Design Better Data Tables](https://uxdesign.cc/design-better-data-tables-4ecc99d23356) outlines a number of ways to improve the usability of your tables.
