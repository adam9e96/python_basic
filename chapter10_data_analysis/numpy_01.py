
import numpy as np

# 배열 Array 이란 1) 순서가 있는 2) 같은 종류의 데이터가 저장된 집합.
# Numpy 를 이용해 배열을 처리하기 위해서는 우선 NumPy 로 배열을 생성해야 함.

# 다양한 방법으로 배열을 생성하는 방법 보기

# 1) 시퀀스 데이터로부터 배열 생성하기. array()
# 시퀀스 데이터 seq_data 를 인자로 받아 Numpy 의 배열 객체 array object를 생성.
# arr_obj = np.array(seq_data)

# 정수 리스트로 배열 생성
data1 = [0, 1, 2, 3, 4, 5]
print(data1)  # [0, 1, 2, 3, 4, 5]  <-- 리스트

a1 = np.array(data1)
print(a1)  # [0 1 2 3 4 5]  <-- 콤마가 없음. NumPy는. 공백으로 구분함

print(a1.dtype)  # data type 이 int32

# 정수와 실수가 혼합된 경우
# 리스트의 경우 아무 문제가 없는데 넘파이의 경우 하나의 자료형으로 인식해야 하기 때문에 둘 중 하나의 타입으로 변환해야 한다.
data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
print(a2)  # [ 0.1  5.   4.  12.   0.5]

print(a2.dtype)  # float64  정수와 실수가 혼합돼어 있을 때 모두 실수로 변환한다.

# 숫자와 문자가 있는 경우
data3 = [0.1, 5, 4, 12, 'test']
a3 = np.array(data3)
print(a3)  # ['0.1' '5' '4' '12' 'test']

print(a3.dtype)  # <U32  -> 길이가 32인 유니코드 문자열로 변환한다.

# array() 에 직접 리스트를 넣어서 배열 객체도 생성 가능.
a3 = np.array([0.5, 2, 0.01, 8])
print(a3)  # [0.5  2.   0.01 8.  ]
print(a3.dtype)  # float64

# 다차원 배열의 생성 예.
a4 = np.array([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
print(a4)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# 2) 범위를 지정해 배열 생성. arrange()
# arrange() 를 이용해 Numpy 배열을 생성. 파이썬의 range() 와 사용 방법이 비슷.
# arr_obj = np.array([start,] stop[,step])
# start부터 시작해서 stop 전까지 step 만큼 계속 더해 NumPy 배열을 생성.
# start 가 0 인 경우에는 생략 가능.
# step이 1인 경우에는 생략 가능.

a1 = np.arange(0, 10, 2)
print(a1)  # [0 2 4 6 8]

a2 = np.arange(1, 10)
print(a2)  # [1 2 3 4 5 6 7 8 9]

a3 = np.arange(5)
print(a3)  # [0 1 2 3 4]

# 여기까진 range 와 같은데(1차원 배열까지는 거의 같다?)

# NumPy 배열의 arange() 를 이용해 생성한 1차원 배열에 reshape(m, n) 을 추가하면 m * n 형태의 2차원 배열(행렬)로 변경.
# 주의할 점은 arange()로 생성되는 배열의 원소 개수와 reshape(m, n)의 m * n의 개수가 같아야 함.
a4 = np.arange(12).reshape(4, 3)  # 4행 3열 4행*3열 =12 , arange = 12 둘다 동일해야 가능하다
print(a4)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# NumPy 배열의 형태를 알기 위해서는 'ndarra.shape' 를 실행.
print(a4.shape)  # (4,3)

# 1차원 배열의 경우 '(n, )' 처럼 표시.
print(a1.shape)  # (5,)

# np.linspace()
# 범위의 시작과 끝을 지정하고 데이터의 개수를 지정해 배열을 생성.
# arr_obj = np.linspace(start, stop[, num])
# linspace() 는 start 부터 stop 까지 num 개의 배열을 같은 간격으로 생성. num 을 지정하지 않으면 50 이 기본값.

a1 = np.linspace(1, 10, 10)
print(a1)  # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
a2 = np.linspace(1, 10, 4)
print(a2)  # [ 1.  4.  7. 10.]

# 0부터 파이까지 동일한 간격으로 20개를 나눈 배열 생성.
a3 = np.linspace(0, np.pi, 20)
print(a3)
# [0.         0.16534698 0.33069396 0.49604095 0.66138793 0.82673491
#  0.99208189 1.15742887 1.32277585 1.48812284 1.65346982 1.8188168
#  1.98416378 2.14951076 2.31485774 2.48020473 2.64555171 2.81089869
#  2.97624567 3.14159265]
print(np.pi)  # 3.141592653589793

# 3) 특별한 형태의 배열 생성.
# 모든 원소가 0 혹은 1인 다차원 배열을 만들기 위해서는 zeros() 와 ones() 를 이용.

# 원소가 0이고 개수가 10개인 1차원 배열 생성.
a1 = np.zeros(10)
print(a1)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(a1.dtype)  # float64

# 3 * 4 의 2차원 배열을 생성.
a2 = np.zeros((3, 4))
print(a2)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

a3 = np.ones(5)
print(a3)  # [1. 1. 1. 1. 1.]
print(a3.dtype)  # float64

# 4) 배열의 데이터 타입 변환.
# 배열은 숫자뿐만 아니라 문자열도 원소를 가질 수 있음.

# 문자열이 원소인 배열 생성 예
a1 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(a1)  # ['1.5' '0.62' '2' '3.14' '3.141592']

print(a1.dtype)  # <U8

# NumPy 데이터의 형식.
# b : 불. bool
# i : 기호가 있는 정수. (signed) integer
# u : 기호가 없는 정수. unsigned integer
# f : 실수. floating-point
# c : 복소수. complex-floating point
# M : 날짜. datetime
# O : 파이썬 객체. (Python) objects
# S or a : 바이트 문자열. (byte) string
# U : 유니코드. Unicode

# 배열이 문자열(숫자 표시)로 돼어 있다면 연산을 위해서는 문자열을 숫자(정수나 실수)로 변환해야 함.
# 형 변환은 astype()로 가능.
# num_arr = str_arr.astype(dtype)

# 실수가 입력된 문자열을 원소로 갖는 배열을 실수 타입으로 변환하는 예
str_a1 = np.array(['1.567', '0.123', '5.123', '9', '8'])

num_a1 = str_a1.astype(float)
print(num_a1)  # [1.567 0.123 5.123 9.    8.   ]
print(str_a1.dtype)  # <U5
print(num_a1.dtype)  # float64

# 정수를 문자열 원소로 갖는 배열을 정수로 변환하는 예.
str_a2 = np.array(['1', '3', '5', '7', '9'])
num_a2 = str_a2.astype(int)

print(num_a2)  # [1 3 5 7 9]
print(str_a2.dtype)  # <U1
print(num_a2.dtype)  # int32

# 5) 난수 배열의 생성.
# Numpy 에서 난수를 발생시킬 수 있는 다양한 함수가 있음.
# rand() 함수를 이용하여 실수 난수를 요소로 갖는 배열을 생성.
# randint() 함수를 이용하면 정수 난수를 요소로 갖는 배열을 생성.
# rand_num = np.random.rand([d0,d1, ... , dn])
# rand_num = np.random.randint([low,] high [, size])

# rand() 함수는 [0,1) 사이의 실수 난수를 갖는 배열을 생성.
# * [a, b) 의 표현은 값의 범위가 a 이상이고 b 미만 이라는 의미.

# randint() 함수는 [low,high) 사이의 정수 난수를 갖는 배열을 생성.
# size 는 배열의 형태 지정.
# low가 입력하지 않으면 0으로 간주.
# size가 입력하지 않으면 1로 간주.

a1 = np.random.rand(2, 3)  # 2행 3열
print(a1)
# [[0.57990916 0.55837668 0.81518476]
#  [0.681181   0.13706035 0.94941191]]

a2 = np.random.rand()
print(a2)  # 923720085929832 <- 단 하나의 값만 뽑음

a3 = np.random.rand(2, 3, 4)  # 3차원 배열 <- 된다는것만 보셈. 3차원까지는 잘 사용안함
print(a3)
# [[[0.5322846  0.56993197 0.8900606  0.26343003]
#   [0.22479969 0.53165433 0.46174664 0.95116995]
#   [0.13805994 0.55327013 0.67772248 0.24138498]]
#
#  [[0.30346752 0.65417356 0.04857577 0.24004361]
#   [0.91189346 0.7484844  0.50599378 0.63969585]
#   [0.48294087 0.1653     0.73069005 0.30250692]]]

a4 = np.random.randint(10, size=(3, 4)) # 3행 4열의 배열이 나온다 <- size는 튜플형태로 줘야함.
    # 0에서 9까지의 정수 난수를 요소로 가지는 3 * 4 배열을 생성.
print(a4)
# [[0 9 1 6]
#  [9 7 2 3]
#  [3 0 2 5]]

a5 = np.random.randint(1,30)
print(a5)   # 7

a6 = np.random.randint(1,30,3)
print(a6)   # [8 7 9]