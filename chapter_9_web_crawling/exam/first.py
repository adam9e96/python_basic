# https://www.data.go.kr/iim/api/selectAPIAcountView.do
# 데이터명 : 대구광역시 북구_둘레길
import json
from urllib import request

import requests
import json
import csv

# 문제
# 1. 공공데이터 포털(data.go.kr)에서 '대구광역시 북구_둘레길‘를 API 연결을 통해 데이터를 수집하시오.
#    데이터중에 도덕산과 함지산의 데이터를 뽑아서 산 명, 노선, 거리, 소요시간을 csv로 저장하시오.
#    파일명은 bukgu_trail.csv로 하시오.

# 요구 데이터
# 도덕산, 함지산의 산 명, 노선, 거리, 소요시간


# 요구 파라미터
api_key: str = '9C0QXRXwHgqkBMTIJ0pl2l%2ByWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw%3D%3D'

# 산 조회
url: str = 'http://apis.data.go.kr/3450000/bukguDulleRoadService/getBukguDulleRoad'
parameter: str = f'?serviceKey={api_key}&currentPage=1&perPage=10&MNTN_NM=도덕산'

response = requests.get(url + parameter)
# print(response.url)

json_data = response.text  # 문자열로 저장
dict_data = json.loads(json_data)
# print(dict_data)

# 도덕산
mount_dict: list[dict] = list()
for data in dict_data['body']:
    # print(data['MNTN_NM'])  # 산 명
    # print(data['ROUTE'])  # 노선
    # print(data['DSTNC'])  # 거리
    # print(data['REQRE_TIME'])  # 소요 시간
    temp_dict = dict()
    temp_dict['산 명'] = data['MNTN_NM']
    temp_dict['노선'] = data['ROUTE']
    temp_dict['거리'] = data['DSTNC']
    temp_dict['소요 시간'] = data['REQRE_TIME']
    mount_dict.append(temp_dict)

# 함지산
parameter: str = f'?serviceKey={api_key}&currentPage=1&perPage=10&MNTN_NM=함지산'
response = requests.get(url + parameter)
json_data = response.text  # 문자열로 저장
dict_data = json.loads(json_data)

for data in dict_data['body']:
    # print(data['MNTN_NM'])  # 산 명
    # print(data['ROUTE'])  # 노선
    # print(data['DSTNC'])  # 거리
    # print(data['REQRE_TIME'])  # 소요 시간
    temp_dict = dict()
    temp_dict['산 명'] = data['MNTN_NM']
    temp_dict['노선'] = data['ROUTE']
    temp_dict['거리'] = data['DSTNC']
    temp_dict['소요 시간'] = data['REQRE_TIME']
    mount_dict.append(temp_dict)

file_name = 'bukgu_trail.csv'
with open(f'{file_name}', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=mount_dict[0].keys())
    csv_writer.writeheader()
    for data in mount_dict:
        csv_writer.writerow(data)
    print(f'{file_name} 저장 성공')
