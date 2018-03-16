from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import time

html = urlopen("https://bechdeltest.com/?list=all")
bsObj = BeautifulSoup(html, "html.parser")

urlList = []

div = bsObj.findAll('div', {"class":"movie"})

for link in div:
    passFail = (link.img['src'])
    if passFail == "/static/pass.png":
        urlList.append(link.a.get('href'))
    else:
       continue

output = []

with open('movieratings.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for url in urlList:
        try:
            html = urlopen(url)
            bsObj = BeautifulSoup(html, "html.parser")
            title = bsObj.find({"h1"}).get_text()
            rating = bsObj.find('span', {"itemprop":"ratingValue"}).get_text()
        except Exception as e:
            time.sleep(10)
            continue
        writer.writerow((title,rating))
csvfile.close()
