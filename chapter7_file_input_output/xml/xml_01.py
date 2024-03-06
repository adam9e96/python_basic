# 네트워크로 주고 받을 때는 1줄이라도 Ctrl Alt L 을 이용해 포맷팅해서 사용하면된다.

import xmltodict
import pprint

with open('data.xml', 'r', encoding='utf-8') as xml_file:
    dict_data = xmltodict.parse(xml_file.read(), xml_attribs=True)  # xml 데이터를 딕셔너리로 변경
    # print(dict_data)
    # print(dict_data['response']['body']['items'])
    datas = print(dict_data['response']['body']['items'])
    pprint.pprint(datas)
