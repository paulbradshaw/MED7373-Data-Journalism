# Workshop: applying styles to a story

This exercise demonstrates how CSS selectors work - and Codepen.

## Create an account on Codepen and create a new 'pen'

Create an account on [Codepen](https://codepen.io/) and create a new 'pen' (go to https://codepen.io/pen/ and then change the name in the upper left corner from 'untitled')

## Copy the text into Codepen

Here's the text you need to copy and paste into the **HTML** view on the left hand column in Copepen (it's from [this story](https://www.bbc.co.uk/news/uk-58085428)):

> 'NHS abandoned me after I tried to kill myself'
>
> A woman who tried to take her own life after suffering post-natal depression says she was abandoned by NHS mental health services during the pandemic.
>
> Katie Yelland, 30, relied on family support to get her through the first lockdown after services were paused.
>
> It comes as monthly mental health referrals across the UK hit their highest point in two years.
>
> Charities warned the surge was set to continue and called for action from the UK and devolved governments.
>
> The UK government says it plans to expand and transform mental health services, backed by £2.3bn a year by 2023-24.

## Add some HTML tags to separate it out

You will notice that in the preview underneath all the text is lumped into one paragraph. That's because we need to add **tags**.

Do the following:

* At the start of the headline, add a `<h1>` tag to indicate that this line is a level 1 heading
* At the end of the headline, add a `</h1>` tag to indicate the end of that heading
* At the start of each line after that, add a `<p>` tag to indicate the start of a paragraph
* At the end of each line, add a `</p>` tag to indicate the end of a paragraph

See the formatting of the preview underneath change as you add those tags.

## Add some styles

Now we have HTML tags, we can 'select' them to apply styles.

Shift your attention to the middle **CSS** column in Codepen.

Let's say we want the text to be a slightly more subtle shade of grey, rather than black. 

How do we use CSS to change text colour? [Google it](https://www.w3schools.com/css/css_text.asp). 

It looks like the property is `color`

In the CSS view then we can add the following code:

```
p { color : grey }
```

You should see the preview update. 

Now think of other changes you might want to make. For example:

* Can you style the headline?
* Can you specify a slightly darker shade of grey? How?
* Can you apply multiple styles? How?

## Export the results

Click on the **Export** button in the bottom right corner to save your webpage - choose to save it **as a zip file**. 

Unzip that file and look at the resulting files - go into the 'src' folder and you should see an index.html file and a style.css file.

Open those in Atom or a similar text editor and see if you can 'read' the resulting code.


