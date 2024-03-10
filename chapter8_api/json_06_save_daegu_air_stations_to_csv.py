# 공공데이터 포탈에서 '한국환경공간 에어코리아 측정소 정보' 검색 후 활용신청. 키사용.
# https://www.data.go.kr/data/15073877/openapi.do

# 측정소 목록 조회 서비스를 이용
# 대구에 있는 측정소의 측정소 명, 층정소 주소, 위도, 경도, 설치년도를 csv 파일로 저장
# 파일명 : daegu_air_list.csv

import urllib.request as request
import json
import datetime
import csv

import requests

# 1) 서비스키
# service_key: str = '9C0QXRXwHgqkBMTIJ0pl2l+yWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw==' # Decoding
service_key: str = '9C0QXRXwHgqkBMTIJ0pl2l%2ByWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw%3D%3D' # Encoding

addr: str = '대구'
pageNo: int = 1
returnType: str = 'json'

# 측정소 목록 조회
url: str = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getMsrstnList'
parameter: str = f'?serviceKey={service_key}&returnType={returnType}&numOfRows=100&pageNo={pageNo}&addr={addr}'

response = requests.get(url + parameter)
print(response.url)
json_data = response.text
dict_data = json.loads(json_data)
# print(dict_data)
who_list: list[dict] = list()
for item in dict_data['response']['body']['items']:
    # print(item['addr'])
    if not item['addr'].find('부산') >= 0:
        # print(item['stationName'])  # 측정소 명
        # print(item['addr']) # 측정소 주소
        # print(item['dmX']) # 위도
        # print(item['dmY']) # 경도
        # print(item['year']) # 설치년도
        Dic_new_data: dict = dict()
        Dic_new_data['stationName'] = item['stationName']
        Dic_new_data['addr'] = item['addr']
        Dic_new_data['dmX'] = item['dmX']
        Dic_new_data['dmY'] = item['dmY']
        Dic_new_data['year'] = item['year']
        who_list.append(Dic_new_data)

# print(who_list)
# for data in who_list:
#     print(data)

# 측정소 명, 층정소 주소, 위도, 경도, 설치년도
with open('./output/json06.csv', 'w', newline='', encoding='utf-8') as file:
    # dict_wirter = csv.DictWriter(file)
    dict_writer = csv.DictWriter(file, fieldnames=['stationName', 'addr', 'dmX', 'dmY', 'year'])
    dict_writer.writeheader()
    for data in who_list:
        data: dict
        dict_writer.writerow(data)
print(f'json_06.csv 가 생성되었습니다.')


#