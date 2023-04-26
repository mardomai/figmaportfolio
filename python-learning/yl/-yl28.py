import urllib3
import sys
from bs4 import BeautifulSoup
from tqdm import tqdm

sys.stdout = open('Tahvel' + '_urllib3.txt', 'w')
url = "https://tahvel.edu.ee/#/timetable/38/group/5900/584/23"
r = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(r, "html.parser")
article = soup.find('div', attrs={'class': 'article'})

print( article.contents[0] + ': ')

lister_list_contents = soup.find('div', attrs={'class': 'lister-list'})
i = 1
movieList = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

for div in tqdm(movieList):

    print( str(i) + '.',)

    header = div.findChildren('h3', attrs={'class': 'lister-item-header'})

    for items in header:

        title = header[0].findChildren('a')

        print( 'Movie: ' + str(title[0].contents[0]))

    genre = div.findChildren('span', attrs={'class': 'genre'})
    genre_text = genre[0].text.encode('utf-8').decode('ascii', 'ignore')

    print( 'Genre: ' + genre_text.strip('\n'))

    p_all = div.findAll('p', attrs={'class': 'text-muted'})
    desc = p_all[1].text.encode('utf-8').decode('ascii', 'ignore')

    print( 'Description: ' + desc.strip('\n'))

    i += 1