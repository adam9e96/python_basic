# 공공데이터포탈 data.go.kr
# 기상청_단기예보 ((구)_동네예보) 조회서비스
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15084084
# https://www.data.go.kr/iim/api/selectAPIAcountView.do
# 주소 : http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst
# 요청 변수
# 항목명(영문) / 항목명(국문) / 항목크기 / 항목구분 / 샘플데이터 / 항목설명
# serviceKey / 인증키 / 100 / 1 / 인증키 / (URL Encode) / 공공데이터포털에서 발급받은 인증키
# numOfRows / 한 페이지 결과 수 / 4 / 1 / 10 / 한 페이지 결과 수 Default: 10
# pageNo / 페이지 번호 / 4 / 1 / 1 / 페이지 번호 Default: 1
# dataType/ 응답자료형식 / 4 / 0 / XML / 요청자료형식(XML/JSON) Default: XML
# base_date / 발표일자 / 8 / 1 / 20210628 / ‘21년 6월 28일 발표
# base_time	/ 발표시각 / 4 / 1 / 0600 / 06시 발표(정시단위) -매시각 40분 이후 호출
# nx / 예보지점 X 좌표 / 2 / 1 / 55 /예보지점의 X 좌표값 *별첨 엑셀 자료 참조
# ny / 예보지점 Y 좌표 / 2 / 1 / 127 / 예보지점의 Y 좌표값 *별첨 엑셀 자료 참조
# ※ 항목구분 : 필수(1), 옵션(0), 1건 이상 복수건(1..n), 0건 또는 복수건(0..n)
# ※ 발표일자와 발표시각은 현재 기준으로 24시간 이내여야 함.


import requests
import json
import datetime

# 1. 초기값 설정
# 1) 서비스 키 : requests 사용시 자동으로 인코딩되어서 Decoding 된 키를 사용.
service_key: str = '9C0QXRXwHgqkBMTIJ0pl2l%2ByWXerreJmznFT1CnaS04AUbAz7zoq4jDC81qPCbmdpdSlcwNv29CfJKlD13rykw%3D%3D'

# 2) 날짜 및 시간 설정
now: datetime = datetime.datetime.now()  # 현재 날짜 및 시간 변환.
print(now)  # 2024-03-10 21:42:56.665177

base_date: str = '{:%Y%m%d}'.format(now)  # base_date에 날짜를 입력하기 위해 날짜를 출력 형식으로 지정.
print(base_date)    # 20240310

base_time: str = '{:02}00'.format(now.hour) if now.minute > 30 else '{:02}00'.format(now.hour - 1)
# 현재 분이 30분 이전이면 이전 시간(정시)을 설정.
print(base_time)    # 2100

# 3) 위치 값 (첨부 엑셀 확인)
# 대구광역기 중구 삼덕동 89 90
nx = 89
ny = 90

# 4) 응답자료형식
data_type = 'JSON'

# 5) url 설정
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
parameter = f'?serviceKey={service_key}&base_date={base_date}&base_time={base_time}&nx={nx}&ny={ny}&dataType={data_type}'
print(url + parameter)

# 2. 서버에서 요청값을 받은 후 파싱
# 딕셔너리 데이터를 분석해서 원하는 값을 추출.
response = requests.get(url + parameter)
json_data = response.text
print(json_data)
# print(type(json_data))  # <class 'str'>

dict_data: dict = json.loads(json_data)
# print(dict_data)
# print(type(dict_data))  # <class 'dict'>

weather_items = dict_data['response']['body']['items']['item']
#
print(f'발표 날짜: {weather_items[0]["baseDate"]}')
print(f'발표 시간: {weather_items[0]["baseTime"]}')
#
for k in range(len(weather_items)):
    weather_item = weather_items[k]
    obsr_value = weather_item['obsrValue']
    # T1H: 기온, RN1: 1시간 강수량, REH: 습도 %
    if weather_item['category'] == 'T1H':
        print(f' * 기온: {obsr_value}[℃]')
    elif weather_item['category'] == 'REH':
        print(f' * 습도: {obsr_value} [%]')
    elif weather_item['category'] == 'RN1':
        print(f' * 1시간 강수량: {obsr_value} [mm]')
