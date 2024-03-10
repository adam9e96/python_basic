# 다음 지시사항에 따라 서울특별시 마포구에 설치된 CCTV의 설치 목적을 종류별로 모두 파악하는
# 프로그램을 구현하세요.
#
# 지시사항
# 1. cctv.json 파일을 읽습니다.
# 2. cctv.json 파일은 UTF-8로 인코딩 되어 있습니다.
# (파일 오픈 시에  encoding='utf-8' 옵션이 들어가야 함)
# 예 : with open('./input/cctv.json', 'r', encoding='utf-8')
# 3. cctv.json 파일을 다음과 같은 데이터로 구성되어 있습니다.
# [
#     {
#         "관리기관명":"서울특별시 마포구청",
#         "소재지지번주소":"서교동 395-43",
#         "설치년월":"2005-07",
#         "보관일수":"30",
#         "카메라대수":"1",
#         "경도":"126.916711",
#         "소재지도로명주소":"양화로 72",
#         "위도":"37.550747",
#         "설치목적구분":"주정차단속",
#         "촬영방면정보":"360도전방면",
#         "데이터기준일자":"2020-05-20",
#         "카메라화소수":"200",
#         "관리기관전화번호":"02-3153-8432"
#     }
# }
#
# 실행 예 :
# {'방범(그린파킹)', '주정차단속', '방범(공원)', '방범', '방범(치수과)', '방범(경찰 설치)', '방범(어린이보호구역)'}


import json

with open('../input/JSON/cctv.json', 'r', encoding='utf-8') as json_file:
    json_data = json_file.read()
    # print(json_data)
    print(type(json_data))  # <class 'str'>

    # 테스트. loads가 iterator이라서 for문 돌려야됨
    cctv_list = json.loads(json_data)
    print(type(cctv_list))  # <class 'list'>

    for item in cctv_list:
        # print(item["설치목적구분"])  # <class 'list'>
        pass
    # print(cctv_list)

    cctv_purpose = set()
    for place in cctv_list:
        cctv_purpose.add(place['설치목적구분'])

print(cctv_purpose)
# {'주정차단속', '방범(공원)', '방범(치수과)', '방범(그린파킹)', '방범', '방범(경찰 설치)', '방범(어린이보호구역)'}
