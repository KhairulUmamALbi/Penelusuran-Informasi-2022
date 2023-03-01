import requests
from bs4 import BeautifulSoup

tanggal = 1
session = requests.session()
while tanggal <=30 : 
    html = 'http://indeks.kompas.com/news/?site=all&date=2022-01-' + str(tanggal)
    req = session.get(html)
    bs = BeautifulSoup(req.text, 'html.parser')

    link = bs.find_all('a', attrs = {'class':'article__link'})

    for links in link:
        f = open("list.txt", "a")
        f.write(links['href'] + "\n")

    tanggal += 1

f.close()