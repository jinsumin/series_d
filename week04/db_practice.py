from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.get_database('test')

# db.person.insert_one(
#     {'name': 'kim', 'age': 30}
# )


import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
response = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',
    headers=headers
)

# print(response.text)

# HTML 데이터 가공
soup = BeautifulSoup(
    response.text, 'html.parser')


selector = '#old_content > table > tbody > tr'
title_selector = 'td.title > div > a'
titles = soup.select(selector)

for title in titles:
    title_tag = title.select_one(title_selector)

    if title_tag:
        rank = title.select_one('td:nth-child(1) > img')
        point = title.select_one('td.point')
        print(rank['alt'], title_tag.text, point.text)

        document = {
            'rank': int(rank['alt']),
            'title': title_tag.text,
            'point': float(point.text),
        }

        db.movies.insert_one(document)
        print('DB 적재 완료', document)