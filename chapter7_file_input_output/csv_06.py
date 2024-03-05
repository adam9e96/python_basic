# 조건 : 각 구별 롯데캐슬 거래건수 검색
# 출력조건 : 구(구만 나오도록 할 것), 거래건수
# 저장 파일명 : apt_2403_조건3.csv
# with로 파일 처리

# 구,거래건수
# 중구,110
# 동구,49
# 서구,158
# 북구,17
# 수성구,98
# 달서구,107

import csv
from typing import List, Dict

# 중구 : 110 형태의 데이터가 필요하기 때문에 dict 데이터를 사용. key는 문자열, value 는 정수.

new_datas: Dict[str, int] = dict()

with open('./input/아파트(매매)_실거래가_20240304160735.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row: dict
        # print(row)
        if row['단지명'].find('롯데캐슬') >= 0:
            new_key: str = row['시군구'].split(" ")[1]  # 구를 추출
            if new_key in new_datas:  # 구 이름의 키가 있는 경우, 기존 값 1을 더함
                new_datas[new_key] = new_datas[new_key] + 1
            else:  # 구 이름의 키가 없는 경우, 새로 생성 후 1을 입력
                new_datas[new_key] = 1
print(new_datas)
header: list = ['구', '거래건수']

file_name = 'apt_2403_조건3.csv'
with open(f'./output/{file_name}.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for key, value in new_datas.items():
        writer.writerow({header[0]: key, header[1]: value})
        print([key],[value])    # 테스트
print(f'{file_name} 파일이 생성되었습니다.')
