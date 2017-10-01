# Week 4: Interactivity, visualisation - and JavaScript

> "A new media object is not something fixed once and for all, but something that can exist in different, potentially infinite versions. It is is another consequence of the numerical coding of media, and the modular structure of a media object." (Lev Manovich, [The Language of New Media](http://faculty.georgetown.edu/irvinem/theory/Manovich-LangNewMedia-excerpt.pdf), 2011)

This week focuses on exploring interactivity in data journalism, as you develop skills in JavaScript - and an understanding of how to find and adapt *libraries* designed to solve particular problems.

## Start with a table...

To illustrate the principle of **variability** in new media design, we start with a basic element in data journalism: the *table*.

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

This is because you will be adding attributes that change this table...

## Use the sortable library to make it interactive

Look at the [tutorial on using sortable JavaScript library](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/js/sortable.md) in this repo and apply it to your table. You can [find an example on my Codepen here](https://codepen.io/paulbradshaw/pen/JryomX) too.

## Use the FactMint library to turn it into a chart

Look at my [pens demonstrating the FactMint visualisation library](https://codepen.io/paulbradshaw/pens/tags/?selected_tag=factmint). See if you can adapt your own table so it is turned into a chart.

## Turn the headline into a counter

Add a headline, or a passage of text, which tells a numerical story.

Look at the [tutorial on creating counters in JavaScript](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/js/counter.md) and apply this technique to your number. Again, you can [find examples on Codepen](https://codepen.io/paulbradshaw/pens/tags/?selected_tag=counter). This time there are no libraries involved. But could you find one?

## Add a quiz question

Engage the reader by inviting them to guess whether an amount is higher or lower than another amount. 
