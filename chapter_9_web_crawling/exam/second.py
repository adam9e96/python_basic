# 2. 공공데이터 포털(data.go.kr)에서 '대구광역시_음식골목‘를 API 연결을 통해 데이터를 수집하시오.
#
#    데이터중에 동구의 음식골목 데이터중 추출하여 각 음식골목의 대표음식점의 상호와 주소를 골라내 음식골목명, 음식점 상호,
#
#    음식점 주소를 csv로 저장하시오.
#
#    필요 데이터
#
#    파일명은 daegufood_street.csv로 하시오.
import json
import requests
import csv

url = 'https://www.daegufood.go.kr/kor/api/Alley.html?mode=json'
response = requests.get(url)
# print(response.url)

dict_data = json.loads(response.text)
# print(dict_data)

# print(dict_data["data"])
dict_daegufood: list[dict] = list()
for item in dict_data["data"]:
    # print(item['FD_CS'])
    if item['FD_CS'].find('동구') >= 0:
        temp_dict = dict()
        temp_dict['OPENDATA_ID'] = item['OPENDATA_ID']
        dict_daegufood.append(temp_dict)
# print(dict_daegufood)


url = 'https://www.daegufood.go.kr/kor/api/Alley_food.html'
dict_daegu_total: list[dict] = list()
for item in dict_daegufood:
    # print(item)
    # print(item['OPENDATA_ID'])
    parameter = f'?mode=json&OPENDATA_ID={item["OPENDATA_ID"]}'
    response = requests.get(url + parameter)
    dict_data = json.loads(response.text)
    # print(dict_data)
    # print(dict_data["data"])
    # print(dict_data['data'][0]['FD_CS'])
    # print(dict_data['data'][0]['BZ_NM'])
    # print(dict_data['data'][0]['GNG_CS'])
    for item2 in dict_data["data"]:
        # print(item2)
        temp_dict2 = dict()
        print(f'음식골목명 = {item2["FD_CS"]}')
        print(f'음식점 상호 : {item2["BZ_NM"]}')
        print(f'음식점 주소 : {item2["GNG_CS"]}')
        temp_dict2['음식골목명'] = item2["FD_CS"]
        temp_dict2['음식점 상호'] = item2["BZ_NM"]
        temp_dict2['음식점 주소'] = item2["GNG_CS"]
        dict_daegu_total.append(temp_dict2)
# print(dict_daegu_total)

file_name: str = 'daegufood_street.csv'
with open(f'{file_name}', 'wt', newline='') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=dict_daegu_total[0].keys())
    csvwriter.writeheader()
    for item in dict_daegu_total:
        csvwriter.writerow(item)
    print(f'{file_name} 저장 성공')
