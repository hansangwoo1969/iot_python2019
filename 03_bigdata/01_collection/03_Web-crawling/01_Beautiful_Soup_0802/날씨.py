import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=3&acq=%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8"
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
# print(soup)
# <span class="todaytemp">31</span>
temp = soup.find('span', {'class':'todaytemp'}).text
temp_mark = soup.find('span', {'class':'tempmark'}).text[-1]
weather = soup.find('p', {'class':'cast_txt'}).text
#<p class="cast_txt">구름많음, 어제보다 2˚ 높아요</p>
print(temp + temp_mark, weather)
