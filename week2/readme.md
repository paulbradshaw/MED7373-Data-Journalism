# Computational thinking: the postcode challenge

This task is an example of using computational thinking techniques such as pattern recognition, abstraction and decomposition (breaking down a problem). It's also a common problem that data journalists face: splitting up a postcode.

## Why do we need to split a postcode?

Let's say we have a dataset with multiple rows. Each row contains details for some sort of incident (a crime, a fire, an accident), including the address and postcode.

One story we might want to tell is which part of the city has the most incidents - but doing that based on full addresses or postcodes won't be too meaningful, because the areas - and numbers - are too small. Instead we want to paint a bigger picture based on larger areas. 

How do we do that? By aggregating our incidents based on just part of the postcode - the first part, which represents the postcode *district*.

This example isn't limited to postcodes - the same process might be used with phone numbers (which is the area code that most calls come from in a dataset), or dates (which is the day of the week with the most incidents, rather than the specific date), or licence plates (what part of the country, or the age of the vehicle).

## Decomposition of the data

Looking at the data this way is an example of **decomposition**: instead of seeing each postcode (or phone number, or date) as a single element, we can recognise that it is actually formed of different elements. For example:

* A postcode consists of two parts: the postcode district (e.g. B42) and a second part which provides more detail.
* A telephone number consists of two parts: the area code (or other code) and the core phone number
* A date consists of three parts: a day, month and year
* A licence plate consists of a place that registration was issued, and a year of registration

In fact, some extra research will tell you that [postcodes can be broken down into more parts](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting), [phone numbers can be broken down further](https://en.wikipedia.org/wiki/Telephone_numbering_plan), and [licence plates have more detail too](https://www.nationalnumbers.co.uk/number-plate-formats-explained.htm)

## Decomposition of the problem

But that's not the main thing we need to decompose. We need to break down the *problem* too. How do we extract the first part of the postcode - the postcode district?

The answer will depend on how the data is formatted, and how **clean** it is - in terms of its consistency.

For example, postcodes often include a space in the middle, between the two parts. If our postcodes are formatted in this way, and *all* the postcodes are formatted the same way, then we only need to split all our postcodes on the space.

If this is not the case, however, then we have a bigger challenge.

If the postcodes were all the same length, and had *no* spaces, we could split on a particular position of character. But we can rule that out straight away: some reading around postcodes will tell you that they can vary between 5 and 7 characters in length.

But [that reading](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Modern_postcode_system) should also tell you something else useful about the *pattern* of postcodes.

What is it?

## Pattern recognition

...

The second part of a postcode is always 3 characters. It is the first part - the postcode district - which can range from 2 to 4 characters.

Now that we have that information, we can start a process of **abstraction** to come up with a way to tackle it.

## Abstraction

