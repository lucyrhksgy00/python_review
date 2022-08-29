import requests
from bs4 import BeautifulSoup

url = 'http://www.naver.com'
response = requests.get(url)
print("웹서버의 응답시간 :", response.elapsed)
print("웹서버의 상태 :", response.status_code)
# print(response.text)

url = 'https://search.naver.com/search.naver'
param = {'query': 'movie'}
response = requests.get(url, params=param)
# print(response.text)

url = 'http://www.samsungfire.com'
response = requests.get(url)
response.encoding = None
# print(response.text)

# naver 영화 사이트
url = 'https://movie.naver.com/movie/bi/mi/basic.naver'
param = {'code':'194196'}
response = requests.get(url, params=param)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

from Color import *

# find_all을 이용하여 한줄평 가져오기
stmt = soup.find_all('div', class_='score_reple')
for idx, div in enumerate(stmt):
    if idx == 0:
        print(RED + str(idx+1) + ' : ' + div.find('p').text.strip() + END)   # strip()에 아무 문자열도 넣지 않으면 공백으로 인식함
    elif idx == 1:
        print(GREEN + str(idx+1) + ' : ' + div.find('p').text.strip() + END)
    else:
        print(str(idx+1) + ' : ' + div.find('p').text.strip())

print()
# select를 이용하여 한 줄 평 가져오기 (*** CSS Selector 문법 공부하기 ***)
stmt = soup.select('div.score_reple > p')
for div in stmt:
    print(div.text.strip())

print()
# 명대사 가져오기
stmt = soup.select('div.tx_top > strong')
for div in stmt:
    print(div.text.strip())

print()
# API 방식으로 데이터 가져오기
for i in range(1,11):
    url = 'https://m.stock.naver.com/api/index/KOSDAQ/price?pageSize=50&page={}'.format(i)
    response = requests.get(url)
    jdata = response.json()
    for dat in jdata:
        print(dat['localTradedAt'], dat['closePrice'])