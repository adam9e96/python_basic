import csv
from typing import List

new_datas: List[dict] = list()
with open('./input/아파트(매매)_실거래가_20240304160735.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row: dict
        #print(row)
        if row['단지명'].find('래미안') != -1:
            print(f'{["단지명"]}')
            new_data : dict = dict()
            new_data['시군구'] = row['시군구']
            new_data['단지명'] = row['단지명']
            new_data['전용면적(㎡)'] = row['전용면적(㎡)']
            new_data['층'] = row['층']
            new_data['거래금액(만원)'] = row['거래금액(만원)']
            new_datas.append(new_data)
print(new_datas)
header: list = new_datas[0].keys()

file_name = 'apt_2403_조건1.csv'
with open('./output/12345.csv','w',newline='',encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for data in new_datas:
        writer.writerow(data)
print('f{file_name} 파일이 생성되었습니다.')