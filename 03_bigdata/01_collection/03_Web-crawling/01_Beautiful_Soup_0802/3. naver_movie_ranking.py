import urllib.request
# import requests
import csv
from bs4 import BeautifulSoup
html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
# html = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

body = soup.find('tbody')
trs = body.find_all('tr')

data = []

for tr in trs:
    if tr.find('img'):
        r = tr.find('img')
        rank = r['alt']
        tite = tr.find('a')
        title = tite.text
        u_d = tr.find('td', attrs={'class':'range ac'})
        up_down = u_d.text

        if tr.findAll('img')[1]:
            gr = tr.findAll('img')[1]
            grade = gr['alt']

            data.append([rank, title, grade, up_down])

with open('movie_ranking.csv', 'w', encoding='utf8', newline="") as f:
    csvwriter = csv.writer(f)
    for row in data:
        csvwriter.writerow(row)
print(data)



