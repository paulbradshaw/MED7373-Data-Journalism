# Why map?

When it comes to data visualisation, everyone loves a map. More exciting than a chart, easier than an infographic, it's generally the first thing that journalists and journalism students alike ask: "How can we create a map?"

But **just because you have some geographical data doesn't mean you should map it**. 

Here's why: maps, like all methods of visualisation, are designed for a purpose. They tell *particular types of stories* well - but not all of them.

There is also **more than one type of map**. You can map points, shapes, or routes. You can create heat maps and chloropleth maps.

I'll tackle those different types of maps first - and then the sorts of stories you might tell with each. But the key rule running throughout is this: **make sure you are clear what story you are trying to tell, or the story that users will try to find**. The test is whether a map does that job best.

## Mapping with points

If you are mapping points it means that each row in your dataset is given a location on your map. For example, if you were mapping businesses' food hygiene inspections then a pointer would be placed at the location of each business.

This approach is one of the simplest ways to get started with mapping. But for the same reason it can be used badly.

Mapping points makes sense if:

* Your data refers to **specific locations**, such as businesses or crime scenes
* Users will want to look at **data points near them**, such as how local schools perform, or whether someone was arrested for that crime
* The resulting map **shows a clear distribution** of those points, and this is the story you are trying to tell: for example fast food vans near the sports stadium are failing food hygiene inspections; or there are more burglaries in one area than another.

Mapping points *is not the right approach* if:

* Your data refers to **larger areas**, such as countries or regions. Even cities or parts of cities can make little sense when plotted as points on a map.
* Users **do not need a map to find a location relevant to them, or cannot**. For example in a national map, many users may not be able to locate their town; after all, how many times do we use national maps to orientate ourselves? In reality we tend to use local maps or specific road maps. 
* The story is **not about the visible distribution or clustering** of those points, but about comparison (for example the worst or best places) or composition. 

In this last case you are better using a visualisation device designed for that purpose, such as a bar chart (comparison) or pie chart (composition). 

If your story *is* about distribution but not a geographical one, then try a scatter chart.

### Geo data: the more detail the better

One thing to note about mapping points is the potential for mapping tools to **place marks wrongly**.

This is because mapping tools work by **geocoding your locations**. That effectively means that they *convert* text in your address fields (such as 'London' or '34 High Street') into geographical data: typically latitude and longitude.

The best case scenario is if you *have* latitude and longitude in your data. This means that the tool does not have to perform any conversion, and the process is much quicker and more accurate (assuming your lat/long values are accurate).

But if your geographical information is partial or inexact, and outside the US, you may have problems.

Most mapping tools default to the US, so 'Cambridge' will be placed in Massachusetts unless you are able to specify otherwise. It may be able to map zip codes, but not postcodes.

There are two ways to reduce the chances of misplacement: the first is to **use any options in your mapping tool to limit the geocoding**. 

The mapping tool [BatchGeo](http://batchgeo.com), for example, allows you to specify a particular country rather than the default 'worldwide'. And Google Fusion Tables allows you to specify 'hints' on locations.

The second way to reduce misplacement is by **combining the address details into one column**, rather than (or as well as) having things like 'street name' and 'city' and 'country' in separate fields.

This is particularly the case with Google Fusion Tables, which maps based on one column (BatchGeo does allow you to specify which column contains the city, which contains a zip or post code, and so on). 


### Customising markers: avoid the rainbow effect

If you are mapping points it is likely that you're going to want to **classify those points** in some way - for example, in order to distinguish between those locations with high values (high crime, high ratings, high performance) and those with low ones.

You should also think about the information which is provided when a user clicks on a particular point - often called the 'information window'.

There are three main ways of indicating the classification of points: **colour, shape and size**.

Colour is the most commonly used approach, and certain colours are used particularly often: for example green to indicate 'good' values (high ratings; low crime) and red to indicate 'bad' ones (high incidence of disease; poor performance), as well as perhaps orange ('amber') to indicate values which are neither high nor low, or grey to indicate points where no data exists.

When choosing colour try to avoid the 'rainbow effect'. This is the temptation to use a different colour for each classification in a system.

For example the food hygiene rating system in the UK goes from 0 to 5: that's six different bands. 

If you were mapping these ratings by location you may be tempted to use six colours: one for each band. But ask yourself what the story is, or what the user might want to know.

Ultimately the user wants to know 'Is my local takeaway good or bad?' and the story might be 'Which areas have the most restaurants failing food inspections?'

Both are binary: good/bad, pass/fail. So your colour scheme should reflect that. Ratings from 0 to 2 are fails (bad); ratings 3 and above are passes (good). So you only need two colours for those two bands.

The resulting map is much clearer than if we used more colours: patterns (if they exist) are more easily discernible; users can at a glance see if a business is good or bad, without having to check against a legend, and then whether a value is a pass or a fail.

The inverted pyramid is a useful analogy here: we begin a story with the 'broad brush' of whether a restaurant has failed an inspection or not; extra details on the specific rating and so on would go lower in the story.

In this case, that information goes in the information window, which the user can click on if they want to know more.

### Using shape: don't repeat yourself

As well as colour you can **use shape or size to indicate a value**, depending on the tool. BatchGeo, for example, gives the option of a limited range of shapes. Google Fusion Tables has a [whole library of them]().

Shapes can be appealing to play with - but often add nothing to your 'story' (the map). Often people use shapes for points on their map simply because they can, and not because they make the story clear.

Instead, too often the shapes actually get in the way of a story: much as using ten words where one will do is considered bad journalism.

So if you are using shapes ask yourself carefully: 

* Are your shapes repeating the same information as the colour? If so, take them out. 
* Are the shapes telling the story itself, or adding extra information? If they are not the main story, take them out.
* Are the shapes the easiest way for users to navigate the map? If not, take them out.

Shapes work best when they are instantly recognisable icons, when there are not too many different ones, and when they are the primary use of the map. For example, if you wanted people to find the nearest facilities to them, and they could use icons to identify different types.

But if they are primarily interested in some other numerical criteria (the colour coding) it may be easier for them to filter from a drop-down list second.

### Using size: play with opacity

The third way of customising markers is to change their **size** based on a value or category. 

Here again you need to ask yourself whether you are adding too much information and obscuring the story, or making it harder for the user to find what they want.

If you are changing the size of the marker it is normally to indicate an amount. For example, where more than one crime has occurred at the same location you might increase the size of the point at that location to indicate this.

The potential problem here is that particularly large markers (sites with high amounts) can obscure markers in the same area. For that reason it is a good idea to choose semi-transparent colours for your markers, so the user can see other markers underneath. 

Your mapping tool may not allow you to do this, so you may have to look at other tools or JavaScript mapping libraries, or reconsider.

If you are using the size to indicate something other than amount, think carefully: if you are showing a percentage (90% being bigger than 50%, for example) is that what people will understand intuitively and be able to compare most easily? Most likely not: colour coding may be clearer.

If you are indicating categories (different sizes for different categories), you have the same problem: size is associated with amount, not category (even if the category is numerical), so it is best to think of other ways to indicate this.

### Heatmaps

One type of marker I haven't mentioned yet is the heatmap. This is where markers show **intensity** rather than location. 

Heatmaps can be useful where you are merely showing distribution, but they can also be misleading.

This is because they do not generally control for population density or other factors. A heatmap of failing food hygiene inspections, for example, may simply show the areas with the most restaurants and cafes. A heatmap of road accidents may simply show roads with the most traffic. 

## Mapping shapes

A more ambitious alternative to mapping points is to map *shapes*: in other words, instead of each data point being placed on a specific point on a map, instead different **areas on that map are drawn** and coloured/labelled according to the relevant data.

Shapes can be anything: you can have a map with shapes for each country in the world or a particular continent; or you can have a map with shapes for each county in the UK, or each constituency (voting region), or local authority. Or police authority area. Or health authority.

This is particularly useful if your data does not relate to geographical points (a specific location with its own latitude and longitude) but rather to broader geographical areas, such as a town or city, region or country, or an administrative area.

And data often *will* only relate to areas: unemployment rates, inflation and health data will all relate to areas. You are not going to get data which shows you the location of every sick person, unemployed person, or expensive loaf of bread.

If you are to be accurate in representing these figures, shapes are the way to do it. 

But they are also harder to 'draw' than points on a map.

This is because shapes are actually data too: a description of the coordinates and paths needed to draw each shape.

As a result, drawing a map with shapes invariably involves **merging data**: your data about those places; and the data containing the descriptions of those shapes.

This second set of data is often called 'shape files'. The mapping tool OpenHeatMap, for example, has a number of shape files stored in its database, including shapes for countries, US states, UK constituencies and authorities, and administrative regions in New Zealand, Mexico, Ireland, and other places.

This means that you can upload your own data and mix it with those shapes to generate maps that combine the two: shapes coloured according to a specified field in your data.

More broadly, Google Fusion tables has made shape files accessible to a much wider userbase than ever before.

Fusion Tables uses a language called KML (Keyhole Markup Language) to describe shapes. This means if you need to find the shapes to combine with your data, to create a map, then it's much easier to do so: once you upload your own data to Google Fusion Tables you can go to **File > Find a table to merge with...** and search all other public tables that share some information (for example the name of the regions).

[Here, for example, Simon Rogers lists 16 useful Fusion Tables files](http://simonrogers.net/2013/01/28/borders-and-boundaries-16-google-fusion-border-files-for-you-to-use/) for mapping shapes.

A more direct way to identify public tables is to use [Google's table search tool](http://research.google.com/tables) and specify that you want **Fusion Tables** results only. Adding 'geometry' to your search terms also increases the chance that you find shape files rather than just numerical or text data.

If the shapes you want to draw don't already exist in a Fusion Tables map, you may be able to find it in another format and convert. The .SHP file format, however, is often used for shape files, and can be converted to KML at the site SHPSCAPE.

Another option is to use a JavaScript library for mapping which has the shapes you need. Or to use more advanced mapping tools like GIS.

The final option is to draw the shapes yourself. In [Google Maps Engine Lite](https://mapsengine.google.com/map/) once you have drawn your maps (shapes, points, or routes) you can export as KML - then import when creating a new Fusion Table.

There's also another option which doesn't involve shape files at all: you can find an image showing all the regions you need, then add a layer of interactivity to convert that into an image map, as described below.

### Colouring map shapes

When choosing to colour-code shapes in a map you need to consider the same issues as outlined above with regard to points: don't choose too many colours, and keep the story clear and/or useful.

It is a good idea to use a tool like Colorbrewer to help you choose the colour palette. This will suggest colour combinations which can be seen by users with colourblindness, and which also suit the type of data you are showing (ordinal, for example). Below you can see a good example (from [this article](https://www.washingtonpost.com/news/wonk/wp/2016/04/11/the-dirty-little-secret-that-data-journalists-arent-telling-you/)) of how different colour schemes - and colour *scales* - communicate different types of data more clearly. 

![](https://raw.githubusercontent.com/paulbradshaw/mapping/master/mapcolour.png)

In that piece Christopher Ingraham writes: "Mapmakers often respect big distinctions by using a bivariate color scale – say, one set of colors for positive values (like blue), and another set of colors for negative ones (like red)." Colorbrewer includes explanations of different colour scales.

Consider making shapes semi-transparent so the detail underneath can still be seen; and setting border as white rather than black.

### The information window

Most mapping tools also allow you to customise the window which appears when a user clicks on a point or shape. 

Often these default to a list of headings and values. The headings are taken from your original spreadsheet, and the values from the particular row (location) being shown.

For that reason it's a good idea to make sure headings are clear, and to choose only the data that needs to be in that box. 

But in the more advanced tools such as Fusion Tables it's also worth taking the time to customise information windows further so that they are not merely a list of values, but rather a more readable sentence. 

For example, instead of `Location: Amsterdam, population: 3,000,000, burglaries per 1000: 0.5` you would customise the code to read:

`In Amsterdam there are 0.5 burglaries for every thousand people. The city has a population of 3,000,000 people`

Of course that requires reading up on that.

## Mapping routes

Routes are mapped much less often than shapes or points, but it is worth mentioning them here too. 

Tools like [Meograph](http://www.meograph.com/), Dipity and [Tripline](http://www.tripline.net/) allow you to tell stories with routes, while [Google Maps Engine Lite](https://mapsengine.google.com/map/) allows you to draw them and export in a format which can be used in Fusion Tables.

If your story is about a route it is worth considering these tools instead of simple points. You could also look at timeline tools like Timeline JS (and Dipity again) as routes can often be shown in this format too.

A route has its own built-in narrative which can be quite powerful. They lend themselves to photoblogging (taking images along the route) or audio or video (likewise). You could present data about each point along the route using those media (charts, for example) rather than making it about the map.

## Image maps

A final type of map is not, strictly speaking, geographical at all. This is the **image map**.

An image map is created when an image is 'mapped' by overlaying interactive elements on top of it. A good example might be an image of a group of people: this could be made into an image map by bringing up information about a particular person when your mouse hovers over her, or when you click on him. 

Indeed, on Facebook when you tag a person in an image this is exactly what happens. And Flickr allows you to add information to images in a similar way.

Image maps can be created with any image: it could be a picture of a complex system; a diagram; a street scene; a floor plan or schematic. In short, any image which includes elements you can tell different stories about.

**Image maps are one alternative way to create interactive maps without having to use shape files**: simply find a map of the regions you wish to visualise, and add a layer of interactivity on top.

The tool [Thinglink](http://thinglink) is one of the easiest ways to create an image map: you upload your image, then select an area you want to make interactive, then type the text, or image, video or audio URL, that you want to appear or play when someone clicks on that part of the image.

But you can achieve the same effect and take more control with JavaScript too.



### Tools

I've mentioned a lot of tools above. Which ones you use depends on what you want to achieve, but also how quickly and easily you want to do that.

BatchGeo is very quick and easy to get started with when it comes to mapping points. However, if you have more than a thousand or so rows then BatchGeo will ask you to pay to upgrade to the Pro version. At that point you might consider Google Fusion Tables as a more powerful, free, alternative.

CartoDB is another mapping tool which offers different functionality - for example the ability to size points based on a particular value. It also allows you to query your data and create different views using a language called SQL. Again there are limits to how much data you can store in the free account.

OpenHeatMap is a quick way to get started on mapping shapes - but make sure you read the documentation carefully and download the example spreadsheets for the shapes you want to use. You need to give your location column the same name as the documentation specifies, and make sure that location names match exactly (watch out for ampersands).

Tableau has some mapping options which are also worth exploring - particularly if you want to size placemarkers

Fusion Tables can do both points and shapes (and routes) and provides more customisation.

