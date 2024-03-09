import csv

import requests
from bs4 import BeautifulSoup as bs

# 벅스차트 크롤링

# step01. 제목, 가수, 앨범 출력
url: str = 'https://music.bugs.co.kr/chart/'
response = requests.get(url)
# print(response.text)
# print(response) # <Response [200]>
soup = bs(response.text, 'html.parser')
# print(response.status_code)
# print(soup)
# print(soup.prettify())

# print(soup.select('table > tbody > tr'))
# print(type(soup.select('table > tbody > tr')))  # <class 'bs4.element.ResultSet'>
# print(datas)
# for data in datas:
#     # print(type(data))   # <class 'bs4.element.Tag'>

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
    print(f'가수 : {item.select_one(".artist > a").text.strip().replace("/", ",")}')
    print(f'앨범 : {item.select_one(".album").text.strip()}')
    print(f'앨범이미지 : {item.select_one(".thumbnail img").get("src")}')
    # step2. 순위, 제목, 가수, 앨범 csv 저장
    # 파일명 : bugs_chart.csv
    dict_temp: dict = dict()
    dict_temp['순위'] = idx
    dict_temp['곡제목'] = item.select_one(".title a").text.strip()
    dict_temp['가수'] = item.select_one(".artist > a").text.strip().replace("/", ",")
    dict_temp['앨범'] = item.select_one(".album").text.strip()
    dict_data.append(dict_temp)
    # step 03. 앨범 이미지를 저장.
    # 파일명 순위_곡제목_가수.jpg
    # 예 ) 54_사건의 지평선_윤하 (YOUNHA).jpg
    # response = requests.get(item.select_one(".thumbnail img").get("src"))
    # with open(f"./output_image/bugs_image/{dict_temp['순위']}_{dict_temp['곡제목']}_{dict_temp['가수']}.jpg",
    #           'wb') as image_file:
    #     image_file.write(response.content)
    response = requests.get(item.select_one(".thumbnail img").get("src"))
    with open(f"./output_image/bugs/{dict_temp['순위']} _{dict_temp['곡제목']}_{dict_temp['가수']}.jpg", 'wb') as image_file:
        image_file.write(response.content)

# print(dict_data)
file_name: str = 'bugs_chart.csv'
with open(f'./output/{file_name}', 'wt', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=dict_data[0].keys())
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)
print(f'{file_name} 저장 완료')
