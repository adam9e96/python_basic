import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : select() 메소드 이용하기

# select() 메소드
# CSS selector로 지정한 태그들을 모두 가져오는 메소드. 가져온 태그들은 모두 리스트에 보관

"""
find() : 하나만
find_all() : 여러개

select_one() : 하나만
select() : 여러개
"""
url: str = 'https://news.daum.net/digital#1'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
tag_series = soup.select('.list_todayseries li')
# print(tag_series)

# for tag in tag_series:
#     print()
#     tag_series_title = tag.select_one('.link_txt').text
#     print(f'제목: {tag_series_title}')
#
#     tag_series_press = tag.select_one('.txt_info').text
#     print(f'신문마: {tag_series_press}')
