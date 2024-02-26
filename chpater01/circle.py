"""
1. 파일명 : circle.py
2. 개요: 반지름을 전달하면 원의 넓이를 반환하는 get_area() 함수를 정의하고
사용하는 예시
3 작성자 : 홍길동
4. 작성일: 2022-08-25
"""
# 삼중 큰 따옴표(""")는 여러 줄의 주석을 만들 떄 사용

# math 모듈 포함 : # 은 한 줄 주석을 만들 때 사용
import math # 원의 넓이를 계산하기 위해 필요한 수학적 연산을 제공하는
# 파이썬 내장 `math` 모듈을 포함시킨다는 의미.
# math 모듈은 `pi` 상수와 `pow()` 함수를 포함하고 있다.


# get_area() 함수 정의
# 이 함수는 반지를을 입력으로 받아 원의 넓이를 계산하고 반환한다.
def get_area(radius):  # 파이썬은 표기법으로 카멜법 보다는 언더바법을 선호.
    """ 반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수 """
    """ 파이썬은 기본적으로 반환형을 지정하지 않아도 된다. """
    area = math.pi * math.pow(radius, 2)
    return area
# 여기서 math.pi 는 원주율 파이의 값
# math.pow(radius,2)는 반지를 제곱을 의미한다.
# 파이썬에서는 함수의 반환 타입을 명시적으로 지정하지 않아도 된다.

## 함수의 반환 값은 실행 시점에 결정된다. (런타임 시점)


# 1) 클래스 안에 있는 메서드와 다르게 독립적으로 함수를 사용할 수 있음.
# 2) 표기법은 언더바 법을 사용
# 3) 데이터타입이 없음

radius = 1.5 # 반지름을 1.5로 설정
# get_area() 함수 호출 결과를 area 변수에 저장
area_result = get_area(radius)   # 
print(area_result)
print(get_area.__doc__)  # get_area 의 Docstring 확인
# 함수에 커서를 대면
# def get_area(radius: Any) -> float #여기서 float는 타입 추론임.
# 반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수 : __doc__ 를 보여줌

asdf = 1.6
print(asdf)
