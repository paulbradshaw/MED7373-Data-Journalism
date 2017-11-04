# Understanding JSON

The most common data format you are likely to encounter in an API is JSON (JavaScript Object Notation). This is because JSON is a very useful format for storing data.

As its name suggests, this is a format which particularly suits JavaScript, and one of the best ways to understand it is to create and manipulate a JSON object in JavaScript.

## Creating a JSON object

A JSON object opens and closes with a curly bracket: `{ }`. Inside those curly brackets will be one or more 'key-value' pairs, with a colon between the key and the value, like so: `"name" : "Paul"`.

The 'key' comes first, and is similar to a column in a spreadsheet. Note that both the key and the value are inside quotation marks. However, if the value is numerical, you do not use quotation marks - for example: `"age" : 28`.

Here, then, is some JavaScript which creates a very simple JSON object with just one key-value pair:

`var myjson = {"name" : "Paul"}`

If you want to have more than one key, you separate each pair with a comma:

`var myjson = {"name" : "Paul", "age" : 28}`

Objects can be - and often are - more complex than this. We'll come onto that in a minute. First, while things are simple, let's look at how to grab information from inside a JSON object.

## Accessing values in a JSON object

To access one of the values inside a JSON object, you need to specify both the name of the object and the key whose value you want to grab. There are two ways to do this, shown below:

`myjson.name`

`myjson['name']`

In the first example you can see that the object name and the name of the key are joined by a period.

In the second example the object name is followed by square brackets containing the name of the key in single (or double) quotes.

## Try it yourself

To get used to using this format, write some JavaScript which creates a JSON object and then grabs some data from it, to display in the console ([you can see this code in this pen](https://codepen.io/paulbradshaw/pen/XzXpVv)):

```js
<script type="text/javascript"> //Not needed if in Codepen JS window
var myjson = {
  "name" : "Paul", "age" : 28
};
console.log(myjson.name);
console.log(myjson["age"]);
</script> //Not needed if in Codepen JS window
```

Needless to say, you can use other code to show values from a JSON object on the page, or in response to use actions (one button might fetch the value from one key, and so on). It is also often used to draw charts and maps.

## Making the JSON object more complex

At the moment the example JSON object is 'flat': everything in it is on the same level. But JSON is often used in a *branching* structure, with information **nested** within other information. Here's an example:

```js
var mynestedjson = {"title" : "My book", "year" : 2017, "publisher" :{"name" : "Routledge", "location": "Oxford"}}
```

After the first two keys we can see that the third key, "publisher", doesn't have a string or number as a value - it has another set of curly brackets containing a whole new set of key-value pairs.

Here's the same JSON but split across multiple lines so that it's easier to see those branches:
```js
var mynestedjson = {
  "title" : "My book",
  "year" : 2017,
  "publisher" :{
    "name" : "Routledge",
    "location": "Oxford"
  }
}
```

The logic behind these branches makes sense: here we have an object (data about a book) which has some basic properties. The book has:

* A title
* A year
* A publisher

But some of those properties can *also* have properties. In this case the publisher has two properties:

* A name
* A location

To access those properties we just need to extend the same naming convention we used earlier, to specify the next branch. For example:

`mynestedjson.publisher.name`

Or:

`mynestedjson['publisher']['name']`

Each of these is saying 'take the object `mynestedjson`, grab the value for the key `publisher`, then within that grab the value for the key `name`'

Again, you can test that with code like this ([also available in this pen](https://codepen.io/paulbradshaw/pen/GOZQxV)):

```js
<script type="text/javascript"> //Not needed if in Codepen JS window
var mynestedjson = {
  "title" : "My book",
  "year" : 2017,
  "publisher" :{
    "name" : "Routledge",
    "location": "Oxford"
  }
};
console.log(mynestedjson.publisher.name);
console.log(mynestedjson['publisher']['location']);
</script> //Not needed if in Codepen JS window
```

Try changing the code to grab different branches.

## Applying this to JSON from an API

The [Postcodes.io API](http://postcodes.io/) returns data - in JSON format - for any given postcode, if you add the postcode (without any spaces) to the end of the URL `http://api.postcodes.io/postcodes/`. Here, for example, is the URL to get JSON for the postcode B42 2SU: [http://api.postcodes.io/postcodes/b422su](http://api.postcodes.io/postcodes/b422su)

I have pasted the JSON below:

```js
{
  status: 200,
  result: {
    postcode: "B42 2SU",
    quality: 1,
    eastings: 407067,
    northings: 291048,
    country: "England",
    nhs_ha: "West Midlands",
    longitude: -1.89728701783489,
    latitude: 52.5172741346402,
    european_electoral_region: "West Midlands",
    primary_care_trust: "Heart of Birmingham Teaching",
    region: "West Midlands",
    lsoa: "Birmingham 033F",
    msoa: "Birmingham 033",
    incode: "2SU",
    outcode: "B42",
    parliamentary_constituency: "Birmingham, Perry Barr",
    admin_district: "Birmingham",
    parish: "Birmingham, unparished area",
    admin_county: null,
    admin_ward: "Perry Barr",
    ccg: "NHS Sandwell and West Birmingham",
    nuts: "Birmingham",
    codes: {
      admin_district: "E08000025",
      admin_county: "E99999999",
      admin_ward: "E05001200",
      parish: "E43000250",
      parliamentary_constituency: "E14000566",
      ccg: "E38000144",
      nuts: "UKG31"
    }
  }
};
```

You can see that there are 3 different levels in this JSON:

1. At the bottom level are two branches: `status`, and `result`
2. Within `result` are over a dozen branches, from `postcode` to `codes`
3. Within `codes` are another 7 branches, from `admin_district` to `nuts`

The `status` value is a code that represents whether the API query was successful. This is quite common in APIs as it allows you to handle situations where your API query has not worked (you might add a line saying "if this value is not 200, then don't do anything"). To see what a result looks like when the postcode doesn't exist, see [http://api.postcodes.io/postcodes/b42xsu](http://api.postcodes.io/postcodes/b42xsu) - you'll notice the `status` value is `404`, and there's a new `error` value: `"Invalid postcode"`.

Aside from that, we can see that to grab anything from this JSON we're going to have to describe a path of at least two steps: the first to `result`, and the second to one of its sub-branches.

You can play with this JSON by copying and pasting it into your own code, and assigning it to a variable, like so (you can [see this code in this pen](https://codepen.io/paulbradshaw/pen/JOXpem)):

```js
var myapijson = {
  status: 200,
  result: {
    postcode: "B42 2SU",
    quality: 1,
    eastings: 407067,
    northings: 291048,
    country: "England",
    nhs_ha: "West Midlands",
    longitude: -1.89728701783489,
    latitude: 52.5172741346402,
    european_electoral_region: "West Midlands",
    primary_care_trust: "Heart of Birmingham Teaching",
    region: "West Midlands",
    lsoa: "Birmingham 033F",
    msoa: "Birmingham 033",
    incode: "2SU",
    outcode: "B42",
    parliamentary_constituency: "Birmingham, Perry Barr",
    admin_district: "Birmingham",
    parish: "Birmingham, unparished area",
    admin_county: null,
    admin_ward: "Perry Barr",
    ccg: "NHS Sandwell and West Birmingham",
    nuts: "Birmingham",
    codes: {
      admin_district: "E08000025",
      admin_county: "E99999999",
      admin_ward: "E05001200",
      parish: "E43000250",
      parliamentary_constituency: "E14000566",
      ccg: "E38000144",
      nuts: "UKG31"
    }
  }
};
console.log(myapijson.status);
console.log(myapijson['result']['region']);
```

This will work where the API returns a single JSON object, but there's another type of JSON object we need to look at too...

## Dealing with arrays of JSON objects

Many APIs return more than one result when queried. The Spotify API, for example, will return a list of the 10 most popular tracks by an artist. The Police API will return a list of all the crimes reported at a particular location in a given month. The Google Places API will return a list of distances when queried with a list of start and end points.

These lists are called *arrays* and begin and end with square brackets: `[ ]`

By way of example, the Data.police.uk API includes [an API method which will give you a list of all the police forces](https://data.police.uk/docs/method/forces/) that it covers. The URL to query that API is [https://data.police.uk/api/forces](https://data.police.uk/api/forces) (note that you do not need to specify anything).

Here is what you will see at that URL, but with just the first two forces shown:

```
[
  {
    id: "avon-and-somerset",
    name: "Avon and Somerset Constabulary"
  },
  {
    id: "bedfordshire",
    name: "Bedfordshire Police"
  }
]
```

You can see that each force is represented by its own JSON object with two properties: `"id"` and `"name"`.

There are 44 of these objects - one for each of the 44 police forces in England and Wales.

How do we handle data like this? Well there are two things you are most likely to do:

1. Specify *which* item in the list you want, and grab one or more of its values
2. Loop through *each* item and grab one or more of the values

To specify *one* item, you would use an index in square brackets, like so: `[43]`. So if we stored the data in a variable called `myapijson` and we wanted to grab the first item, we would write `myapijson[0]` (`0` is the index position for 'first', because counting begins from zero in JavaScript).

That would allow us to access the JSON object in the *first position* in that array. To then grab the value for `id` we would add `['id']` to the code, like so:

`myapijson[0]['id']`

To loop through and do something with each requires a bit more explanation...

### Looping through an array of JSON objects

Handling an array of JSON by looping through it is the same as handling any array of items in JavaScript generally. There are many ways of doing this - including the jQuery function `each` ('for each item, do this') but one of the most basic you can use is [the `for... of` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of). When used with an array called `myapijson` it can look something like this:

```js
for (item of myapijson){
  console.log(item.id)
}
```

What the code above is saying is: loop through each thing in the array `myapijson` and use `console.log()` to show the value of `id` in that thing.

Here's the same code stripped back to it core elements:

```js
for (INVENT_A_NAME of ARRAY_VARIABLE_NAME){
  WRITE_WHAT_TO_DO_FOR_EACH
}
```

The easiest part to replace is `ARRAY_VARIABLE_NAME` - this should be the name of your array variable. Remember that an array is a *list* because...

The `INVENT_A_NAME` part is where you decide what to call each individual *item* in that list, in the code that follows. This name does not exist anywhere else - it is nothing special, you do not have to find it. It is entirely arbitrary. Sometimes people choose to call it `i`, or you might call it something more meaningful like `force` or `crime` or `item`. But it really doesn't matter.

Next, in the `WRITE_WHAT_TO_DO_FOR_EACH` part, you get to do something with that individual item. If you're dealing with an array of JSON objects, you'll probably want to drill down into it as described previously, to fetch a particular property, and then do something with that.

But you get the basic structure. So, going back to the example:

```js
for (item of myapijson){
  console.log(item.id)
}
```

If `myapijson` contains 44 JSON objects, then this loop will run 44 times. Each time it calls the individual JSON object `item` and then, inside the curly brackets, extracts the `id` value of that, and sends it to the console.

In [this pen](https://codepen.io/paulbradshaw/pen/QONmyM?editors=1111) you can see code which creates a new array containing the data from the data.police.uk API forces URL, then loops through it and displays the `id` value in the console. It even has some buttons which will either grab specific indexes from that array, or loop through and add them all to the page.

## Summing it up

That should give you most of the basics to understand how JSON is structured and how to work with it. Here are the key points again:

* JSON objects are commonly used to supply data from APIs
* JSON objects start and end with curly brackets `{ }`
* JSON uses **key-value** pairs, with a colon between the key and the value, like so: `"name":"Paul"`
* Multiple pairs are separated by commas
* JSON uses a branch structure to show *properties within properties*, with curly brackets **nested** within other brackets like so: `{"place":{"name":"Birmingham","latitude":52.4862}}`
* Data within JSON is fetched by describing a path through each object's key, like so: `jsonobject['place']['name']`
* JSON can also be supplied in **arrays**, with a series of JSON objects each separated by a comma and contained within a single pair of square brackets like so: `[{"force":"West Midlands"},{"force":"Mercia"}]`
* Data within an array can be accessed by using an index after the array name, and then the path through the JSON at that position, like so: `arrayobject[0]['force']`
* Data within an array can also be **looped through** by using `for ... of`
