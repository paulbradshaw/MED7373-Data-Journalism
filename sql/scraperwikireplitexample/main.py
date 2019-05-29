import scraperwiki
import lxml.html
import cssselect

#
# # Read in a page
urltoscrape = "https://en.wikipedia.org/wiki/List_of_twin_towns_and_sister_cities_in_England"
baseurl = "https://en.wikipedia.org"
html = scraperwiki.scrape(urltoscrape)
print(html)
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)

root = lxml.html.fromstring(html)
lis = root.cssselect('dl dd dl dd')
print(len(lis))
#create a dictionary to store what we find
record = {}
#loop through those lis
for li in lis:
  print(li.text_content())
  #This next line is the troubleshooted version
  #print(li.text_content().encode('utf-8').strip())
  record['address'] = li.text_content()
  #detaillink = baseurl+li.attrib['href']
  #record['link'] = detaillink
  scraperwiki.sqlite.save(['address'],record, table_name='twintowns')

print(scraperwiki.sql.select("count(*) from twintowns"))

print(scraperwiki.sql.select("* from twintowns where address LIKE '%Poland%'"))