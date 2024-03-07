# 공공데이터포탈에서 `인천국제공항공사_여객편 주간 운항 현황` 검색
# xml만 지원, 키 필요
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15095074

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
# https://www.data.go.kr/iim/api/selectAPIAcountView.do

url: str = 'http://apis.data.go.kr/B551177/StatusOfPassengerFlightsDSOdp/getPassengerDeparturesDSOdp'
# 	여객편 주간 운항 현황-출발
"""공항별 여객 항공기 출발 조희일로부터 +6일간 운항정보 현황조회"""
# 요청변수(Request Parameter)
serviceKey: str = '9C0QXRXwHgqkBMTIJ0pl2l%2ByWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw%3D%3D'
type: str = 'xml'
airport_code: str = 'IAD'

# 공항 코드를 지워야 제대로 나옴
# parameter = f'?serviceKey={api_key}&airport_code={airport_code}&type={type}'
parameter = f'?serviceKey={serviceKey}&type={type}'

response = requests.get(url + parameter)

# print(response.url)  # 테스트
# print(response.content)   # 테스트 # 이건 안됨

xml_data = response.text
# print(xml_data)

dict_data = xmltodict.parse(xml_data)
# print(dict_data)
# print(type(dict_data))
# pprint.pprint(dict_data, indent=4)

dict_data_result: list[dict] = []
for data in dict_data['response']['body']['items']['item']:
    # pprint.pprint(data)   # 테스트
    if data.get('airline') and data['airline'] == '대한항공':
        # print(data['airline'])  # 대한항공만 나오는지 테스트
        dict_data_new: dict = dict()
        # print(data['airline'])
        # print(data['flightId'])
        # print(data['estimatedDateTime'])
        # print(data['airport'])
        dict_data_new['항공사'] = data['airline']
        dict_data_new['편명'] = data['flightId']
        dict_data_new['예정시간'] = data['estimatedDateTime']
        dict_data_new['도착지공항'] = data['airport']
        dict_data_result.append(dict_data_new)
# print(dict_data_result)
# pprint.pprint(dict_data_result, indent=4)

file_name: str = 'pus_international_air.csv'
with open(f'../output/{file_name}', 'wt', encoding='utf-8', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=dict_data_result[0].keys())
    # csv_writer = csv.DictWriter(csv_file, fieldnames=['항공사', '편명', '예정시간', '도착지공항'])  # 이렇게 하면 list[dict] 형태아니여도 됨
    csv_writer.writeheader()
    for row in dict_data_result:
        csv_writer.writerow(row)

print(f'{file_name}파일이 저장되었습니다:')
#
# 항공사 , 편명, 예정시간 도착지공항
# 응답 메시지
# airline : 항공사
# flightId : 편명
# scheduleDateTime : 예정시간
# airport : 도착지공항
