# 공공데이터 포털에서 '인천국제공항공사_버스정보' 검색
# https://www.data.go.kr/data/15095045/openapi.do
# 인천국제공항 여객터미널 T1, T2 버스 정보(공항행 첫차/막차, 종점행 첫차/막차, 성인요금,
# 버스등급, 버스번호, 지역, 운수사, 평일시간, 주말시간, 노선정보, 승차위치)를 제공
import csv
import pprint

# 인천국제공항에서 대구로 가는 버스 목록
# 버스번호, 버스등급, 성인요금, 평일시간표, 주말시간표를 csv로 저장
# 시간표는 이른 시간이 먼저 나오도록
# 예) '0610, 0630, 0810, 0830, 1130, 1150, 1740, 1800',
# 파일명 air_bus_daegu.csv
# 서비스키 : serviceKey
# 한페이지 결과수 : numOfRows
# 데이터 표출 페이지 : pageNo
# 지역: area : 1:서울, 2:경기, 3:인천, 4:강원, 5:충청, 6:경상, 7:전라, default=1
# 응답유형 : type: [xml, json] default=xml

import requests
import xmltodict

service_key_decode: str = '9C0QXRXwHgqkBMTIJ0pl2l+yWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw=='
service_key_encode: str = '9C0QXRXwHgqkBMTIJ0pl2l%2ByWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw%3D%3D'
area: int = 6
type: str = 'xml'
url: str = 'http://apis.data.go.kr/B551177/BusInformation/getBusInfo'
num_of_rows: int = 50
parameter: str = f'?serviceKey={service_key_encode}&area={area}&numOfRows={num_of_rows}&pageNo=1&type={type}'

# print(url+parameter)
response = requests.get(url + parameter)
print(response.url)  # 테스트

xml_data = response.text
# print(type(xml_data))   # <class 'str'>

dict_data = xmltodict.parse(xml_data)


# print(dict_data)
# print(type(dict_data))

def sort_str(string1: str, string2: str) -> str:
    # 기본 데이터는 문자열. 2개의 문자열을 결합하고, 공백제거 후, 리스트로 변환
    temp_list: list[str] = (string1 + ', ' + string2).replace(' ', '').split(",")
    temp_list = list(set(temp_list))  # 중복 제거
    temp_list.sort()  # 정렬
    return str(temp_list)[1:-1].replace("'", '')


dict_datas: list[dict] = []
for item in dict_data['response']['body']['items']['item']:
    # print(item['routeinfo'])
    if item['routeinfo'].find('대구') != -1:
        # print(item)
        # print(item['busnumber'])  # 버스번호
        # print(item['busclass'])  # 버스등급
        # print(item['adultfare'])  # adultfare
        # print(item['t1wdayt'])  # T1평일시간표
        # print(item['t1wt'])  # t1주말시간표
        # print(item['t2wdayt'])  # T2평일시간표
        # print(item['t2wt'])  # t1주말시간표
        dict_temporary = dict()
        dict_temporary['버스번호'] = item['busnumber']  # 버스번호
        dict_temporary['버스등급'] = item['busclass']  # 버스등급
        dict_temporary['성인요금'] = item['adultfare']  # adultfare
        # 기본 데이터는 문자열. 2개의 문자열을 결합하고, 공백제거 후, 리스트로 변환
        dict_temporary['평일시간표'] = sort_str(item['t1wdayt'], item['t2wdayt'])

        dict_temporary['주말시간표'] = sort_str(item['t1wt'], item['t2wt'])

        # temp_list: list[str] = (item['t1wdayt'] + ', ' + item['t2wdayt']).replace(' ', '').split(',')
        # temp_list = list(set(temp_list))  # 중복 제거
        # temp_list.sort()  # 정렬
        # dict_temporary['평일시간표'] = str(temp_list)[1:-1].replace("'", '')
        #
        # temp_list: list[str] = (item['t1wt'] + ', ' + item['t2wt']).replace(' ', '').split(',')
        # temp_list = list(set(temp_list))  # 중복제거
        # temp_list.sort()  # 정렬
        # dict_temporary['주말시간표'] = str(temp_list)[1:-1].replace("'", '').replace('[', '').replace(']', '')

        dict_datas.append(dict_temporary)
print(dict_datas)

file_name: str = 'air_bus_daegu.csv'
with open(f'../chapter7_file_input_output/output/{file_name}', 'wt', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, dict_datas[0].keys())
    csv_writer.writeheader()
    for item in dict_datas:
        csv_writer.writerow(item)
print(f'{file_name}이 저장되었습니다.')

# CSV 저장로직을 함수화
from share import save_csv

# def save_csv(file_path: str, dict_list: list[dict]) -> None:
#     with open(f'../output/{file_path}', 'wt', newline='', encoding='utf-8') as csv_file:
#         csv_writer = csv.DictWriter(csv_file, fieldnames=dict_list[0].keys())
#         csv_writer.writeheader()
#         for item in dict_list:
#             csv_writer.writerow(item)
#     print(f'{file_path}이 저장되었습니다.')

save_csv('abcdefg.csv', dict_datas)
# 이게 함수를 사용하는 이유.
