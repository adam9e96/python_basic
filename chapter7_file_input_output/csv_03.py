import csv

example_file = open('./input/아파트(매매)_실거래가_20240304160735.csv')
reader = csv.DictReader(example_file)
# for row in example_reader:
#     print(f'{row}')
# print('='*20)
find_str = "래미안"
new_datas = []
for row in reader:
    result = row["단지명"]
    # print(f'{result}') # 테스트
    # print(result)
    index = result.find(find_str)
    if index != -1: # 못찾으면 -1 임
        # print(f'{row["시군구"]},{row["단지명"]},{row["전용면적(㎡)"]},{row["층"]},{row["거래금액(만원)"]}')
        new_data:dict = dict()
        new_data["시군구"] = row["시군구"]
        new_data["단지명"] = row["단지명"]
        new_data["전용면적(㎡)"] = row["전용면적(㎡)"]
        new_data["층"] = row["층"]
        new_data["거래금액(만원)"] = row["거래금액(만원)"]
        new_datas.append(new_data)

print(new_datas)
header:list = list(new_datas[0].keys())
    # ['시군구','단지명','전용면적(㎡)','층','거래금액(만원)']
file_name = 'daegu_hraemian3.csv'
with open('./output/daegu_hraemian3.csv','w',newline='',encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=header)
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)
print(f'{file_name}파일이 생성 되었습니다.')

# 조건 : 래미안 단지만 검색
# 출력조건 : 시군구 단지명, 전용면적, 층, 거래금액
# 저장 파일명 : apt_2403_조건1.csv
# with로 파일처리

import csv

# 조건 : 롯데캐슬 거래건만 검색
# 출력조건: 구(구만 나오도록 할 것), 단지명, 전용면적, 층, 거래금액
# 저장 파일명: apt_2403_조건2.csv
# with로 파일 처리
# 예) 달서고, 롯데캐슬레이크,84.91,3,"32.100"