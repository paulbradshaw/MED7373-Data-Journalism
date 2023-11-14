# Using generative AI (ChatGPT/Bard) to write JavaScript

Generative AI tools such as ChatGPT and Google Bard are especially useful in helping both draft code, and troubleshoot your own code. 

The more coding knowledge you have, the better you can use them. Equally, the more you use them, the more opportunities you will have to find out more about how code works. 

Try this prompt to create some JavaScript for a counter (a part of the page which counts up. This is typically used to show how much something is changing in real time, such as a well-paid celebrity's wages, or deaths caused by global warming):

> Write some code which creates a counter inside the tag `<span id="mycounter">` which starts at 0 but goes up by 3.4 every 0.4 seconds.

Responses will vary but on the whole ChatGPT/Bard will provide the code for a whole webpage, including the HTML and including the `<head>` tags.

If you're using Codepen, however, it's important to remember that a) it splits HTML, CSS and JavaScript into three separate windows/files; and b) you do *not* have to write the `<head>` and `<body>` tags - it does that for you.

Once you get the initial response, then, you can prompt: 

> Split that code so that it can be used in Codepen.io

It should now provide a revised response with separate blocks for HTML, CSS (empty) and JavaScript.

However, even this response needs a little tweaking: the HTML block will still include `<head>` and `<body>` tags, so you will need to ignore those and only copy the HTML inside the `<body>` tag (not including the `<body>` tags themselves).

You will also need to build on/tweak the HTML for more specific purposes: it's likely you will want your counter to sit in the middle of a sentence, for example, so you will probably need to add a paragraph around it (including the `<p>` tags), e.g.

```
<p>Since you started reading this <span id="mycounter"></span> puppies have exploded.</p>
```

You might also want to add a new prompt asking it to round the number so that it's not displaying to multiple decimal places.

**IMPORTANT: Use of generative AI should be clearly attributed - failure to attribute the use of generative AI is considered a Category A plagiarism. If you are using generative AI in your work, make sure you document the process (e.g. screenshots; copies of prompts and responses) and what you did with the results (e.g. edited, adapted, iterated).** 

**There should be some critical reflection on good practice and limitations: after all, you are exploring emerging practices in the industry, so there's an opportunity here to contribute to knowledge.**

## Tips on using generative AI in your coding

Some other tips to consider when using this approach:

* Specify the library that you want to use
* Ask it to suggest libraries that could also be used
* Provide the data you want used (remember that ChatGPT has a 500 word limit to inputs, so it won't be able to accept very large data pasted in)
* Ask it to break up the code into sections for Codepen
* Iterate: ask it to add labels, change colours, etc.
* Ask it to problem-solve: paste code and ask it why it might not be working
* Keep notes on the prompts and the responses - see the note above on attribution

