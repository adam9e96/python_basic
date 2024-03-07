import csv
import pprint

import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : find_all() 메소드 이용하기

# 다음뉴스에서 제목, 링크, 뉴스 본문 추출하기.

# 다음 뉴스에서 제목, 링크, 뉴스 보눈 추출해서 파일로 저장하기
# 1) 이전 예제를 활용할것
# 2) 링크를 추출한 for 안에서 제목을 추출
# 3) 뉴스 본문은 링크를 이용
# 4) 링크를 타고 뉴스 본문을 들고 와야 되니
# for 문 안에서 requests, BeautifulSoup가 실행이 되어야 함
# 5) 제목, 링크, 뉴스 순으로 csv 저장

# 기사 모으기
# 다음 뉴스
url = 'https://news.daum.net/'
resp = requests.get(url)
soup = bs(resp.text, 'html.parser')
# pprint.pprint(soup)

dict_list: list[dict] = []
tags = soup.find_all('div', {'class': 'item_issue'})
print(len(tags))  # 20
for tag in tags:
    # print(tag.find_all('a')[1])
    # print("-" * 20)
    temp_dict = dict()
    title: str = tag.find_all('a')[1].text.strip()
    link: str = tag.find_all('a')[1].get('href')
    temp_dict['title'] = title
    temp_dict['link'] = link
    # print(f'title: {title}, link: {link}')
    # print('-' * 20)
    dict_list.append(temp_dict)
# print(dict_list)
from share import save_csv

save_csv('abcdef.csv', dict_list)

# 내가 한거
# sections = soup.find_all('ul', {'class': 'list_newsissue'})
# # pprint.pprint(sections)
# # intersection = sections.find_all('div', {'class': 'item_issue'})
# for news in sections:
#     # print(news)
#     intersection = news.find_all('div', {'class': 'item_issue'})
#     # pprint.pprint(news.find_all('div', {'class': 'item_issue'}))
# for i in intersection:
#     # print(i.find('strong', {'class': 'tit_g'}))
#     # print(i.find('a').get('href'))
#     # title_tag = i.find('strong', {'class': 'tit_g'})
#
#     title = i.find('strong', {'class': 'tit_g'}).text.strip()  # .text로 텍스트 추출 후 .strip()으로 양쪽 공백 제거
#     link = i.find('a').get('href')

# print(title)
# print(link)
# print(title)
# print(link)

# file_name: str = 'news_title_test.txt'
# with open(f'../output/{file_name}', 'w', encoding='utf-8') as file:
#
#         for news in len(intersection):
#             pass
#         # csv_writer = csv.DictWriter(file)
#         # print(news.find_all('a')[1].text.strip())
#         file.write(f'{news.find_all("a")[1].text.strip()}\n')
#         # print('*' * 20)
# print()
