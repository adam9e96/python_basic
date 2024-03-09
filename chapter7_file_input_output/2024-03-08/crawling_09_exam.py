import pprint
import requests
from bs4 import BeautifulSoup as bs  # <--은 지금 안씀 html 파싱을 안함
import os.path
import csv
import json

from requests import Response


# url = 'https://www.melon.com/chart/'
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')
# print(soup.prettify())
# pprint.pprint(soup)
# print(soup)  안나온다

# request_headers = {
#     'User-Agent': ('Mozilla/5.0 (Windows NT 12.0; Win64; x64) AppleWebKit/537.36 '
#                    '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
#     'Referer': '',
# }

def requests_get(url: str) -> Response:
    request_headers: dict = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 12.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
        'Referer': '',
    }
    return requests.get(url, headers=request_headers)


url = 'https://www.melon.com/chart/'
# response = requests.get(url, headers=request_headers)
response = requests_get(url)
soup = bs(response.text, 'html.parser')
# print(soup)
# html 문서에 table 태그가 하나만 있음
# pprint.pprint(soup.select('table tbody tr')[0])
t1 = soup.select('table tbody tr')[0]
# print(t1)

# 제목
# t2 = t1.select('td')
# pprint.pprint(t2)
# print(f'제목 / 아티스트 / 앨범')
# datas = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
datas = soup.select('table tbody tr')

# pprint.pprint(datas.text)  # '밤양갱'

t4 = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
# pprint.pprint(t4.text)  # ' 비비'
# #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
dict_list: list[dict] = list()
for idx, item in enumerate(datas):
    # print(data.text.strip())
    # print(data.select_one('td'))
    # print(item.select_one('div.ellipsis.rank01 > span ').text.strip())  # 제목
    # print(item.select_one('div.ellipsis.rank02 > span > a').text.strip())  # 곡 가수
    # print(item.select_one('div.ellipsis.rank03').text.strip())  # 앨범
    # print(item.select_one('a src'))
    print(f'{idx + 1}')
    print(f'곡제목 : {item.select_one(".rank01").text.strip()}')
    print(f'가수 : {item.select_one(".rank02 a").text.strip()}')
    print(f'앨범 : {item.select_one(".rank03").text.strip()}')
    # print(item.get('td > div > a > img'))
    # print(item.select_one('div a img').get('src'))
    print(f'앨범이미지 : {item.select_one("td:nth-child(4) img").get("src")}')
    # print(f'앨범이미지 : {item.select_one("div a img").get("src")}')
    new_dict = dict()
    new_dict['순위'] = idx + 1
    new_dict['곡제목'] = item.select_one('div.rank01').text.strip()
    new_dict['가수'] = item.select_one('div.rank02 a').text.strip()
    new_dict['앨범'] = item.select_one('div.rank03').text.strip()
    dict_list.append(new_dict)

    # response = requests_get(item.select_one("div a img").get("src"))
    # with open(f"./output_image/melon/{idx}.jpg", "wb") as image_file:
    #     image_file.write(response.content)
    response = requests_get(item.select_one("div a img").get("src"))
    with open(f"./output_image/melon/{new_dict['순위']}_{new_dict['곡제목']}_{new_dict['가수']}.jpg", "wb") as image_file:
        image_file.write(response.content)
    # print('이미지 저장')

file_name = 'melon_chart.csv'
with open(f'./output/{file_name}', 'wt', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=dict_list[0].keys())

    writer.writeheader()
    for data in dict_list:
        writer.writerow(data)
print(f'{file_name} 저장 성공')

# 멜론 차트 가져오기
# 1) 순위, 곡제목, 가수, 앨범을 csv 로 저장
# 파일명 melon_chart.csv
# print(f'제목 / 아티스트 / 앨범')

# 2) 앨범 이미지를 저장
# 파일명 순위_곡제목_가수.jpg
# 54_사건의 지평선_윤하.jpg
