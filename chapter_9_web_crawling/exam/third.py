# 3. cgv 홈페이지(cgv.co.kr)의 무비차트에서 순위별로 영화 제목과 개봉일, 예매율을 requests를
#   이용해서 데이터와 영화 포스터 이미지를 수집하시오.
#
#    영화 제목과 개봉일, 예매율을 데이터 베이스에 저장할 수 있는 테이블 생성 쿼리를 생성하고,
#
#    반복문을 이용하여 영화 제목과 개봉일, 예매율을 저장하는 insert 쿼리를 출력하는 코드를 작성하시오.
import csv

# 사이트 https://www.cgv.co.kr/
import requests
from bs4 import BeautifulSoup as bs

url: str = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
response = requests.get(url)
# print(response.text)
# print(response.status_code) # 200
soup = bs(response.text, 'html.parser')

# print(soup.select('div.sect-movie-chart '))
# movie = soup.select('div.sect-movie-chart > ol > li')
movie = soup.select('.wrap-movie-chart div.sect-movie-chart ol li')
# print(len(movie))   # 19

movie_data: list[dict] = list()
for idx, item in enumerate(movie, 1):
    # print(item.select_one('.title').text.strip()) # 영화 제목
    # print(f'영화제목 : {item.select_one(".title").text.strip()}')
    # print(f'개봉일 : {item.select_one(".txt-info > strong").text.strip().split(" ")[0]}')
    # print(f'예매율 : {item.select_one("div.box-contents > div > strong > span").text.strip()}')  # 예매율
    # print(f'이미지 : {item.select_one("img").get("src")}')
    temp_dict = dict()
    temp_dict['영화 제목'] = item.select_one(".title").text.strip()
    temp_dict['개봉일'] = item.select_one(".txt-info > strong").text.strip().split(" ")[0]
    temp_dict['예매율'] = item.select_one("div.box-contents > div > strong > span").text.strip()
    movie_data.append(temp_dict)
    response = requests.get(item.select_one("img").get("src"))
    with open(f"./img/{idx}_{temp_dict['영화 제목']}_{temp_dict['개봉일']}_{temp_dict['예매율']}.jpg", 'wb') as image_file:
        image_file.write(response.content)
# print(movie_data)

file_name: str = 'cgv_chart.csv'
with open(f'./{file_name}', 'wt', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=movie_data[0].keys())
    writer.writeheader()
    for data in movie_data:
        writer.writerow(data)
        print(f'INSERT INTO movies(title, release_date, reservation_rate) VALUES [{data["영화 제목"]}],[{data["개봉일"]},[{data["예매율"]}]] ')
print(f'{file_name} 저장 완료')

# 테이블 생성
# CREATE TABLE movies (
#     id INT AUTO_INCREMENT PRIMARY KEY,    # 고유식별id
#     title VARCHAR(50) NOT NULL,
#     release_date VARCHAR(50) NOT NULL,
#     reservation_rate VARCHAR(10) NOT NULLs
# );

# 반복문을 이용하여 영화 제목과 개봉일, 예매율을 저장하는 insert 쿼리를 출력하는 코드
# for item in movie_data:
# print(item['영화 제목'])
# print(item['개봉일'])
# print(item['예매율'])
# INSERT INTO movies(title, release_date, reservation_rate) VALUES (item['영화 제목'], item['개봉일'], item['예매율']);
