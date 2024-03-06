import xmltodict

# 파일에서 XML 데이터 읽기
with open('example.xml', 'r') as file:
    xml_data = file.read()

print(type(xml_data))
# XML을 dict로 변환
data_dict = xmltodict.parse(xml_data)

# 데이터 접근
print(data_dict['root']['child'])
