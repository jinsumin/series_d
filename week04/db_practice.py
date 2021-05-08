from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.get_database('test')

# db.person.insert_one(
#     {'name': 'kim', 'age': 30}
# )


# import requests
# from bs4 import BeautifulSoup
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# response = requests.get(
#     'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',
#     headers=headers
# )
#
# # print(response.text)
#
# # HTML 데이터 가공
# soup = BeautifulSoup(
#     response.text, 'html.parser')
#
#
# selector = '#old_content > table > tbody > tr'
# title_selector = 'td.title > div > a'
# titles = soup.select(selector)
#
# for title in titles:
#     title_tag = title.select_one(title_selector)
#
#     if title_tag:
#         rank = title.select_one('td:nth-child(1) > img')
#         point = title.select_one('td.point')
#         print(rank['alt'], title_tag.text, point.text)
#
#         document = {
#             'rank': int(rank['alt']),
#             'title': title_tag.text,
#             'point': float(point.text),
#         }
#
#         db.movies.insert_one(document)
#         print('DB 적재 완료', document)

# CRUD

# 몽고DB에서 도큐먼트 읽어오기
movies_documents = db.movies.find(
    {},  # 검색조건
    {'_id': False},  # 데이터 표현방법 -> _id 값은 필요없으니 빼고 가져온다
)
movies = list(movies_documents)  # 바로 DB 접속해서 가져오도록 list() 사용

# 아래와 같이 하면 도큐먼트가 바로 나오지 않음
# <pymongo.cursor.Cursor object at 0x000001E66BDB8190>
# 지연된 평가
# 만약 movies_documents 선언하고 한참... 나중에 사용한다면?
# print(movies_documents)
