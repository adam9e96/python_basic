import pprint
import requests
from bs4 import BeautifulSoup as bs  # <--은 지금 안씀 html 파싱을 안함
import os.path
import csv
import json
from requests import Response

url = 'https://www.melon.com/chart/'


# response = requests.get(url)
# soup = bs(response.text, 'html.parser')


# print(soup.prettify())
# pprint.pprint(soup)
# print(soup)  # 안나온다

# request_headers = {
#     'User-Agent': ('Mozilla/5.0 (Windows NT 12.0; Win64; x64) AppleWebKit/537.36 '
#                    '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
#     'Referer': '',
# }
# response = requests.get(url,headers=request_headers)
# soup = bs(response.text, 'html.parser')
# print(soup) # 나온다.

def requests_get(url: str) -> Response:
    request_headers: dict = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 12.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
        'Referer': '',
    }
    return requests.get(url, headers=request_headers)


url = 'https://www.melon.com/chart/'
response = requests_get(url)
soup = bs(response.text, 'html.parser')
# print(soup)
# html 문서에 table 태그가 하나만 있음
# print(soup.prettify()) #

# pprint.pprint(soup.select('table tbody tr')[0])
# t1 = soup.select('table tbody tr')[0]
# print(t1)

# 제목
# t2 = t1.select('td')
# pprint.pprint(t2)
# print(f'제목 / 아티스트 / 앨범')
# datas = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
datas = soup.select('table tbody tr')
# print(datas)
# print(datas[0])

# pprint.pprint(datas[0].text.split()) # 일단 이안에 제목 가수 등 다있다는 것을 확인

dict_list: list[dict] = list()
for idx, item in enumerate(datas, 1):
    # print(f'{idx + 1}')
    print(f'순위 : {idx}')
    # print(f'곡제목 : {item.select_one("div.ellipsis.rank01 span a").text}')
    # print(f'가수 : {item.select_one("div.ellipsis.rank02 a").text.strip()}')
    # print(f'앨범 : {item.select_one("div.ellipsis.rank03").text.strip()}')
    # print(f'앨범이미지 : {item.select_one("a.image_typeAll img").get("src")}')
    # print(f'앨범이미지2 : {item.select_one("div a img").get("src")}')
    # print(f'앨범이미지3 : {item.select_one("td img").get("src")}')
    # print(f'앨범이미지4 : {item.select_one("td>div>a>img").get("src")}')

    dict_temp: dict = dict()
    dict_temp['순위'] = idx
    dict_temp['곡제목'] = item.select_one("div.ellipsis.rank01 span a").text.strip()
    dict_temp['가수'] = item.select_one("div.ellipsis.rank02 a").text.strip()
    dict_temp['앨범'] = item.select_one("div.ellipsis.rank03").text.strip()
    dict_list.append(dict_temp)
    response = requests.get(item.select_one("a.image_typeAll img").get("src"))
    with open(f"./output_image/melon/{dict_temp['순위']}_{dict_temp['곡제목']}_{dict_temp['가수']}.jpg", 'wb') as image_file:
        image_file.write(response.content)

# print(dict_list)
# t2 = soup.select('table tbody')
file_name = 'melon_chart.csv'
with open(f'./output/{file_name}', 'wt', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, dict_list[0].keys())
    writer.writeheader()
    for item in dict_list:
        writer.writerow(item)
    print(f'{file_name} 저장 성공')

# for idx, item in enumerate(datas):
# response = requests_get(item.select_one("div a img").get("src"))
# with open(f"./output_image/melon/{idx}.jpg", "wb") as image_file:
#     image_file.write(response.content)
# response = requests_get(item.select_one("div a img").get("src"))
# with open(f"./output_image/melon/{new_dict['순위']}_{new_dict['곡제목']}_{new_dict['가수']}.jpg", "wb") as image_file:
#     image_file.write(response.content)
# print('이미지 저장')

#

# 멜론 차트 가져오기
# 1) 순위, 곡제목, 가수, 앨범을 csv 로 저장
# 파일명 melon_chart.csv
# print(f'제목 / 아티스트 / 앨범')

# 2) 앨범 이미지를 저장
# 파일명 순위_곡제목_가수.jpg
# 54_사건의 지평선_윤하.jpg
