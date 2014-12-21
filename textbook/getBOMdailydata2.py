import urllib
from bs4 import BeautifulSoup

year = '2014'
month = '07'
day = [str(x) for x in range(20)]

# get website content
bs = BeautifulSoup(urllib.urlopen('http://www.boxofficemojo.com/daily/chart/?view=1day&sortdate=' + year + '-' + month + '-' + '20' + '&p=.htm').read())

# html = []
# for line in conn:
#     html.append(line)
# 
# for i in html:
#      if i[:183] == '<tr><td colspan="3" align="center"><table border="0" cellpadding="5" cellspacing="1"><tr bgcolor="#dcdcdc"><td align="center"><font size="1"><a href="/daily/chart/?view=1day&sortdate=':
#          boxOfficeTable = str(i)

# bs = BeautifulSoup(boxOfficeTable)


table = bs('table')[8].prettify()

for row in bs('table')[8].findAll('tr'):
    tds = row('td')
#     print tds

tableDict = dict() 

for x in range (1, 25):
    key = bs('table')[8].findAll('tr')[x].findAll('td')[2].a.string
    tableDict[key] = []
    for i in range(1, 9):
        # print bs('table')[8].findAll('tr')[0].findAll('td')[i].a.string
        tableDict[key].append(bs('table')[8].findAll('tr')[0].findAll('td')[i].a.string)

print tableDict