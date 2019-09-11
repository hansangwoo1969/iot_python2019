from bs4 import BeautifulSoup
import requests
import urllib.request

html = urllib.request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
# html = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

tags = soup.findAll('div', attrs={'class':'tit3'})  # findALL:조회된 모든 자료가 한꺼번에 리스트로 반환
up_downs = soup.findAll('img', attrs={'class':'arrow'})
ranks = soup.findAll('img', attrs={'width':'14'})
ranges = soup.findAll('td', attrs={'class':'range ac'})

f = open('movie_rank_test.csv', 'w', encoding='utf-8')  # 저장할 파일 열고,
f.write('rank, name, range\n')                          # 컬럼네임 지정하고,
i = 0                                                   # 인덳스 초기화,
while i < len(ranks)-1:
    print('{0}, {1}, {2}, {3}'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    f.write('{0}, {1}, {2}, {3}\n'.format(int(ranks[i]['alt']), tags[i].a['title'], ranges[i].string, up_downs[i]['alt']))
    i += 1
f.close()
