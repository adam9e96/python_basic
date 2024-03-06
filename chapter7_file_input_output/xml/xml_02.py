# 공공 데이터 포탈에서 '대구광역시_오페라하우스 공연일정' 검새. 키 필요없음
# https://www.data.go.kr/data/15057055/openapi.do
# 제목과 링크를 csv 저장
# 파일명 daeguperahouse_오늘날짜.csv 예) daeguperahouse_240306.csv

import pprint
import xmltodict
import requests
from datetime import datetime
import csv

# 1. 데이터 추출
url: str = 'http://www.daeguoperahouse.org/rss.php'
# openurl: str = 'http://www.daeguoperahouse.org'

# with open(f'../input/XML/daeguopera.xml', 'r', encoding='utf-8') as xml_file:

response = requests.get(url)
# print(response.url)
xml_data = response.text
# dict_data = xmltodict.parse(json_data)
# dict_data = json.loads(json_data)
# print(dict_data)

dict_data = xmltodict.parse(xml_data)
# pprint.pprint(dict_data)#출력용도임

# for i in dict_data['rss']['channel']:
#     print(i[1])
# print(type(dict_data))  # <class 'dict'>
# print(dict_data)

# print(dict_data['rss']['channel']['title'])
# print(dict_data['rss']['channel']['link'])
for element in dict_data['rss']['channel']:
    pass
    # print(element[0])
    # print(element[2])
# for data in  dict_data['rss']['channel']['title']:
#     print(data)


# with open('result.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
# 공연 정보 순회
dict_list: list[dict] = list()
for element in dict_data['rss']['channel']['item']:
    # pprint.pprint(element)
    new_dict: dict = dict()
    # case1
    new_dict['title'] = element['title']
    new_dict['link'] = element['link']
    # case2
    # title = element['title']
    # link = element['link']
    # print(element['title'])
    # print(element['link'])
    # writer.writerow([title, link])
    dict_list.append(new_dict)
    # writer.writerow([title, link])  # CSV 파일에 쓰기

# print(result_dict)
# # 현재 날짜로 파일명 생성
# import datetime
today_str = datetime.now().strftime("%y%m%d")  # 년월일 형식
print(today_str)
filename = f'daeguperahouse_{today_str}.csv'

with open(f'{filename}', 'wt', newline='',encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile,fieldnames=dict_list[0].keys())
    # writer = csv.writer(csvfile)
    # csv_writer.writerow(dict_list)
    csv_writer.writeheader()
    for row in dict_list:
        csv_writer.writerow(row)

print(f'{filename}파일이 저장되었습니다:')

#
# # 공연 정보 추출 및 CSV 파일 저장
# with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
#     writer.writerow(['title', 'link'])  # 컬럼명 작성
#
#     # 공연 정보 순회
#     for item in dict_data['rss']['channel']['item']:
#         title = item['title']
#         link = item['link']
#         writer.writerow([title, link])  # CSV 파일에 쓰기

