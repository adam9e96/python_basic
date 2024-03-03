# 변수는 프로그램을 실행할때 데이터를 저장하기 좋은 방법.
# 그러나 프로그램을 종료한 후에도 데이터를 유지하고 싶다면, 파일 형태로 저장해야 함.
import os
# 1. 파일과 파일 경로
# 파일에는 `파일 이름`과 `경로`라는 두 가지 주요 속성이 있음.

# 예를 들어 윈도우 운영체제를 사용하는 노트북 컴퓨터의
# C:\Users\al\Documents 라는 경로에 project.docx 라는 이름의 파일이 있는 경우
# 파일이름 project.docx 는 워드 문서이고 Users, al, Documents는 모두 폴더(디렉토리) 라고 함.

# 경로의 C:\는 루트 폴더를 나타내며 모든 폴더가 이 안에 들어 있음.
# 윈도우에서 루트 폴더의 이름은 "C:\" 이며, C 드라이브라고 부름.
# 맥OS나 리눅스에서 루트 폴더는 "/" 임.
# 윈도우, 맥 OS에서는 폴더 이름이나 파일이름의 대소문자를 구분하지 않지만,
# 리눅스의 경우 이를 구분함.

# 윈도우에서의 폴더 구분은 "\" 백슬러시를 사용하고, 맥OS 나 리눅스에서는 "/" 슬러시를 사용함.
# 프로그램이 모든 운영체제에서 작동하게 할려면, "\", "/" 두 가지 경우 모두 처리하도록 스크립트를 작성하는 것도 가능.
# 1) Path 객체 사용.
from pathlib import Path
path = Path('spam','bacon','eggs') # 운영체제에 맞는 경로 객체를 만들어 줌.
print(path) # 출력 : spam\bacon\eggs

# 2) platform.system() 함수 사용.
import platform
my_os = platform.system()

print("OS in my system : ", my_os)  # windows
if my_os == 'Windows':
    print('Windows 운영체제입니다.')
else:
    print('Windows 운영체제가 아닙니다.')

# 현재 작업 디렉토리
print(Path.cwd())   # C:\dev\projects\PythonBasic\chapter7_file_input_output

# 절대 경로와 상대 경로
# 절대 경로 : 항상 루트 폴더에서 시작하는 경로
# 상대 경로 : 현재 작업 디렉토리에 대한 경로

# '.' : 현재 디렉토리
# '..' : 상위 디렉토리

# 새로운 디렉토리 만들기
# os.makedirs() 함수로 새로운 디렉토리를 만들 수 있음.
# os.path.isdir(path) : path 인자의 디렉토리가 있는지 확인.
import os
path = './test123'
if not os.path.isdir(path):
    os.makedirs(path)   # 현재 작업 폴더안에 test123 라는 폴더 생성.

# 파일 크기와 폴더 내용 확인하기
# os.path.getsize(path) : path 인자에 해당하는 파일 크기를 바이트 단위로 반환.
# os.listdir(path) : path 에 있는 파일 이름 리스트를 반환

path = './input'
print(os.path.getsize(f'{path}/hello.txt')) # 61 바이트
list_dirs = os.listdir(path)    # 해당 경로에 있는 파일 이름 리스트를 반환
print(list_dirs)    # ['hello.txt', '엄마돼지아기돼지.txt', '연락처.txt']

path = 'C:/'
print(os.listdir(path))