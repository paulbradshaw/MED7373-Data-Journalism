# Creating a sortable table


## Level 1: Using the `sortable` JavaScript library

[Sortable](http://github.hubspot.com/sortable/docs/welcome/) is a very simple JavaScript library which helps you turn a basic HTML table into one that people can sort on any column.

*(A library, by the way, is just a collection of commands that someone else has written to solve a common problem)*

To use it, you only need to make sure your webpage has a HTML table, and do 3 things:

1. Add a link in your HTML to the `sortable.min.js` JavaScript library
2. Add a link in your HTML to the `sortable-theme-light.css` style sheet (or one of the other style sheets published by the creators)
3. Add `class="sortable-theme-light" data-sortable` to the `<table>` tag in your HTML

Below I've outlined each step. You'll also need to make sure your webpage is hosted somewhere that you can edit the HTML to include JavaScript links. GitHub Pages, for example, allows you to host webpages. I've [explained more about that here](https://github.com/paulbradshaw/tables/blob/master/githubpages.md).

## Turn your spreadsheet into a HTML table using Tableizer

[Tableizer](http://tableizer.journalistopia.com/) is a web-based tool which will turn data from a spreadsheet into a HTML table.

Specifically, once you have:

1. Copied your data from Excel, Google Sheets, or anywhere else;
2. Pasted it into the box at [tableizer.journalistopia.com](http://tableizer.journalistopia.com/);
3. Clicked the *Tableize It!* button

...you will be presented with a box full of HTML code that you can copy and paste into webpage HTML.

Copy that code but after you paste it, make sure to delete the following:

* Delete all the style information from `<style type="text/css">` all the way to `</style>`
* In `<table class="tableizer-table">` delete `class="tableizer-table"` so you just have `<table>`
* Likewise, in `<tr class="tableizer-firstrow">` delete the class attribute so all that remains is `<tr>`

This is because you will be adding attributes that make this table sortable.

## Adding attributes to your table

Now that you have deleted the class attribute from the table and tr tags, you need to add a new attribute:

Change the `<table>` tag so that it now reads `<table class="sortable-theme-light" data-sortable`>

This means that the table will be affected by any style sheet or JavaScript that targets those attributes.

The next step is to link to just that: a style sheet and JavaScript which will affect this table.

## Linking to the JavaScript

Between the `<head>` and `</head>` tags in your webpage HTML, paste the following code:

`<script src="https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/js/sortable.min.js"></script>`

`<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/css/sortable-theme-light.css" />`

The first grabs the `sortable` JavaScript library, and the second grabs the CSS file for the 'light' theme, from a website called CDNJS.

CDNJS hosts JavaScript libraries and CSS files so they can be served more quickly. Whenever you are using JavaScript libraries it is a good idea to look for a version of CDNJS. Specifically, [here is the page for the sortable files](https://cdnjs.com/libraries/sortable).

There is more than one theme. If you are going to try a different one, remember you will need to change both the CSS file being imported, and the `class` attribute of the table that it affects.

## Test it out

Once you've made those changes, save (or commit, if using GitHub Pages) your changes, and test the results. However, note that changes do not show immediately live at your github.io address - you may have to wait a few minutes.

Tip: The article [Design Better Data Tables](https://uxdesign.cc/design-better-data-tables-4ecc99d23356) outlines a number of ways to improve the usability of your tables.
