# 연락처.txt를 보면 011 로 시작하는 것들이 있는데 010으로 바꿔바라
# 연락처.txt 파일을 이용하여, 파일에 저장된 연락처 중에서 전화번호가 011로 시작하는 모든 연락처를 010으로 수정하세요.

# 지시사항
# 연락처.txt 파일은 다음과 같은 형식으로 데이터가 저장되어 있습니다.
# "김나라", "목포시", "010-1011-1111"
# "이나라", "서울시", "011-2222-2222"
# "오나라", "전주시", "010-3333-3333"
# "정나라", "속초시", "011-4444-4444"
# "유나라", "제주시", "011-5555-5011"
# ...
# 실행 예
# 총 3건의 011 데이터를 찾았습니다.
# 모든 데이터를 수정했습니다.



data_list_new = []  # 새로운 연락처 저장
# 1. 기존 파일을 읽음
with open('./input/연락처.txt', 'r',encoding='utf-8') as file1: # w로 쓰기모드로 읽어버리면
    # UnsupportedOperation 예외가 발생함.
    #  연락처.txt 파일을 읽기 모드로 열고, 파일의 모든 라인을 data_list 리스트에 저장 한다.
    #  파일의 내용은 변경되지 않습니다.

    data_list = file1.readlines()
    # 라인 단위로 읽은 후 리스트로 반환 ->
    # 라인 단위로 반복문을 사용할 수 있음
    count = 0  # 변경 횟수 저장할 변수
    string_to_find = '"011'  # 중간에 011이 들어간 경우도 있어서 "011로 문자 검색
    for row in data_list:
        # print(row, end='')
        if row.find(string_to_find) >= 0:
            count += 1
            row = row.replace(string_to_find, '"010')  # 문자열 변경
        data_list_new.append(row)
print(f'\n총 {count}건의 011 데이터를 찾았습니다.')
print(data_list_new)

# 2. 변경된 내용을 저장
# 원본 손상을 막기 위해 복사보 ㄴ생성.
# 파이참에서 확인하기 쉽게 utf-8로 인코딩 설정
with open('./output/연락처_복사본.txt','wt',encoding='utf-8') as file:
    for row in data_list_new:
        file.write(row)