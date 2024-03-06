import csv
import json

import requests

# 서비스 키
service_key: str = '9C0QXRXwHgqkBMTIJ0pl2l%2ByWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw%3D%3D'

addr: str = '대구'
pageNo: int = 1
returnType: str = 'json'
addrs: str = '신기동'

# 3 
url: str = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getTMStdrCrdnt'
parameter: str = f'?umdName={addrs}&pageNo={pageNo}&numOfRows=10&returnType={returnType}&serviceKey={service_key}'
# TM 기준좌표 조회
response = requests.get(url + parameter)
# print(response.url)
json_data = response.text
dict_data = json.loads(json_data)
# print(dict_data)

nex_x_y: list[dict] = list()

for data in dict_data['response']['body']['items']:
    # print(data)
    if data['sggName'].find('동구') >= 0:
        new_dict: dict = dict()
        new_dict['tmX'] = data['tmX']
        new_dict['tmY'] = data['tmY']
        nex_x_y.append(new_dict)
print(nex_x_y)

tmX = nex_x_y[0]['tmX']
tmY = nex_x_y[0]['tmY']

# 2

url: str = 'http://apis.data.go.kr/B552584/MsrstnInfoInqireSvc/getNearbyMsrstnList'
parameter: str = f'?tmX={tmX}&tmY={tmY}&returnType={returnType}&serviceKey={service_key}'

response = requests.get(url + parameter)
# print(response.url)
json_data = response.text
dict_data = json.loads(json_data)
# print(dict_data)

total_dict: list[dict] = list()
for item in dict_data['response']['body']['items']:
    print(item)
    dit_new: dict = dict()
    dit_new['stationName'] = item['stationName']  # 측정소 명
    dit_new['addr'] = item['addr']  # 측정소 주소
    # dit_new['addr'] = item['addr']   # 측정소가 위치한 주소
    total_dict.append(dit_new)
    print(item)

print(total_dict)
with open('../output/json_06_01.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=['stationName', 'addr'])
    csv_writer.writeheader()
    for item in total_dict:
        item: dict
        csv_writer.writerow(item)
print('json6_3.csv 저장되었다. 성공!')
