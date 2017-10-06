# Examples of computational thinking in journalism

This week you are being introduced to **computational thinking** techniques. Here are some of my favourite examples of computational thinking being used to spot and execute data journalism stories - see if you can find others and add them!

## Story 1: Which singer has the biggest vocal range?

[This story, published in the UK tabloid newspaper The Mirror](http://www.mirror.co.uk/news/uk-news/singer-best-vocal-range-uk-4323076), is a great example of understanding how a computer might 'see' information and be able to help you extract a story from it.

[The data behind the story](https://www.musicnotes.com/) is a collection of over 300,000 pieces of sheet music. On paper that music would be a collection of ink on paper. But because that has now been digitised, it is now **quantified**.

That means we can perform calculations and comparisons against it. We could:

* Count the number of notes
* Calculate the variety (number of different) of notes
* Identify the most common notes
* Identify the notes with the maximum value
* Identify the notes with the minimum value
* Calculate a 'range' by subtracting the minimum from the maximum

The journalist has seen this, and decided that the last option has perhaps the most potential to be newsworthy - we assume some singers have wider ranges than others, and the reality may *surprise* us (a quality of newsworthiness).

Of course getting to that story requires a great deal of technical skill - acquiring the data may necessitate using or writing a scraper; script may be required to identify the highest and lowest note in each song, then to associate that with an artist, and finally to aggregate the highest and lowest note *by artist*.

There's also some filtering here in looking specifically at UK artists - that may require more data which then needs to be combined with the sheet music data. All of this requires further computational thinking.

But the fundamental idea isn't about technical skill - it's an editorial and logical one.

## Story 2: Gendered dialogue in film scripts

The second example - [She Giggles, He Gallops](https://pudding.cool/2017/08/screen-direction/) - is an example of **pattern recognition**: the writer realises that she can investigate gender representation in films by looking for the verbs that come after the words 'he' and 'she'.

Text, like music, is merely ink on paper in an analogue world - but online it is quantifiable: it only needs a piece of code to say 'go through each film script, look for the word "he" or "she", and when you find it, capture the word immediately after it' (an **algorithm**).

From there it's about filtering (removing non verbs), counting/aggregating, and sorting (which words appear most often against each gender).

## Story 3: BuzzFeed - The Tennis Racket

![](https://img.buzzfeed.com/buzzfeed-static/static/2016-01/15/10/enhanced/webdr03/anigif_original-12912-1452872347-4.gif?downsize=715:*&output-format=auto&output-quality=auto)

[BuzzFeed's investigation into potential match fixing in tennis](https://www.buzzfeed.com/johntemplon/how-we-used-data-to-investigate-match-fixing-in-tennis?utm_term=.xyqaBVVBXJ#.jxYYaMMaXp) was a major undertaking, and involved some particularly advanced coding skills - but working out how to investigate such a subject was just as important as the technical execution.

The story was a good example of **decomposition**: breaking a problem down into a series of smaller ones. These included:

* How is match fixing quantified?
* Where would that be recorded?
* How do we get hold of that data?
* How do we establish some level of proof?

This is all about looking for **signals** of something in the physical world, in the digital world. Here's some of the **abstraction** that took place next:

* Why does match fixing take place? So the fixers can make money through **gambling**
* How do they make money? By placing **large bets** and/or at **longer odds**
* Longer odds mean that results must be **unexpected**
* What happens when those bets are made? The **odds change notably** so bookmakers can reduce their risks

This requires some knowledge of and/or exploration of the systems of match fixing and bookmakers, by the way.

Now the initial plan might be to get hold of records of the bets made on matches - but bookmakers are unlikely to cooperate with such an approach. So assuming that an approach has been made - and declined - we move onto a secondary signal: significant swings in odds in the lead up to a match.

By pairing those with unexpected results, the journalists can identify areas for further investigation: do particular players keep recurring in those results?

[A more detailed methodology is available on their GitHub repo](https://github.com/BuzzFeedNews/2016-01-tennis-betting-analysis), including data and notebooks.

## Story 4: Trump's Android versus his assistants' iPhone

[David Robinson's work on Donald Trump's tweets](http://varianceexplained.org/r/trump-tweets/) - which he was [asked to write up for the Washington Post](https://www.washingtonpost.com/posteverything/wp/2016/08/12/two-people-write-trumps-tweets-he-writes-the-angrier-ones/?utm_term=.104d90779aae) is another story of *pattern recognition* - in this case, different tones of voice coming from Donald Trump's tweets, and meta data associated with those (whether updates came from Twitter for iPhone or Twitter for Android).

There's also a level of *abstraction* here in identifying core words which represent a particular tone of voice.

## Add your own

You can fork this GitHub repo and edit this page to add your own - then submit a pull request to add it to my original version...
