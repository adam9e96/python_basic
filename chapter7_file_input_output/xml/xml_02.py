# 공공 데이터 포탈에서 '대구광역시_오페라하우스 공연일정' 검새. 키 필요없음
# https://www.data.go.kr/data/15057055/openapi.do
# https://www.daegu.go.kr/index.do?menu_id=00000277
# 제목과 링크를 csv 저장
# 파일명 daeguperahouse_오늘날짜.csv 예) daeguperahouse_240306.csv

import pprint
import xmltodict
import requests
from datetime import datetime
import csv
import json

# 1. 데이터 추출
# 대구오페라하우스 공연일정 소개
# https://www.daegu.go.kr/index.do?menu_id=00000277
url: str = 'http://www.daeguoperahouse.org/rss.php'

response = requests.get(url)
# print(type(response))   # <class 'requests.models.Response'>
# print(response.url)   # 테스트

# 서버로부터 받은 응답 내용을 텍스트로 저장
xml_data = response.text
# print(type(xml_data))   # <class 'str'>

dict_data = xmltodict.parse(xml_data)
# print(dict_data)

# print(type(dict_data))  #  <class 'dict'>
s
# pprint.pprint(dict_data)    #출력용도임

# print(dict_data['rss']['channel']['title'])
# print(dict_data['rss']['channel']['link'])

# 공연 정보 순회
dict_list: list[dict] = list()
for element in dict_data['rss']['channel']['item']:
    # print(element)
    new_dict: dict = dict()

    # case1
    new_dict['title'] = element['title']
    new_dict['link'] = element['link']
    # print(element['title']) # 테스트
    # print(element['link'])  # 테스트

    dict_list.append(new_dict)

print(dict_list)

# 공연 정보 추출 및 CSV 파일 저장
# 현재 날짜로 파일명 생성 # CSV 형식으로 저장
from datetime import datetime

today_str = datetime.now().strftime("%y%m%d")  # 년월일 형식
print(today_str)  # 테스트
filename = f'daeguperahouse_{today_str}.csv'

with open(f'../output/{filename}', 'wt', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=dict_list[0].keys())
    # print(type(dict_list[0]))  # <class 'dict'>
    # print(type(csv_writer)) # <class 'csv.DictWriter'>

# https://docs.python.org/3.10/library/csv.html#csv.DictWriter.writeheader
    csv_writer.writeheader()
    # writer = csv.writer(csvfile)
    for row in dict_list:
        csv_writer.writerow(row)

print(f'{filename}파일이 저장되었습니다:')
