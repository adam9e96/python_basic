name = 'Alice'  # singleline 문자열 저장
age = 25  # 정수를 저장
address = '''우편번호 12345
서울시 영등포구 여의도동
서울빌딩 501호'''  # multiple line 문자열 저장
boyfriend = None  # 아무 값도 저장하지 않음 #자바의 null과 같음
height = 168.5  # 실수를 저장

print(name)
print(age)
print(address)
print(boyfriend)
print(height)

"""
파이썬의 기본 데이터 타입 4 가지 : 정수, 실수, 불, 문자열
파이썬의 컬렉션 데이터 타입 4가지 : list, tuple, set, dict <-- 파이썬에 컬렉션은 기본 데이터 타입처럼 사용함

파이썬은 8가지 데이터 타입만 외우면 된다. 
"""

# 정수 int
# int() 함수를 이용하면 다른 자료형의 값을 정수형 데이터로 변환할 수 있음.
print(int(1.9))      # 1 / 1.9 의 소수점 (.9) 이하를 제거하여 정수 1로 변환
print(int(True))     # 1 / True 는 1로 변환
print(int(False))    # 1 / False 는 0으로 변환
print(int('100'))    # 100 / 문자열 '100' 을 정수 100 으로 변환
print(type(100))     # <class 'int'>

# 10 진수를 2진수, 8진수, 16 진수로 변환 하는 방법
print()
n = 95
print(type(n))  # <class 'int'>
# print(bin(n)) # 0b1011111 | 2진수로 변환
# print(oct(n)) # 0o137     | 8진수로 변환
# print(hex(n)) # 0x5f      | 16진수로 변환


####

# 실수 float
# 소수점이 있는 숫자를 실수 (floating point number) 라고 함

# float() 함수를 이용하면 다른 자료형의 값을 실수형 데이터로 변환 할 수 있음
print(float(1))  # 1.0 / 정수 1을 실수 1.0 으로 변환
print(float(True)) # 1.0 / True 는 1.0 으로 변환
print(float(False)) # 0.0 / False 는 0.0 으로 변환
print(float('3.14')) # 3.14 / 문자열 '3.14' 를 실수 3.14로 변환
print(float('100')) # 100.0 / 문자열 '100' 을 실수 100.0 으로 변환
print((type(3.14))) # <class 'float'>



# 실수의 연산은 부정확
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
# sol)
# 정수를 형변환 후 계산하고 그 값을 실수로 다시 형 변환함

# 논리 bool
# 논리 자료형. 참과 거짓을 의미하는 True 와 False 값을 가질 수 있음
# True 나 False 모두 첫 글자는 반드시 대문자로 작성

# 파이썬에는 False 는 값이 없는 모든 경우를 의미. 숫자0, 빈 문자열'', 빈 리스트[] 등은 모두 False 로 인식한다
print(bool(0)) # False
print(bool('')) # False
print(bool([])) # False
print(bool(1)) # True
print(type(True)) # <class 'bool'>

print(3>4) # False
print(3<4) # True

# bool은 조건문을 사용할 떄 사용한다.

# 문자열 str
# 문자열 자료형. 기본적으로 따옴표로 묶어서 데이터를 표현
# 문자열을 한 글자이거나 여러 글자여도 작은 따옴표(')와 큰 따옴표(")를 모두 사용할 수 있음
# 각 따옴표을 3개씩 사용하는 삼중 땅모표(''' ''', """ """) 도 사용할 수 있음
# single line : 한 줄의 문자열 : 작은 따옴표(')와 큰 따옴표(")
# mulitple line : 여러 줄의 문자열 : 삼중 따옴표(''' ''', """ """)

print()
# 문자열 변환
# str() 함수를 사용하면 다른 자료형의 값을 문자열 데이터로 변환 할 수 있음
print(str(100)) # '100' / 정수 100을 문자열 '100'으로 변환
print(str(True)) # 'True' / 논리 True를 문자열 'True'로 변환
print(str(False)) # 'False' / 논리 False 를 문자열 'False' 로 변환
print(type(str(3.14))) # <class 'str'> '3.14' / 실수 3.14 를 문자열 '3.14' 로 변환

# 문자열 인덱싱 indexing
# 0번 부터 시작
print()
s = 'hello'
print(s[1]) # e
# 마이너스(-)인덱스는 문자열 뒤에서 부터 부여, 마지막 인덱스는 -1이 됨 #0은 사용하고 있으니 -1부터 시작함

print(s[-4]) # e

print(s[1] == s[-4]) # True


# 문자열 슬라이싱 slicing
# 문자열 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용
# s[start:stop:step]
# start : 시작 인덱스를 지정. 생략하면 처음부터 추출
# stop : 종료 인덱스를 지정. 생략하면 끝까지 추출
# step : 인덱스의 증감값, 생략하면 1씩 변화

print()
s = 'banana'
print(s[0:3]) # 0번 시작, 3번째 앞에서 스탐
print(s[0:6:2]) # 0번 시작, 6번째 앞에서 스탑. 2씩 증가
# 파이썬 특징
# 종료 인덱스 앞에서 끝남.
print(s[:6:2]) # bnn
print(s[::]) # banana
print(s[2::2]) # nn

s2 = 'hello world'
print(s2[:])


# 문제
student = '31025'
grade_no = student[0]
class_no = student[1:3]
# stu_no = student[3:] # stu_no = student[-2:] 도 가능
stu_no = student[-2:] # stu_no = student[-2:] 도 가능

print(grade_no, '학년', class_no, '반', stu_no, '번')
# 3 학년 10 반 25 번

# 마이너스 인덱싱도 가능하다.
print(student[-3])

# 문제 2
# 전체 차량번호에서 뒤에 숫자 4자리만 출력하는 프로그램을 구현하세요.
# 전체 차량번호는 '서울2가 1234', '10가 1234', '288가 1234'와 같이 다르지만, 모두 차량번호 4자리는 '1234'입니다.
# 실행 예)
# 서울2가 1234의 차량번호 4자리는 1234입니다.

car1 = '서울2가1234'
car2 = '10가1234'
car3 = '288가1234'

car_no1 = car1[-4:]
car_no2 = car2[-4:]
car_no3 = car3[-4:]
print(car1, '의 차량번호는 4자리는', car_no1, '입니다.')
print(car2, '의 차량번호는 4자리는', car_no2, '입니다.')
print(car3, '의 차량번호는 4자리는', car_no3, '입니다.')

# 리스트 list
# 여러 값을 저장할 때 가장 많이 사용하는 자료형
# 저장 하고자 하는 값들의 자료형(type)이 서로 다르더라도 하나의 리스트에 저장

# 대괄호([]) 또는 list() 함수를 이용해서 생성
# 정수, 실수, 문자열을 각 1개씩 저장하고 잇는 리스트 생성
li = [100, 3.14, 'hello']
print(li) # [100, 3.14, 'hello']
print(type(li)) # <class 'list'> # li의 데이터타입을 알 수 없을때 대괄호에 콤마를 썼다면 일단 리스트임.

# 인덱싱
# 문자열과 동ㅇ리한 방식으로 인덱싱을 지원
# 저장된 요소들마다 고유 번호인 인덱스를 부여하여 순서대로 관리
print()
print(li[0]) # 100
print(li[1]) # 3.14
print(li[2]) # 'hello'

# 슬라이싱
print()
li = [10, 20, 30, 40]
print(li[0:3]) # [10, 20, 30]
print(li[:2]) # [10, 20]
print(li[::2]) # [10, 30]
print(li[-2::]) # [30, 40]