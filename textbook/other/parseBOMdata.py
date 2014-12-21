from pyparsing import makeHTMLTags,withAttribute,Suppress,Regex,Group
import urllib

year = '2014'

conn = urllib.urlopen('http://www.boxofficemojo.com/yearly/chart/?yr=' + year + '&p=.htm')

""" looking for this recurring pattern:
          <td valign="top" tdalign="center">00-03</td>
          <td valign="top">.50</td>
          <td valign="top">.50</td>

    and want a dict with keys 0, 1, 2, and 3 all with values (.50,.50)
"""

td,tdend = makeHTMLTags("td")
keytd = td.copy().setParseAction(withAttribute(tdalign="center"))
td,tdend,keytd = map(Suppress,(td,tdend,keytd))

# realnum = Regex(r'1?\.\d+').setParseAction(lambda t:float(t[0]))
# integer = Regex(r'\d{1,3}').setParseAction(lambda t:int(t[0]))
DASH = Suppress('-')

# build up an expression matching the HTML bits above
entryExpr = (keytd + tdend + 
                    Group(2*(td + tdend))("vals"))
                    
# search the input HTML for matches to the entryExpr expression, and build up lookup dict
lookup = {}
for entry in entryExpr.searchString(conn):
    for i in range(entry.start, entry.end+1):
        lookup[i] = tuple(entry.vals)
        
print lookup                