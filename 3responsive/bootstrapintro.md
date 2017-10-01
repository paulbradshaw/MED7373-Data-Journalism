# Intro to responsive web design with Bootstrap

This tutorial is designed to get you started quickly with creating responsive webpages using the Bootstrap framework.

Bootstrap is a collection of CSS and JavaScript files which are designed to make it easy to quickly put together webpages that will work on both mobile devices and desktop monitors ('responsive design').

If you go to the [Bootstrap website](http://getbootstrap.com/) you will find a prominent download link - but you don't need to download it to get started.

In this tutorial you're going to copy and adapt some code to quickly explore the capabilities of Bootstrap and understand how basic responsive design works.

## Step 1: Create the skeleton of a HTML page

A HTML page starts and ends with a `html` tag, and normally has a `head` section (for invisible information *about* the page) and a `body` section (for the page contents). Here is some code that you can copy to create that basic skeleton:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
   </head>

  <body>
   </body>
</html>
```

There are a couple of extra elements here - for example the [DOCTYPE declaration](https://en.wikipedia.org/wiki/Document_type_declaration) and [the `lang=` attribute of the `<html>` tag](https://www.w3schools.com/tags/att_lang.asp). You can click on those links to read more about those if you want to. But I'm going to move on.

## Step 2: Copy the links to the CSS and JavaScript from Bootstrap

In order for Bootstrap to work your page needs to be able to load the Bootstrap CSS file (to control appearance) and the Bootstrap JavaScript file (to control behaviour). The code for that is given on Bootstrap's [Getting Started page](http://getbootstrap.com/getting-started/). I've pasted it below. Copy this and then paste it between your `<head>` tags:

```html
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```

If you want to, you can also add a `<title>` tag, or any other tags that you want to include in the `<head>` section. Once you're happy with that, move on to the `<body>` section.

## Step 3: Copy example code for the Jumbotron template

In that [Getting Started page](http://getbootstrap.com/getting-started/) you will also find a [section showing examples](http://getbootstrap.com/getting-started/#examples) built with the framework. One of these is **Jumbotron**.

We are going to copy the code from that example, and then adapt it.

First, then, [go to the page with the Jumbotron example](http://getbootstrap.com/examples/jumbotron/). Right-click on the page and select **View source** to see the code.

Start copying from just under the `<body>` tag, and copy everything until the closing `</body>` tag.

Now paste that code between your own `<body>` and `</body>` tags. Commit changes, and switch to your GitHub Pages version to see if it's worked (you will need an internet connection).

In case there's any doubt, here is that code in full:

```html
<nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Project name</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <form class="navbar-form navbar-right">
            <div class="form-group">
              <input type="text" placeholder="Email" class="form-control">
            </div>
            <div class="form-group">
              <input type="password" placeholder="Password" class="form-control">
            </div>
            <button type="submit" class="btn btn-success">Sign in</button>
          </form>
        </div><!--/.navbar-collapse -->
      </div>
    </nav>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1>Hello, world!</h1>
        <p>This is a template for a simple marketing or informational website. It includes a large callout called a jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
        <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more &raquo;</a></p>
      </div>
    </div>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">
          <h2>Heading</h2>
          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
        </div>
        <div class="col-md-4">
          <h2>Heading</h2>
          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
       </div>
        <div class="col-md-4">
          <h2>Heading</h2>
          <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
        </div>
      </div>

      <hr>

      <footer>
        <p>&copy; 2016 Company, Inc.</p>
      </footer>
       </div> <!-- /container -->
```

## Step 4: Adapt the code

Now you have a direct copy of the Jumbotron page. But you want to adapt that to your own content. Here's how:

The page consists of a number of elements. These can be broken down like so:

* The navigation, which begins with `<nav class="navbar navbar-inverse navbar-fixed-top">` and ends with `</nav>`
* The main title and text area at the top of the page, which begins with `<div class="jumbotron"> <div class="container">` and ends with `</div> </div>`
* The columns of text, which begin with `<div class="container"> <div class="row">` and ends with `</div> </div>`

The title area can be customised by just changing the text inside tags like `<h1>` (heading) and `<p>` (paragraph). The text across the top of the navigation can also be changed by changing the text between `<a class="navbar-brand" href="#">` and `</a>`.

I'm going to focus instead on how the columns work, because that's the most interesting bit.

### Changing the width of columns

Each row on your page is created by the HTML tag `<div class="row">`

Within each row are several tags like this: `<div class="col-md-4">`. The number 4 in that tag controls the width of the area that text in that tag can occupy. Specifically, it refers to the number of columns used, within a 12-column grid. Let me explain...

Imagine the page is divided up into 12 equal columns. Those 12 columns can be used to order content in a number of ways:

* You can have one very wide 12-column-wide box which takes up the entire page
* You can have two 6-column-wide boxes, each of which takes up half of the page
* You can have three 4-column-wide boxes
* You can have four 3-column-wide boxes
* You can have two 3-column-wide boxes *and* one 6-column wide boxes
* You can have three 3-column-wide boxes filled with text *and* one 3-column-wide box which is left empty to create some white space
* Or you can come up with dozens of other combinations

The first `<div class="row">` contains three `<div class="col-md-4">` tags: in other words, three boxes, each of which is 4 columns wide.

Try changing the number to 3 in just one and see what happens.

You should now have one box with is 3 columns wide, two which are still 4 columns wide, and that leaves a 12th column empty.

Try making all three of them 3, and then adding a new fourth `<div class="col-md-4">` tag (don't forget the closing `</div>` too) to create an extra box of text.

That is how you can create custom layouts using the Bootstrap framework. But they're also responsive...

### Showing how the page responds in a different size window

The quickest way to test a responsive layout is to resize the browser window. Make sure you are on the published page, and click the right edge of your browser to start resizing the window. As you drag the right edge further and further in (making the browser more and more narrow) you should see the columns become more and more narrow too: they are *responding* to the change in width by adjusting their size proportionally.

However, when the width reaches a certain point, something else happens: the layout shifts from three boxes of text across each row (or four if you changed it), to just the one.

This is because, when viewed on a mobile device with a width like this, Bootstrap decides to run each block of text under each other, rather than trying to generate columns of text on a tiny screen.

### Images and 100% width

As well as text you can of course add images or embedded media like video and audio players or maps. If you do this there's a useful tip to keep those responsive as well: set the `width` property to `100%`. Here's an example:

`<img src="http://petplays.co.uk/wp-content/uploads/2013/06/Vocalizations-and-ear-movements-of-a-cat-tips.png" width="100%" style="margin:20px 0px"/>`

When the image tag includes `width="100%"` it takes up the width of the `div` block (not the entire page). This means as the div gets resized, so the width of the image does too. You can [see an example I created here](https://paulbradshaw.github.io/jsplay/bootstrap.html).

Note that I've also added `style="margin:20px 0px"` to create a small margin of breathing space around the image too. This isn't the best way to do it - it would be better to add a CSS style to apply to all images, earlier in the page or in a separate CSS file. But I've done it this way so you can see why it has a margin.

Here's another example of setting the width property on the embed code for an YouTube video:

`<iframe width="100%" height="315" src="https://www.youtube.com/embed/pe5NrtuhX-g" frameborder="0" allowfullscreen></iframe>`

In this case YouTube will give you embed code that already has the width set. You need to make sure you change that from a pixel setting (like `500`) to a percentage setting as shown above.

Note also, however, that if you do this you may end up with videos which are cropped into a vertical format - useful if your video is also vertical, but if you want to avoid this, use wider columns or stick to a fixed width.

The same technique can be used for iframe embed codes for maps and audio players too.

That should get you started with using a basic responsive framework. It's now up to you to customise it further, and learn more about Bootstrap and [its other examples](http://getbootstrap.com/getting-started/#examples) and [components](http://getbootstrap.com/components/).
