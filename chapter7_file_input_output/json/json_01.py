import json
from typing import List

dict_list: List[dict] = [
    {
        'name': 'james',
        'age': 20,
        'spec': [
            175.5,
            70.5
        ]
    },
    {
        'name': 'alice',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    }

]
json_string: str = json.dumps(dict_list,indent=4)   # indent는 보기는 좋으나 실제 네트워크에서 주고 받을 때는 안쓰는게 좋음
# print(json_string)    # json.dumps()의 반환형이 str임.

with open('../output/dict_list_02.json', 'w') as file:
    file.write(json_string)
print('dict_list_02.json 파일이 생성되었습니다.')

with open('../output/dict_list_02.json', 'r') as file:
    json_reader = file.read()
    # print(json_reader)
    dict_list = json.loads(json_reader) # loads() 함수를 쓰면 적당한 데이터 타입으로 변환해서 저장해줌.
    print(dict_list)
    print(type(dict_list))  # <class 'list'>

for dic in dict_list:
    print('이름: {}'.format(dic['name']))
    print('나이: {}'.format(dic['age']))
    print('키: {}'.format(dic['spec'][0]))
    print('몸무게: {}'.format(dic['spec'][1]))
    print()


import csv
import json
#
# DictWriter 객체는 csv 파일을 생성하기 위해 딕셔너리를 사용.
output_file = open('../output/output_with_header2.csv', 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
# 파일에 헤더 행을 넣고 싶으면 writeheader() 를 호출

output_dict_writer.writeheader()
#
# # writerow() 메서드를 호출하여 각 행을 쓸 수 있는데, 이 떄 딕셔너리를 사용.
# 딕셔너리의 키는 헤더이고, 딕셔너리의 값은 파일에 쓰려는 데이터가 들어감.
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})  # 누락된 키는 빈 상태로 나옴.
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})  # 순서는 중요하지 않음
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})  # 순서는 중요하지 않음
output_file.close()

print('12345')
# 2. loads() 함수를 사용하여 JOSN 읽기.

string_json_data: str = '{"Name":"Zopgie","isCat":true,"miceCaught":0,"felineIQ":null}' # json 타입으로 맞춰진 형태,자바와 비슷함
json_data_as_python_value = json.loads(string_json_data)
print(type(json_data_as_python_value))  # <class 'dict'>

print(json_data_as_python_value)    # {'Name': 'Zopgie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}  # 파이썬 타입으로 맞춰진 형태

# 중요
# 온라인에서 JSON 파일 열기
import urllib.request as request
json_data = request.urlopen('https://jsonplaceholder.typicode.com/todos/1').read()
print(type(json_data))  #   <class 'bytes'>
python_data = json.loads(json_data)
print(type(python_data)) # <class 'dict'>
print(python_data)  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
# print(python_data['userId'])  # 1

"""
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
"""

# 3. dumps() 함수를 이용하여 JSON 작성하기.
# 파이썬 값을 JSON 형식 데이터 문자열로 변환.
python_data: dict = {'Name': 'Zopgie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
json_data: str = json.dumps(python_data)
print(type(json_data))  # <class 'str'>

print(json_data)    # {"Name": "Zopgie", "isCat": true, "miceCaught": 0, "felineIQ": null}
