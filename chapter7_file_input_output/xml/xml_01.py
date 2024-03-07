# 네트워크로 주고 받을 때는 1줄이라도 Ctrl Alt L 을 이용해 포맷팅해서 사용하면된다.

import xmltodict
import pprint

with open('../input/XML/data.xml', 'r', encoding='utf-8') as xml_file:
    # xml 파일을 읽고, 딕셔너리로 변환
    dict_data = xmltodict.parse(xml_file.read(), xml_attribs=True)
    dict = xml_file.read()
    print(type(dict))  # <class 'str'>  xmltodict으로 파싱을 하지않고 단순히 read만 한 경우

    print(type(dict_data))  # <class 'dict'>    xmltodict으로 파싱한경우

    # print(dict_data) 
    # print(dict_data['response']['body']['items'])

    # 'response' > 'body' > 'items' 경로의 데이터를 'datas' 변수에 저장
    datas = dict_data['response']['body']['items']

    # 'datas' 변수에 저장된 데이터를 예쁘게 출력
    # pprint.pprint(datas)
