# pickle
# -> 텍스트가 아닌 자료형 (리스트나 딕셔너리 자료형등)을 저장하기 위한 방식
# import pickle을 통하여 모듈 임포트가 필요.
# pickle로 데이터를 저장하거나 불러올때는 파일의 바이너리 형식으로 읽거나 써야함 (wb, rb)
# 모든 파이썬 데이터 객체를 저장하고 읽을 수 있음.
import pickle

data = {
    'a': [1, 2.0, 3, 4 + 6],
    'b': ("character string", "byte string"),
    'c': {None, True, False}
}
print(type(data))  # <class 'dict'>

# 1. 일반 텍스트 파일 형식을 사용하는 경우.
# 저장
with open('./output/data.txt', 'w') as file:
    # file.write(data) # TypeError: write() argument must be str, not dict
    file.write(str(data))  # write() 메서드의 인자는 문자열이어야 함.

# 읽기
with open('./output/data.txt', 'r') as file:
    data_output = file.read()
print(data_output)  # {'a': [1, 2.0, 3, 10], 'b': ('character string', 'byte string'), 'c': {False, True, None}}

print(type(data_output))  # <class 'str'>

# 2. pickle 방식을 사용하는 경우
# 저장
with open('./output/data.pickle', 'wb') as file:
    pickle.dump(data, file)

# 읽기
with open('./output/data.pickle', 'rb') as file:
    data_output = pickle.load(file)  # 읽음.

print(data_output)  # {'a': [1, 2.0, 3, 10], 'b': ('character string', 'byte string'), 'c': {False, True, None}}

print(type(data_output))  # <class 'dict'>

print(data_output.get('a'))  # [1, 2.0, 3, 10]
