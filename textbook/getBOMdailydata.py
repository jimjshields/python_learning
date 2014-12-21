import urllib
import csv
from bs4 import BeautifulSoup

dataTable = []
date = '2014-07-25'
start = 2014-01-01 # starting year of the range - inclusive
end = 2014-07-27 # ending year of the range - inclusive (b/c of +1 in range below)

# for date in range(start, end + 1):

# get website content
bs = BeautifulSoup(urllib.urlopen('http://www.boxofficemojo.com/daily/chart/?view=1day&sortdate=' + date + '&p=.htm').read())

for row in bs('table')[9].findAll('tr'):
    tds = row('td')
    movie_data = []
    
#     print tds

    if tds[0].font is not None:
        if tds[0].font.string in str(range (1, 101)): # or tds[0].font.string == '-'
    
            movie_data.append(date)
            movie_data.append(tds[1].b.string)
            movie_data.append(tds[0].font.string)
            movie_data.append(tds[2].a.string)
            movie_data.append(tds[3].b.string)
            movie_data.append(tds[4].font.string)
            movie_data.append(tds[5].font.string)
            movie_data.append(tds[6].font.string)
            movie_data.append(tds[7].font.string)
            movie_data.append(tds[8].font.string)
            movie_data.append('null')
        
            dataTable.append(movie_data)
    
    print movie_data


# ifile  = open('/Users/jimshields/Python/test.csv', "rb")
# reader = csv.reader(ifile)

ofile  = open('/Users/jimshields/Python/dailytest.csv', "wb")
writer = csv.writer(ofile) # delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL

for row in dataTable:
    writer.writerow(row)

# ifile.close()
ofile.close()


# <td align="right"><font size="2">1</font></td><td align="right"><font size="2">1</font></td>
# <td><font size="2"><a href="/movies/?page=daily&id=dawnoftheapes.htm"><b>Dawn of the Planet of the Apes</b></a></font></td>
# <td><font size="2"><a href="/studio/chart/??view2=calendar&yr=2014&studio=fox.htm">Fox</a></font></td>
# <td align="right"><font size="2"><b>$11,059,498<b></font></td>
# <td align="right"><font size="2"><nobr><font color="#ff0000">-25%</font></nobr></font></td>
# <td align="right"><font size="2"><nobr><font color="#ff0000">-43%</font>/nobr></font></td>
# <td align="right"><font size="2">3,969</font></td>
# <td align="right"><font size="2">$2,786</font></td>
# <td align="right"><font size="2">$139,207,154</font></td>
# <td align="right"><font size="2">10</font></td></tr>