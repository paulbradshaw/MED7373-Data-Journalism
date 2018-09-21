# Algorithmic accountability - @ndiakopoulos

"Algorithmic accountability is about how people exercise power through algorithms".

Importance for journalists:

* How to interrogate
* Characterise
* Make our own algorithms accountable

## Newsworthiness

The newsworthiness of #algorithms: bad decisions, violate expectations, public significance (severity and prevalence)
@ndiakopoulos

4 types:
* Discrimination/unfairness - e.g. ProPublica's [Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) series
* Errors/mistakes - e.g. no-flight list.
* Violation of expectation  - e.g. [How Facebook Outs Sex Workers](https://gizmodo.com/how-facebook-outs-sex-workers-1818861596)
* Human misuse - designers anticipate reasonable use, and set guidelines, but if people are ignoring/using differently then this can be a story of negligence or misuse

Errors/mistakes can be mapped against 2 axes:

* Vertical axis: attention/treatment by algorithm;
* Horizontal axis: negative or positive treatment

![](/algorithmsmatrix.png)

e.g. driving licence might come under more attention, that is negative - so upper left quadrant of graph
decrease in positive treatment - special offers only for selected people - lower right quadrant
less negative attention (classed as low risk when actually higher risk) - lower left quadrant

## Getting the story

* Reverse engineering: uncovering specifications for how algorithm works
* Auditing: correlate inputs to outputs; look for errors; compare to benchmarks
* Poking and prodding: exposing algorithmic reactivity can help illustrate
* Crowdsourcing: sock puppets, "data donation drives" ([Algorithm Watch](https://algorithmwatch.org/en/)) and plugins
* Code audits: get the code and read it; limited but important uses. Identifying what data is being used, for example, e.g. [WHAT HAPPENS WHEN AN ALGORITHM CUTS YOUR HEALTH CARE](https://www.theverge.com/2018/3/21/17144260/healthcare-medicaid-algorithm-arkansas-cerebral-palsy) where the algorithm hadn't been properly coded to account for things in the policy; it hadn't been translated properly.


## Complicating factors

* Information deficits - how can you open up data? One attempt to "lower the cost" of algorithmic reporting is at [algorithmtips.org](http://algorithmtips.org/)
* Sociotechnical assemblages - potential feedback loops, responsibility can be diffused
* Temporal instability - Google's algorithm changes 100s of times per year. Can you use a dashboard/interface to communicate the dynamic nature?
* Expectation setting - clearly define the norm that is being violated; they may vary by context
* Legal barriers - FOI (is software FOI-able?), access requests, privacy, Computer Fraud and Abuse Act (CFAA)



## Data Justice Lab:

Used a list of terms related to algorithms and scraped Google search results for those terms at `.gov.uk` and `.uk` domains.

Then scraped the linked documents and stored in database.

Extracted entities from the text to compile a list of key companies, products.

Scraped search results for terms on that list and 400 local authority domains, to create a further database.

* Existing story, e.g. profiling troubled families
* Fraud detection - London Counter Fraud Hub, DWP benefits fraud AI,
* Personal exploration - by company, place, dept, phrase

* What range & connections can we get from companies involved
* Methods used, data, is it shared
* Transparency, oversight and accountability
* Is potential for AI bias addressed
* History: data breaches, security
