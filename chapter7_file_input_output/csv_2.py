# 문제 1번
# 다음 지시사항에 따라 서울특별시 마포구에 설치된 CCTV의 개수를 구하는
# 프로그램을 구현하세요.
import csv

# 지시사항
# 1. cctv.csv 파일을 읽습니다.
# 2. 모든 라인에 존재하는 카메라 개수를 합한 결과를 출력합니다.
# 5번째 데이터가 카메라 대수 입니다.

# 실행 예:
# 서울특별시 마포구에 설치된 CCTV는 총 2167 대입니다.

# DictReader 이용할 것
# with open('./input/CSV/cctv.csv') as file:
#     datas = csv.DictReader(file)
#
#     # print(cctv_file_reader)
#     total_cctv = 0
#     for data in datas:
#         # print(data['카메라대수'])
#         total_cctv += int(data['카메라대수'])
#
# print(f'서울특별시 마포구에 설치된 CCTV는 총 {format(total_cctv, ",")} 대입니다.')


# 문제 2번
# with open('./input/CSV/pop_seoul.csv') as file:
#     datas2 = csv.DictReader(file)
#     print(datas2)
#     for data in datas2:
#         print(data)
#     print(data["Foreigner"])
#     korean = int(data["Korean"])
#     foreigner = int(data["Foreigner"])
#     print(korean)

# 1. pop_seoul.csv 파일을 읽어서 딕셔너리로 출력
example_file = open('./input/CSV/pop_seoul.csv')
example_file_reader = csv.DictReader(example_file)  # dict 형식으로 파일을 읽기
# print(list(example_file_reader))

result = []

for row in example_file_reader:
    # print(row)
    # print(row["Korean"])
    # print(row["Foreigner"])
    korean = int(row["Korean"].replace(",", ""))
    foregin = int(row["Foreigner"].replace(",", ""))
    senior = int(row["Senior"].replace(",", ""))
    rate = foregin / (korean + foregin + senior) * 100

    if rate > 3:
        # print(f"{rate}")    # 테스트
        # print(row)  # 테스트
        # print(rate)   # 테스트
        result.append(row)


# print(result)
# # print(out_file_writer)
# example_file.close()
#
pop_seoul_result = open('./output/pop_seoulresult.csv', 'w',newline='')
pop_seoul_writer = csv.writer(pop_seoul_result)
for row in result:
    pop_seoul_writer.writerow([row])
pop_seoul_result.close()


# 개발 절차
# 1. pop_seoul.csv 파일을 읽어서 딕셔너리로 출력
# 2. 반복문을 돌려서 한 행씩 출력
# 3. 한 행씩 출력하는 코드에서 외국인 비율을 구해서 출력
# 4. 조건(비율이 3% 이상)에 해당하는 데이터만 리스트나 딕셔너리로 저장
# 5. 저장된 데이터를 csv로 저장

import csv
new_datas: list = []
with open('./input/CSV/pop_seoul.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # 외국인 비율 : 외국인 / 총 인구수(한국인+외국인) * 100
        # 구별 총 인구수 출력 : 데이터가 문자열이라서 콤마(,)를 제거해야 정수로 형변환 가능
        total_population: int = int(row["Korean"].replace(',','')) + int(row["Foreigner"].replace(',','')) + int(row["Senior"].replace(',',''))
        print(f'{row["Gu"]}의 총 인구 수 : {total_population}')

        # 외국인 비율
        rate_foreigner:float = int(row["Foreigner"].replace(',','') ) / total_population *100
        print(f'{row["Gu"]}의 외국인비율 : {rate_foreigner}')

        if rate_foreigner >= 3.0:
            new_data: dict = dict()
            new_data["Gu"] = row["Gu"]
            new_data["Korean"] = row["Korean"]
            new_data["Foreigner"] = row["Foreigner"]
            new_data["Rate"] = round(rate_foreigner, 1)
            new_datas.append(new_data)


# print(new_datas)

with open('./output/pop_seoul.csv','w',newline='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=['Gu','Korean','Foreigner','Rate'])
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)


# 부동상 실거래 파일 http://rtdown.molit.go.kr/ 다운 받아 사용.
# 계약일자는 기본 값, 파일 구분은 CSV, 나머지는 기본 값 사용

# 24년 update : 홈페이지 접근 후 [자료제공 바로가기] 클릭
# 전국은 1달치, 지역을 지정하면 1년치
# 대구 1년치로 작업
# 계약일자는 기본 값, 파일 구분은 CSV, 나머지는 기본 값 사용.
# 다운 받은 후 메모장에서 파일을 열고 15행까지는 삭제.