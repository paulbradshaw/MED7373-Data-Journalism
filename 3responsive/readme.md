# Responsive design and mobile UX

In line with industry practice, we are adopting a 'mobile first' approach to data journalism. This means thinking from the start about how our data journalism might be experienced on mobile phones, and building from there.

## Basic web design principles: HTML and CSS

Before continuing, you should ensure that you understand basic principles of HTML explored in the background reading and in class. That includes:

* HTML tags, attributes and values - what they do, and the differences between them
* When to use a `id` attribute and when to use `class`
* When to use a `<div>` tag and when to use `<span>` (block elements vs inline elements)
* How CSS selectors work
* How CSS rules work

If you don't feel that you can explain those, revisit the readings and other resources online.

## Mobile UX vs responsive design

It is important to distinguish between responsive *design* and mobile *UX*: responsive design is merely the technical processes you need to understand to make web content look different depending on the device (to *respond*, in other words). But you also need to consider more broadly what the user *wants to do* with your content, and *how* they might do that. This is explored in the lecture.

To complicate things a little further, there are a number of options to choose from when creating a mobile user experience. These include:

* A separate mobile site (typically beginning with `m.`, e.g. `m.mywebsite.com`) which is served to visitors from mobile devices
* A web app: a webpage designed to look and behave like a mobile app
* A website using responsive design: the layout of the screen is dynamically adjusted based on the screen being used (phone, phablet, tablet, desktop, etc.)
* Adaptive design: the server loads the version (and assets) of the site for that particular device

## Tools: Codepen, GitHub, Atom and the inspector

Before getting started it's worth mentioning four tools which are likely to come in useful throughout the process of designing web pages.

## Codepen

A good way to test out some web design techniques is to use a service like [Codepen](https://codepen.io/). This allows you to write HTML, CSS and JS (JavaScript) on the same screen, and see the results live. It also allows you to easily load popular libraries and clone/fork code ('pens') by other users. Once you're happy with a webpage you can export it as a zip file containing separate HTML, CSS and JS files. These can then be hosted on a service like GitHub Pages, and edited in a text editor like Atom (see below).

### GitHub Pages

Although you can create individual pages on Codepen, at some point you'll want to move beyond that and create larger projects. An easy way to do that is GitHub's 'Pages' service. This allows you to create a website based on a particular repository. Typically, the GitHub.com repository then acts as a 'behind the scenes' for the live website (which is at a different github.io address).

I have written a [guide to creating websites using GitHub Pages here](https://github.com/paulbradshaw/introtogithub/blob/master/githubwebsites.md).

### Atom or other text editors

When you move from Codepen to GitHub you will need a text editor to edit your HTML, CSS and JS files. Popular text editors for coding include Atom (owned by GitHub) and Sublime Text. These are better than general text editors such as Textedit because they include automatically completing brackets and quotes, and colour coding to distinguish different elements, and alert you to potential problems. They also look a lot cooler!

### The inspector (Web Developer Tools)

A final tool to know is the web browser's built-in 'Inspector', opened by right-clicking on a page and selecting 'Inspect' or 'Inspect element', or by clicking on the View menu and selecting Developer > Tools (in Chrome) or Tools > Web Developer > Inspector (in Firefox).

Chrome and Firefox have particularly good inspectors. While testing your webpage in a browser the inspector allows you to identify elements, try out code, and see any errors your webpage is generating (in the Console).

One of the most basic things the inspector can do is [simulate mobile devices, using device mode](https://developers.google.com/web/tools/chrome-devtools/device-mode/). Try looking at that page in mobile mode, for example, and you'll notice the hamburger menu, the right hand navigation options disappearing, and the cursor changing to a circle (akin to a finger 'tap').

## Responsive design: get started

Try some of the following techniques in a code editor like Codepen. Then export them to your computer, unzip, and add to a GitHub repo (make sure to retain the file structure). Finally, generate a GitHub Pages website that uses those files as their basis (they'll need to be in the main repo, a folder called 'docs', or a branch called 'gh-pages').

### Setting the viewport

The first thing we need to do is add a `meta` tag that tells the device not to scale the webpage. If you forget to add this tag then a mobile device will still try to show the whole page, despite any CSS telling it to do otherwise. Here's the tag:

`<meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>`

And here's the HTML 'skeleton' of the page with that line added:

```html
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta content='text/html' charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>
    <title>Put your page title here</title>
  </head>
  <body>

  </body>
</html>
```

### Loading the stylesheet(s)

The next thing is to link to the stylesheet(s) that contain the rules for our page. It might look like this:

`<link rel='stylesheet' href='styles.css'>`

Or, if we've put it in a separate folder called 'css', it will look like this:

`<link rel='stylesheet' href='css/styles.css'>`

Here's the full HTML with that line too:

```html
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta content='text/html' charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>
    <link rel='stylesheet' href='css/styles.css'>
    <title>Put your page title here</title>
  </head>
  <body>

  </body>
</html>
```

### Adding some text

We just need to add some text which we can then style in different ways for different devices. Ideally you want to plan this out as a structure, with `<section>` tags for each section, perhaps a `<div>` tag for the whole page, and so on. But for this exercise we just need some basic text for now. We'll add a heading and some paragraph text.

```html
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta content='text/html' charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0, maximum-scale=1.0'>
    <link rel='stylesheet' href='css/styles.css'>
    <title>Put your page title here</title>
  </head>
  <body>
    <h1>Man bites dog</h1>
    <p>Police are asking witnesses to come forward after a dog was assaulted in Central Park this morning.</p>
  </body>
</html>
```

### Creating the stylesheet

Now to style that. The stylesheet obviously needs to be in the same place that was linked to from the HTML file.

At the top of the stylesheet should be any extra fonts that you want to load (we're not using any here). Then comes the 'normal' styles, and finally the responsive styles, which begin with `@media`.

Below is an example you can adapt. It has four sections:

* First, a normal CSS rule uses the `body` selector to select everything in the `<body>` tag, and apply a font-family to that.
* Second, the first `@media` rule specifies that this will apply to screens with a maximum width of 400 pixels - in other words, mobile phones. Within that, another `body` selector now specifies a background-color and text colour
* Third, another `@media` rule specifies that this will apply to screens between 401 and 960 pixels in width - tablets. Within that, a selector specifies a width and margin to use for the `<body>` tag on those devices
* Finally, a third `@media` rule specifies that this will apply to screens with a minimum width of 961 pixels - monitors. Within that, a similar selector now specifies a width and margin.

```css
body {
  font-family: arial;
}


/* Mobile Styles */
@media only screen and (max-width: 400px) {
  body {
    background-color: black;
    color: white;
  }
}
/* Tablet Styles */
@media only screen and (min-width: 401px) and (max-width: 960px) {
  body {
    width: 380px;
    margin: 0 auto;
  }
}
/* Desktop Styles */
@media only screen and (min-width: 961px) {
  body {
    width: 570px;
    margin: 0 auto;
  }
}
```

Try these rules in your CSS file and then check the results. You can [see an example of similar rules in my pen here](https://codepen.io/paulbradshaw/pen/mBwZeZ).

Play around with other things you might want to change on different sized screens.

## Responsive images

One of the biggest challenges in responsive design is images: smaller devices on mobile connections might not need large images, or as many images, as desktop users. Here's an example of HTML code which loads one of two images depending on the width of the screen:

```html
<img src="https://www.restedface.com/wp-content/uploads/2014/03/medium-dog-breeds-pictures-and-names.jpg" srcset="https://i.ytimg.com/vi/VVeLuvzcVuA/maxresdefault.jpg 1280w, https://cmeimg-a.akamaihd.net/640/cme/cuteness_data/s3fs-public/diy_blog/What-Qualifies-as-a-Medium-Sized-Dog.jpg 864w" sizes='(min-width: 1000px) 1000px, 100vw' class="pic" />
```

Let's pick that apart:

First we have a default image:

`<img src="https://www.restedface.com/wp-content/uploads/2014/03/medium-dog-breeds-pictures-and-names.jpg"`

Then there is a `srcset` attribute which specifies multiple (a set of) image src urls, and after each a specific width (a number followed by `w`):

`srcset="https://i.ytimg.com/vi/VVeLuvzcVuA/maxresdefault.jpg 1280w, https://cmeimg-a.akamaihd.net/640/cme/cuteness_data/s3fs-public/diy_blog/What-Qualifies-as-a-Medium-Sized-Dog.jpg 864w"`

These two `w` numbers - `1280w` and `864w` specify the width of those images. As soon as the width of the screen hits 864 pixels and lower, that image is loaded.

Next, the `sizes` attribute defines a minimum width `(min-width)` at which the image is rendered at a particular specified width (`1000px`), otherwise it takes up `100vw` - 100% of the viewport width.

`sizes='(min-width: 1000px) 1000px, 100vw'`

Finally, a `class` attribute:

`class="pic"`

This is used to style the picture as 100% width in the CSS:

```css
.pic {
  width: 100%;
}
```

## Responsive frameworks

Thankfully, there are a number of responsive frameworks for webpage designs which you can adapt for your own project. [Get started with this tutorial on one of the best known: Bootstrap](https://github.com/paulbradshaw/jsintro/blob/master/responsive/bootstrapintro.md)

## Accessibility

Check your site for accessibility. Do you have:

* `<alt>` tags on images?
* `<html lang="en">` language declared
* `<h>` tags used meaningfully (e.g. `<h1>` for main title, `<h2>` for headings, and so on)
* The use of meaningful tags for sections, e.g. `<main>`, `<section>`, `<aside>`, `<article>`, `<nav>`, `<button>` etc?
* Enough contrast in your text and background colours - [use this tool](https://leaverou.github.io/contrast-ratio/#blue-on-red) to test them (it should be at least 4.5-to-1)
* Not using colour alone as the only source of information
* Readable text
* `@media` print style
* If you are hiding content you are [doing so appropriately](https://medium.com/@matuzo/writing-css-with-accessibility-in-mind-8514a0007939)
