# Using VLOOKUP with coronavirus data

The Government publishes [Weekly statistics for NHS Test and Trace (England) and coronavirus testing (UK)](https://www.gov.uk/government/collections/nhs-test-and-trace-statistics-england-weekly-reports). 

Click through to the latest report, and then scroll down to the **NHS Test and Trace regional breakdowns: data tables**.

You will [find an example of that data here](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/2functions/vlookupdata/Regional_contact_tracing_week16.csv) (click on **Raw** and then save to your computer).

This has data for every local authority on track and trace - but it's missing context about variation in the populations of those areas.

## Getting the population data

Search around for 'local authority populations'. Eventually you may end up on [the ONS page for population estimates](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland) which has a local authority breakdown.

Download the data - you can also [find it here](https://github.com/paulbradshaw/MED7373-Data-Journalism/blob/master/2functions/vlookupdata/ukmidyearestimates20192020ladcodes.xls) (click on the 'Download' link to save it.)

## Matching them up

Follow the steps in the chapter on VLOOKUP in *Finding Stories in Spreadsheets*, or in the spreadsheet formulae crib sheet on Moodle. You will need to:

* Move the population sheet into the spreadsheet with the track and trace data
* Write a VLOOKUP formula in the track and trace sheet to fetch populations from the populations sheet
* Check the #N/A errors where the naming is slightly different
* Fix those
* Now you can divide the other figures by the population to get a per-person figure. You might also try a per-thousand or per-10,000 figure by multiplying the per-person figure accordingly 
