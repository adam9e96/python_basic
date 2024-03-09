import csv

import requests
from bs4 import BeautifulSoup as bs

# 벅스차트 크롤링

# step01. 제목, 가수, 앨범 출력
url: str = 'https://music.bugs.co.kr/chart/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)
# datas = soup.select('table > tbody > tr')
# print(soup.select('table > tbody > tr'))
# print(len(soup.select('table.trackList tbody tr')))
# CHARTrealtime > table
# print(soup.select('table.trackList tbody tr'))
# dict_list: list[dict] = list()
# for idx, item in enumerate(datas):
# print(soup.select('table.list.trackList.byChart tbody tr'))# 이렇게도 된다
# for tr in soup.select('table.list.trackList.byChart tbody tr'):
#     print(tr.select_one('.title a').text.strip())

dict_data: list[dict] = list()
for idx, item in enumerate(soup.select('table.list.trackList.byChart tbody tr'), 1):
    print(f'순서 : {idx}')
    print(f'곡제목 : {item.select_one(".title a").text.strip()}')
    print(f'가수 : {item.select_one(".artist > a").text.strip()}')
    print(f'앨범 : {item.select_one(".album").text.strip()}')

    dict_temp: dict = dict()
    dict_temp['순위'] = idx
    dict_temp['곡제목'] = item.select_one(".title a").text.strip()
    dict_temp['가수'] = item.select_one(".artist > a").text.strip()
    dict_temp['앨범'] = item.select_one(".album").text.strip()
    dict_data.append(dict_temp)
print(dict_data)
file_name : str = 'bugs_chart.csv'
with open(f'./output/{file_name}', 'wt', newline='',encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=dict_data[0].keys())
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)
print(f'{file_name} 저장 완료')