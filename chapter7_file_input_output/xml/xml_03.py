# 공공데이터포탈에서 '한국공항공사_노선별 소요시간 및 거래 정보' 검색
# xml만 지원, 키 필요
#
#

# 인천공항공사 에서 제공하는 API 라, 인천공항은 지원하지 않음. 인천공항은 인천국제공항공사 소속.

# 당일 부산에서 출발하는 국제선 정보 구하기
# 도착공항명, 운항거리 운항시간을 csv로 저장
# 파일명 : pus_international_air.csv
# Python3 샘플 코드 #

import pprint
import xmltodict
import requests
from datetime import datetime
import csv

# 인천국제공항공사_여객기 주간 운항 현황 조회 서비스
api_key: str = '9C0QXRXwHgqkBMTIJ0pl2l%2ByWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw%3D%3D'
url: str = 'http://apis.data.go.kr/B551177/StatusOfPassengerFlightsDSOdp/getPassengerDeparturesDSOdp'
# serach_date_first = '20240306'
# serach_date_last = '20240306'
type: str = 'xml'
airport_code: str = 'IAD'
# parameter = f'?serviceKey={api_key}&airport_code={airport_code}&type={type}'
parameter = f'?serviceKey={api_key}&type={type}'
response = requests.get(url + parameter)

# print(response.url)
# print(response.content)

xml_data = response.text
# print(xml_data)
# print(type(xml_data))
dict_data = xmltodict.parse(xml_data)
# print(dict_data)
# print(type(dict_data))

# pprint.pprint(dict_data)
dict_data_result: list[dict] = []
for data in dict_data['response']['body']['items']['item']:
    pprint.pprint(data)
    if data.get('airline') and data['airline'] == '대한항공':
        print(data['airline'])
        dict_data_new: dict = dict()
        # print(data['airline'])
        # print(data['airport'])
        # print(data['estimatedDateTime'])
        dict_data_new['항공사123'] = data['airline']
        dict_data_new['편명123'] = data['flightId']
        dict_data_new['예정시간123'] = data['estimatedDateTime']
        dict_data_new['도착지공항123'] = data['airport']
        dict_data_result.append(dict_data_new)
# ['항공사','편명','예정시간','도착지공항']
# print(dict_data_result)

# pprint.pprint(dict_data_result, indent=4)

file_name: str = 'IAD_01.csv'
with open(f'../output/{file_name}', 'wt', encoding='utf-8',newline='') as csv_file:
    # csv_writer = csv.DictWriter(csv_file, fieldnames=dict_data_result[0].keys())
    csv_writer = csv.DictWriter(csv_file, fieldnames=['항공사123','편명123','예정시간123','도착지공항123'])
    csv_writer.writeheader()
    for row in dict_data_result:
        csv_writer.writerow(row)
#
print(f'{file_name}파일이 저장되었습니다:')
#
# 항공사 , 편명, 예정시간 도착지공항
# 응답 메시지
# airline : 항공사
# flightId : 편명
# scheduleDateTime : 예정시간
# airport : 도착지공항
