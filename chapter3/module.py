# function_01에서 넘어옴
# 1. 모듈이란
# 모듈(module)이란 한마디로 파이썬 파일(.py)
# 언제든지 사용할 수 있도록 변수나 함수 또는 크래스를 모아 놓은 파일

# 2. 모듈 생성
# converter.py 생성

# 3. 모듈의  사용
# 반드시 같은 디렉토리에 있어야 함
# 모듈에 저장된 함수를 사용하는 방법
# 1. 모듈 전체를 가져오는 방법
# 모듈에 저장된 '모든' 클래스나 함수를 사용하고자 할 때
# 예) import 모듈

import converter

miles = converter.kilometer_to_miles(150)  # 모듈.함수() 형식으로 호출
print(f'150km={miles}miles')  # 출력 : 150km=93.20565miles

pounds = converter.gram_to_pounds(1000)
print(f'1000g={pounds}pounds')  # 출력 : 1000g=2.20462pounds

# 2. 모듈에 포함된 함수 중에서 특정 함수만 골라서 가져오는 방법
# 예 ) from 모듈 import 함수
# 예 ) from 모듈 import 함수1, 함수2
# 예 ) from 모듈 import *

print()
from converter import kilometer_to_miles  # 모듈은 가져오지 않고 특정 함수만 가져옴

miles = kilometer_to_miles(150)  # 모듈명을 명시하지 않고 사용
print(f'150km={miles}')  # 출력 : 150km=93.20565

print()
from converter import *  # 모듈은 가져오지 않고 모듈의 모든 함수 가져옴

miles = kilometer_to_miles(150)  # 모듈명을 명시하지 않고 사용
print(f'150km={miles}')

pounds = gram_to_pounds(1000)  # 모듈명을 명시하지 않고 사용
print(f'1000g={pounds}pounds')

# 4. 별명 사용하기
# 모듈이나 함수를 import 하는 경우에 원래 이름 대신 별명 alias 를 지정하고 사용
# 모듈이나 함수의 이름이 긴 경우에 주로 짧은 별명을 지정하고 긴 본래 이름 대신 사용
# 별명을 지정할 때는 as 키워드를 사용
print()

import converter as cvt  # converter 모듈에 cvt 라는 별명을 지정

miles = cvt.kilometer_to_miles(150)  # 별명을 이용해서 함수 사용
print(f'150km={miles}miles')

pounds = cvt.gram_to_pounds(1000)
print(f'1000g={pounds}pounds')

print()
from converter import kilometer_to_miles as k_to_m  # 함수에도 별명을 지정 가능

miles = k_to_m(150)  # 함수 이름 대신 별명을 사용
print(f'150km={miles}miles')

##################################
# 표준 모듈

import math  # import 후 사용

# 1) 원주율 pi
# 더 정확한 파이 값을 사용하기 위해
print(math.pi)  # 출력 : 3.141592653589793

# 2) ceil() 함수와 floor() 함수
# 전달된 값을 정수로 올림 처리하거나 내림 처리
print(math.ceil(1.1))  # 출력 :  2 / 정수로 올림 처리
print(math.floor(1.9))  # 출력 : 1 / 정수로 내림 처리

# 3) trunc() 함수
# 전달된 값을 정수로 절사
# 양수를 처리할 때는 차이가 없지만, 음수를 처리할 때는 결과의 차이가 있슴
print(math.trunc(-1.9))  # -1 / 절사이므로 소수점 이하를 잘라버림
print(math.floor(-1.9))  # -2 / 내림이므로 -1.9 보다 작은 정수로 내림

# 4) sqrt() 함수
# 제곱근 구함
print()
print(math.sqrt(25))  # 5.0 / 루트 25를 의미

# 5) pow() 함수
# 제곱을 구함
print()
print(math.pow(2, 3))  # 8.0 / 2의 3제곱을 의미

# 2. random 모듈
# 난수 random number 를  생성하는 모듈
# 난수를 통해서 간단한 게이믕ㄹ 제작할 수 있고 확률 처리도 할 수 있음.

import random

# 1) randint() 함수
# 전달하는 두 인수 사이의 정수를 임의로 생성
print()
print(random.randint(1, 10))  # 6  1 이상 10 이하의 정수

# 2) randrange () 함수
# range() 함수와 사용 방법이 비슷
# range() 함수는 특정범위의 정숫값들이 모두 생성할 수 잇지만,
# randrange() 함수는 그 특정 범위에 속한 정수중 하나만 임의로 생성
print()
print(random.randrange(10))  # 0이상 10 미만의 정수 # 출력 : 3 or 0 등 10미만
print(random.randrange(1, 10))  # 0이상 10 미만의 정수 # 출력 : 8
print(random.randrange(1, 10, 2))  # 0이상 10 미만의 홀수 # 출력 : 5

# 3) random() 함수
# 0 이상 1미만 범위에서 임의의 실수를 생성
# 0이상 1미만 범위를 백분율로 환산하면 0%이상 100% 미만이기 때문에 확률을 처리할 때도 사용
print()
print(random.random())  # 출력 : 0.897451762390277

# 50% 확률로 '안녕하세요' 출력
if random.random() < 0.5:
    print('안녕하세요')

rand = random.randint(1, 2)
print(rand)
if rand == 1:
    print('안녕하세요')

# 4) choice() 함수
# 전달된 시퀀스 자료형에 속한 요소 중에서 하나를 임의로 반환
print()
seasons = ['Spring', 'Summer', 'fall','winter']
print(random.choice(seasons))   # 출력 : fall

idx = random.randint(0, len(seasons) - 1)
print(seasons[idx]) # 출력 : summer

# 5) sample() 함수
# 전달된 시퀀스 자료형에 속한 요소 중 지정된 개수의 요소를 임의로 반환
# 반환 결과는 리스트 list 자료형이며 중복없이 임의의 요소가 선택
print()
print(random.sample(range(1, 46), 6))  # [36, 4, 14, 35, 12, 16] e,g) 로또

seasons = ['spring', 'summer', 'fall', 'winter']
print(random.sample(seasons, 3))
seasons = ['summer', 'summer', 'summer', 'winter']
print(random.sample(seasons, 3))

# 6) shuffle() 함수
# 전달된 시퀀스 자료형에 속한 요소의 순서를 임의로 조정하여 다시 재배치하는 함수
# 호출하면 실제 전달된 시퀀스 자료형의 순서가 재배치
print()
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)  # 출력 : [1, 4, 2, 5, 3]

