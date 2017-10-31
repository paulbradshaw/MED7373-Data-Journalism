# Working with an API in JavaScript

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

We are going to use the JavaScript library jQuery to work with the API. In Codepen this can be added quickly by going to *Settings*, switching to the *JavaScript* tab, and then using the *Quick Add* drop-down menu at the bottom to select **jQuery**.

This will add a link like this to the boxes above: `https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js`

Alternatively, you can import the jQuery library in the HTML like so:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
```

## Use `get` to grab the data from the API

With the jQuery library imported into our document, we can use the `get()` function to grab the JSON from the Police API.

Because `get()` is part of jQuery, you need to use it with a dollar sign (which means 'jQuery') and a period like so: `$.get()`. Inside the parentheses, you specify the URL of the JSON you want to grab, like so: `$.get("https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592"`

This is followed by a comma, and a `function()`, outlining what name you want to give to the information, and what you want to do with that. Here's the code, followed by more explanation:

```js
$.get("https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592", function(crimes) {
  // Define what the function does
  //crimes is made into Jquery object, .each loops through, performs new function
  // Start 'for each' loop. Run function naming variable 'crime' and index as 'index'
  $(crimes).each(function(index, crime) {
    //Use console log to show crime name
    console.log(crime);
    // change to != to see all other crimes
      $('.crimes').append($('<tr class="row"><td><a href="http://data.police.uk/api/outcomes-for-crime/' + crime.persistent_id + '">' + crime.category + '</a></td>'+ '<td>' + crime.location.street.name + '</td></tr>'))
    
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


## Specify what to do with `each` item of data from the API
