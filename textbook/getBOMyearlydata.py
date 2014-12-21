import urllib
import csv
from bs4 import BeautifulSoup

dataTable = []
start = 1995 # starting year of the range - inclusive
end = 2014 # ending year of the range - inclusive (b/c of +1 in range below)

for year in range(start, end + 1):

    # get website content
    bs = BeautifulSoup(urllib.urlopen('http://www.boxofficemojo.com/yearly/chart/?yr=' + str(year) + '&p=.htm').read())

    for row in bs('table')[6].findAll('tr'):
        tds = row('td')
        movie_data = []
    
        if tds[0].font is not None:
            if tds[0].font.string in str(range (1, 101)):
        
                movie_data.append(year)
                movie_data.append(tds[1].a.string)
                movie_data.append(tds[0].font.string)
                movie_data.append(tds[2].a.string)
                movie_data.append(tds[3].b.string)
                movie_data.append(tds[4].font.string)
                movie_data.append(tds[5].font.string)
                movie_data.append(tds[6].font.string)
                movie_data.append(tds[7].a.string)
                try:
                    movie_data.append(tds[8].font.string)
                except IndexError:
                    movie_data.append('null')
            
                dataTable.append(movie_data)



# ifile  = open('/Users/jimshields/Python/test.csv', "rb")
# reader = csv.reader(ifile)

ofile  = open('/Users/jimshields/Python/test.csv', "wb")
writer = csv.writer(ofile) # delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL

for row in dataTable:
    writer.writerow(row)

# ifile.close()
ofile.close()