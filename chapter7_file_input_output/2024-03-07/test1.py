import pprint

import requests
from bs4 import BeautifulSoup as bs

# 네이버 뉴스 : IT/과학에서 오른쪾 섹션의 언론사별 가장 많이 본 뉴스 제목
# 들고오기
url: str = 'https://news.naver.com/section/105/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

section_list = soup.find_all('ul', {'class': 'ranking_list'})
# print(section_list)
for section in section_list:
    # print(section.find('p', {'class': 'rl_txt'}))
    # pprint.pprint(section.find_all('p', {'class': 'rl_txt'}))
    news_list = section.find_all('p', {'class': 'rl_txt'})
    for i in news_list:
        print(i.text.strip())
    print()
# news_list = section_list.find_all('p', {'class': 'rl_txt'})
# print(news_list)
# pprint.pprint(news_list)

# for news in news_list:
#     print(news.text)
