# Working with an API in JavaScript

This tutorial takes you through using JavaScript and jQuery to pull data from an API and turn it into a live HTML table.

We are using the UK police API at [https://data.police.uk/docs/](https://data.police.uk/docs/) - specifically the [street-level crimes method](https://data.police.uk/docs/method/crime-street/). This allows you to get all crimes for any specified location and date.

To do this you form a URL like this: [https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592](https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592).

The latitude and longitude are specified in the URL. You can also add a month at the end like so: `&date=2017-01`

Open up [that URL](https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592) in a browser and make sure the JSONView extension is installed.

## Create some empty HTML to 'target' with JavaScript

First, we need an empty HTML table which is going to be filled with the data we're grabbing. It has some headings for each column, so you'll need to make sure those headings match with the data that you're about to grab. We've got 3 here:

```html
<table class="crimes">
  <tr>
    <th>category</th>
    <th>location</th>
    <th>street</th>
  </tr>
</table>
```

## Add the jQuery library

We are going to use the JavaScript library **jQuery** to work with the API. In Codepen this can be added quickly by going to *Settings*, switching to the *JavaScript* tab, and then using the *Quick Add* drop-down menu at the bottom to select **jQuery**.

This will add a link like this to the boxes above: `https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js`

Alternatively, you can import the jQuery library in a HTML page like so:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
```

(If you export the project from Codepen, this line will be added to the HTML page)

## Use `get` to grab the data from the API

With the jQuery library imported into our document, we can use the `get()` function to grab the JSON from the Police API.

Because `get()` is part of jQuery, you need to use it with a dollar sign (which means 'jQuery') and a period like so: `$.get()`. Inside the parentheses, you specify the URL of the JSON you want to grab, like so: `$.get("https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592"`

This is followed by a comma, and a `function()`, outlining what name you want to give to the information, and what you want to do with that. [Here's the code](https://codepen.io/paulbradshaw/pen/xPGqqW), followed by more explanation:

```js
$.get("https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592", function(crimes) {
  // Define what the function does
  //crimes is made into Jquery object, .each loops through, performs new function
  // Start 'for each' loop. Run function naming variable 'crime' and index as 'index'
  $(crimes).each(function(index, crime) {
    //Use console log to show crime name
    console.log(crime);
    console.log(index);
    // change to != to see all other crimes
      $('.crimes').append('<tr class="row"><td><a href="http://data.police.uk/api/outcomes-for-crime/' + crime.persistent_id + '">' + crime.category + '</a></td>'+ '<td>' + crime.location.street.name + '</td></tr>')

  }); //Close function
}); //Close get
// }); //Close submit function
//}); //Close document ready
```

After the URL is 'got', then, we get:

`function(crimes)`

This assigns the JSON at the URL to an object we've decided to call 'crimes'. That means we can do stuff with it inside the curly brackets that come next:

```js
{
  $(crimes).each
  ...
  }
```

So firstly, the `$(crimes)` means it is taking that 'crimes' object and turning it into a jQuery object. The data in that JSON is a *list* so next we use `.each()` to go through each item in the list and do something with it.

To understand that better, we need to take a step back and look at `each()` on its own.

## Using `each()` to loop through a list

You can see an example of `each()` in action in [this pen](https://codepen.io/paulbradshaw/pen/YEXJWz). Remember that here also the jQuery library has been added in the Settings.

The first line of JavaScript creates an **array variable**, called `mylist`:

```js
var mylist = [1, 2, 5, 10]
```

An array - or list - is created by using square brackets. Each item inside those brackets is separated by a comma.

Now we can loop through that array using `each()` - but first we need to make it into a jQuery *object* by using the jQuery function `$()` like so:

```js
$(mylist)
```

Next, we *attach* the `each()` function to that object with a period like so:

```js
$(mylist).each()
```

For now those parentheses are empty - but the next step is to fill those with *what we want to do with each object in that list*. And what we want to do is run a function on each object:

```js
$(mylist).each(function(){})
```

Again, I've left the brackets after `function` empty to begin with. In JavaScript functions the first parentheses `()` name the *ingredients* of the function (the **arguments**), and the second, curly brackets, `{}` specify the *actions* that the function should take, typically with those ingredients.

Let's first name the ingredients:

```js
$(mylist).each(function(index, myitem){})
```

This function, then, has two ingredients. This is not accidental: with `each()`, for every item in an array the function gives a name to the **index** (position), and to the **value** of the item. The [documentation for the `each()` function](https://api.jquery.com/jquery.each/) specifies this in its own special way.

For example, our array is `[1, 2, 5, 10]`. It has four values, and four indexes (position 0, 1, 2 and 3 - in most programming indexes start at zero). This means that the `.each()` function will run whatever is inside its parentheses four times, once for each value.

Each time that it runs, it will run this *other* function represented by the code `function(index, myitem){}`. Because this doesn't have a name it is called an **anonymous function**.

So:

1. The first time that it runs, it assigns the index position '0' to `index`, and assigns the value `1` from that array to `myitem`.
2. The second time that it runs, it assigns the index position '1' to `index`, and assigns the value `2` from that array to `myitem`.
3. The third time that it runs, it assigns the index position '2' to `index`, and assigns the value `5` from that array to `myitem`.
4. The second time that it runs, it assigns the index position '3' to `index`, and assigns the value `10` from that array to `myitem`.

Got that? OK, now to specify what it is going to do with those values each time that it runs, by filling in the curly brackets. First, let's drop the closing curly bracket and parenthesis to a new line. I've also added a comment to show where we're going to type next:

```js
$(mylist).each(function(index, myitem){
  //Put the code for the function here
})
```
Now let's put something instead of that comment - two `console.log` commands so we can see those variables that the function creates each time it runs:

```js
$(mylist).each(function(index, myitem){
  console.log(myitem);
  console.log(index);
})
```

If you refresh the page and look at the console now, you should see eight numbers appear in the console: the value, and index, for each of the four items in that array. Try changing the array like so, then refresh and see what happens:

```js
var mylist = ["Paul", "Vic", "Jonny", "Wan", "Carmen", "Sania", "Steve"]
```

This time the values will be different, and there will be more indexes.

Now to show those values on the webpage. To do this we need to *target* or *select* part of the page. To do that we need some HTML on the page with a useful attribute. Here, then, is the HTML for a very small table with the key feature that it has a `class="crimes"` attribute that we can target:

```html
<table class="crimes">
  <tr>
    <th>Your list</th>
  </tr>
</table>
```

Now back to the JavaScript. The selector for `class="crimes"` is `.crimes`. To select it in jQuery we use the `$()` function with that selector in single quotes: `$('.crimes')`. Below you see it added to the anonymous function:

```js
$(mylist).each(function(index, myitem){
  console.log(myitem);
  console.log(index);
  $('.crimes')
})
```

Once selected, we can *chain* more functions or methods to it using a period. One method that is useful for adding extra HTML is `append()` ([documentation](https://api.jquery.com/append/)). Let's do that:

```js
$(mylist).each(function(index, myitem){
  console.log(myitem);
  console.log(index);
  $('.crimes').append()
})
```

Inside `.append()` is the HTML we want to append, as a string. Below I've added the HTML to be appended:

```js
$(mylist).each(function(index, myitem){
  console.log(myitem);
  console.log(index);
  $('.crimes').append('<tr class="row"><td>'+myitem+'</td></tr>')
})
```

Let's take a closer look at that:

`'<tr class="row"><td>'+myitem+'</td></tr>'`

There are actually three parts to this HTML that we are asking to add. And they are combined by using the `+` operator:

```js
`'<tr class="row"><td>'`
`+`
`myitem`
`+`
`'</td></tr>'`
```

Note that the first and last part uses single quotation marks to indicate a *string* of text.

The middle part, however, is not inside quotation marks because it is *not* a string: it is a *variable*: `myitem`. In other words, whatever the value is that the function has grabbed from the array.

The first time that this function runs, then, it grabs `1` (or, if you've changed the array, whatever your first value is), puts it inside `myitem`, and then inserts `myitem` (`1`) between the HTML `'<tr class="row"><td>'` and `'</td></tr>'`. The resulting combination is *appended* to the table with the `class="crimes"`.

In other words, it appends a new row to that table.

Because this function runs for `each` item in the array, it appends four new rows, one each time that it runs - or one for each value in the array. Each time that it runs, the value is different, so the contents of that row is different, but the surrounding HTML is the same.

Had we used a different method to `append`, like `innerHTML`, it may have overwritten the last row. The nice thing about `append` is that it only adds, it doesn't *change*.

Now to apply that within our API code:


## Specify what to do with `each` item of data from the API

Now we know how to loop through an array and do something with `each` (append a row to a table, for example), we can apply that knowledge to the data we are grabbing from the Police API. [Here again is the Codepen](https://codepen.io/paulbradshaw/pen/xPGqqW).

To recap, then, we have that line using `$.get()` to grab the data from the URL, and run a function with it:

```js
$.get(
  "https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592", function(crimes){}
)
```

That anonymous function specifies a name for the data that it gets from that URL - `crimes` - but we need to do something with that in the curly brackets next. Let's move the closing curly bracket down a couple of lines, and add a comment to clarify that:

```js
$.get(
  "https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592", function(crimes){
    //What the function does with that data
  }
)
```
OK, now that data is a list of crimes, which is why we're calling it `crimes`. In other words, an array. So this is where we use `each` to loop through each of those. So let's adapt the code from earlier to specify we want to take `crimes`, and for `each` item, run a function. We're calling the index `index` again, but we'll name each item `crime` so we know it's a single crime.

```js
$.get(
  "https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592", function(crimes){
    $(crimes).each(
      function(index, crime) {}
    )
  }
)
```

Now in the curly brackets we can specify what to do for each crime in the array. Let's begin by sending the data to the console so we can watch it there:

```js
$.get(
  "https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592", function(crimes){
    $(crimes).each(
      function(index, crime) {
        console.log(crime);
        console.log(index);
      }
    )
  }
)
```

Now to use `append` to add a new row to the table for each crime. This time the code is going to be more complicated:

```js
$.get(
  "https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592", function(crimes){
    $(crimes).each(
      function(index, crime) {
        console.log(crime);
        console.log(index);
        $('.crimes').append('<tr class="row"><td>' + crime.category + '</td><td>' + crime.location.street.name + '</td></tr>')
      }
    )
  }
)
```

We're still targeting the `class="crimes"` HTML element using `$('.crimes')` and then appending some HTML using `.append()` but there's a lot more HTML here, and something else I need to explain. Let's break it down:

```js
'<tr class="row"><td>'
+
crime.category
+
'</td><td>'
+
crime.location.street.name
+
'</td></tr>'
```

The main new thing here is that instead of simply naming the `crime` variable, the code adds a period and specifies a *property* of that variable, like so: `crime.persistent_id`

This is because each crime is a JSON *object*. JSON objects can have many properties - in this case each crime has a `category` property and a location with a street property that has a name property.

`crime.category`, then, is looking for a property called `category` within the `crime` object. But `crime.location.street.name` is more complex: it is first finding a `location` property, and then *within that* is looking for a `street` property, and *within that* looking for a `name` property. In this case the `location` property has many other branches that you can dig into. If you have [the page open in your browser](https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592) with JSONView installed, you can hover over an element and see the path to that in the bottom left corner.

Those 2 properties are grabbed and inserted into the HTML, and because there are many many items at that URL, we end up with a very long table. Here's the JS again with comments:

```js
//Use the jQuery get function to fetch JSON data from an API, and run a function on it
$.get(
  "https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592",
  //call the JSON object 'crimes'. This is an array.
  function(crimes){
    //Loop through the JSON array 'crimes' and with each JSON object...
    $(crimes).each(
      //Run an anonymous function. Call the position 'index' and the object 'crime'
      function(index, crime) {
        //Print both to the console
        console.log(crime);
        console.log(index);
        //Select class="crimes" in the HTML and append some more HTML, plus some properties of the 'crime' object
        $('.crimes').append('<tr class="row"><td>' + crime.category + '</td><td>' + crime.location.street.name + '</td></tr>')
      }
    )
  }
)
```

## Further development

* Use JSONView to see what other properties there are in a crime
* See if you can expand the table to add other information.
* You can see outcomes for any individual crime by putting its ID code on the end of the URL `https://data.police.uk/api/outcomes-for-crime/`, like this: `https://data.police.uk/api/outcomes-for-crime/1596e17b83619c0332105beb407e435282314e061474edab28f9b7fd2d771362`. Could you make a link for each crime with this knowledge?
