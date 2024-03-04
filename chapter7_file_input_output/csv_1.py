# student_list = []
# with open('./input/CSV/학생명단.csv', 'rt', encoding='utf-8') as file:
#     file.readline()  # 학번,이름,주소,연락처
#     # print(file.readline())
#     while True:
#         line = file.readline()
#         if not line:  # 더 이상 읽을 내용이 없으면 반복문을 빠져 나옴.
#             break
#         # print(line)
#         student = line.split(',')
#         # print(student)
#         student_list.append(student)
# print(student_list)


# CSV 파일을 사용하다 보면 간혹 큰 따옴표(")를 이용해서 텍스트를 묶는 경우가 있음
# 큰 따옴표를 제거하기 위해서 회원명에 추가로 strip() 메소드를 사용
# member_list = []
# with open('./input/CSV/회원명단.csv', 'rt') as file2:
#     data_list = file2.readline()
#     while True:
#         line = file2.readline()
#         if not line:  # 더 이상 읽을 내용이 없으면 반복문을 빠져 나옴.
#             break
#         member = line.split(',')
#         member[0] = member[0].strip('"')  # 큰 따옴표를 제거
#         member_list.append(member)
# print(member_list)
#
# member[0] 에는 큰 따옴표가 포함된 회원명이 저장되어 있기 떄문에 member[0].strip('"') 으로
# 큰 따옴표를 제거


# 3. csv 모듈로 CSV 파일 생성하기
# import csv 를 통해서 csv 파일을 쉽게 처리할 수 있는 csv 모듈을 사용

# import csv
#
# # w모드로 열고 생성된 파일 객체를 csv.writer() 메소드에 전달
# # 그러면 CSV 파일을 생성할 수 있는 객체가 생성되는데 이 객체를 이용해서
# # writerow() 메소드를 호출하면 CSV 파일에 데이터를 저장할 수 있음
#
# with open('./output/차량관리_03.csv', 'w', newline='') as file:
#     # delimiter=',': ,콤마로 데이터 구분. tab을 사용하는 경우도 있음.tsv.
#     csv_maker = csv.writer(file, delimiter=',')
#     print(csv_maker)
#     csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
#     csv_maker.writerow([2, '25다1234', '2020-10-20,14:10'])
#     csv_maker.writerow([3, '28하1234', '2020-10-20,14:20'])
# print('차량관리_03.csv 파일이 생성되었습니다.')

# 4. csv 모듈로 CSV 파일 읽기
# import csv
# # CSV 파일을 읽기 위해서는 r모드로 파일을 열고 생성된 파일 객체를 csv.reader() 메소드에 전달
# # csv.reader() 메소드로 CSV 파일을 읽고 그 내용을 저장한 객체 iterator 를 반환
# with open('./output/차량관리_03.csv', 'r', newline='') as file:
#     csv_reader = csv.reader(file, delimiter=',', quotechar='"')
#     for line in csv_reader:
#         print(line)



# 1 . reader 객체
# csv 모듈은 별도의 설치없이 사용가능.
# import csv
#
# # csv 모듈을 사용해서 csv 파일을 읽으려면 다른 텍스트 파일처럼 open() 함수로 파일을 열어야 함.
# example_file = open('./input/CSV/example.csv')  # mode를 생략하면 rt가 기본값
#
# # print(example_file)  # <_io.TextIOWrapper name='./input/CSV/example.csv' mode='r' encoding='cp949'>
#
# # read() 대신 csv.reader() 함수에 전달. reader() 객체가 반환.
# example_file = csv.reader(example_file)
# # print(example_file)  # <_csv.reader object at 0x000001D3F74FAE00>
# # print(list(example_file))
#
# # # list 로 변환하여 값에 전급
# example_data = list(example_file)
# # example_data1 = dict(example_file) # dict 은 안됨
#
# print(example_data)
# print(example_data[0][1])  # Apples


# import csv
# # 2. for 반복문을 활용해 reader 객체로부터 데이터 읽기
# # CSV 파일이 큰 경우에는 , 전체 파일을 한 번에 메모리에 로드하지 않고
# # for 반복문에서 reader 객체 사용.
# # reader 객체는 한 번만 사용가능하기 때문에 다시 사용하려면 새로 reader 객체 생성.
# example_file = open('./input/CSV/example.csv')
# example_reader = csv.reader(example_file)
# # print(example_reader)
# print('example.csv 출력')
#
# for row in example_reader:
#     # 각 행의 번호를 얻으려면 reader 객체의 line_num 변수를 사용.
#     print(f'Row #{str(example_reader.line_num)} {str(row)} {str(row[0])}')
# example_file.close()
# print('=' * 20)

# 3. writer 객체
# writer 객체를 사용하면 데이터를 csv 파일에 저장할 수 있음

# import csv
# output_file = open('./output/output.csv', 'w', newline='')  # newline='' : 빈줄이 들어가는 것을 방지.
# output_writer = csv.writer(output_file)  # csv.writer에 전달할 객체 생성.
# output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])  # writer.writerow(): 리스트에 인자를 전달.
# output_writer.writerow(['hello', 'world!', 'eggs', 'bacon', 'ham'])
# output_writer.writerow([1, 2, 3, 3.141592, 4])
# output_file.close()

# # 4. 키워드 인자 delimiter 와 lineterminator
# # 쉼표가 아닌 탭문자로 셀을 구분하고 줄 간격을 한 줄씩 띄우려는 상황을 가정.
# # 구분자 (delimiter) 와 줄 끝 문자 (lineterminator)를 변경.
# # delimiter의 기본값은 쉼표이고, lineterminator의 기값은 개행문자.
# # 셀들이 탭으로 구분되어 있기 때문에 탭으로 구분된 값을 의미하는 .tsv 파일 확장자 사용.
# import csv
# csv_file = open('./output/example.tsv', 'w', newline='')
# csv_writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n\n')
# csv_writer.writerow(['apples','oranges','grapes'])
# csv_writer.writerow(['eggs','bacon','ham'])
# csv_writer.writerow(['spam','spam','spam','spam','spam','spam'])
# csv_file.close()
# print('5. CSV 객체의 DictReader 와 DictWriter')
# import csv
# # 5. CSV 객체의 DictReader 와 DictWriter
# # 헤더 행이 있는 csv 파일의 경우 reader 나 writer 객체보다 DictReader 나 DictWriter 객체를 사용하는 것이 작업하기 편함.
# example_file = open('./input/CSV/example_with_header.csv')
# example_dict_reader = csv.DictReader(example_file)
#
# # DictReader 객체는 1) row를 딕셔너리 객체로 설정하고, 2) 첫 번째 행에 있는 정보를 건너 뜀.
# # 3) 첫 번째 행에 있는 정보를 키  값으로 사용
#
# print('example_with_header.csv 출력')
# for row in example_dict_reader:
#     print(f'{row["Timestamp"]}, {row["Fruit"]}, {row["Quantity"]}')
# print('=' * 20 )

# import csv
# # 헤더 정보가 없는 파일의 경우 DictReader() 생성자의 두 번째 인자로 헤더 이름을 지어서 전달.
# example_file = open('./input/CSV/example.csv')
# example_dict_reader = csv.DictReader(example_file,['time','name','amount'])
# print('example.csv 출력')
# for row in example_dict_reader:
#     print(f'{row["time"]}, {row["name"]},{row["amount"] } ')
# print('=' * 20)

import csv
# DictWriter 객체는 csv 파일을 생성하기 위해 딕셔너리를 사용.
output_file = open('./output/output_with_header2.csv','w',newline='')
output_dict_writer = csv.DictWriter(output_file,['Name','Pet','Phone'])
# 파일에 헤더 행을 넣고 싶으면 writeheader() 를 호출

output_dict_writer.writeheader()

# writerow() 메서드를 호출하여 각 행을 쓸 수 있는데, 이 떄 딕셔너리를 사용.
# 딕셔너리의 키는 헤더이고, 딕셔너리의 값은 파일에 쓰려는 데이터가 들어감.
output_dict_writer.writerow({'Name':'Alice','Pet':'cat','Phone':'555-1234'})
output_dict_writer.writerow({'Name':'Bob','Phone':'555-9999'})  # 누락된 키는 빈 상태로 나옴.
output_dict_writer.writerow({'Phone':'555-5555','Name':'Carol','Pet':'dog'})    # 순서는 중요하지 않음
output_dict_writer.writerow({'Phone':'555-5555','Name':'Carol','Pet':'dog'})    # 순서는 중요하지 않음
output_file.close()
