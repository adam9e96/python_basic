# 파일 출력 output

# 1. 텍스트 파일 생성하기
file = open('./output/hello.txt', 'wt')

# hello.txt에 글 쓰기.
file.write('안녕하세요.1')
file.write('\n')  # 줄 바꿈
file.write('반갑습니다.')
file.write('\n')  # 줄 바꿈
print('hello.txt 파일이 생성되었습니다.')
# 진행 상황을 알기 위해서 화면 출력.

file.close()

# 2. 텍스트 파일에 내용 추가하기
# 기존 파일에 내용을 추가할 수 있는 모드는 a 모드
file = open('./output/hello.txt', 'at')

file.write('Hello.\n')
file.write('Nice to meet you. \n')
print('hello.txt 파일에 새로운 내용이 생성되었습니다.')
file.close()

# utf-8로 문서 작성하기 (인코딩을 ansi -> utf-8)
# import codecs
# file = codecs.open('./output/한글파일.txt','w','utf-8')
# file.write("오늘 나는 학교에 갔습니다.")
# file.close()

file = open('./output/한글파일.txt','w',encoding='utf-8')
file.write("오늘 나는 학교에 갔습니다.")
file.close()
# 파이썬 버전업으로 인해 import 할 필요가 없어짐. open에서도 eoncoding 지원함


###
# 파일 입력 input
# 1. 텍스트 파일 읽기
file = open('./output/hello.txt','rt')

str = file.read()   # 파일 전체를 한 번에 읽어 들임
print(str,end='')
file.close()
# 출력
# 안녕하세요.
# 반갑습니다.
# Hello.
# Nice to meet you.

print()
file = open('./output/hello.txt','rt')

while True:
    str = file.readline()
    if str == '':
        break
    print(str,end='')
file.close()


# 3) readlines() 메소드
# 라인 line 하나가 아니라 전체 라인 lines을 모두 읽어 각 라인 line 단위로 리스트에 저장하는 메소드
print()
file = open('input/hello.txt', 'rt')

line_list = file.readlines()
print(line_list) # ['안녕하세요.\n', '반갑습니다.\n', 'Hello.\n', 'Nice to meet you.\n']
for line in line_list:
    print(line, end='')

file.close()

# enumrate() 함수를 이용하면 라인 번호 line number 도 함께 출력할 수 있슴
print()
file = open('input/hello.txt', 'rt')

line_list = file.readlines()
for no, line in enumerate(line_list):
    print('{} {}'.format(no + 1, line), end='')

file.close()

# sys 모듈을 이용하면 보다 쉽게 파일을 읽을 수 있슴
# sys 모듈에는 표준 입출력을 위한 stdin과 stdout 객체가 포함
# stdout은 출력을 위한 객체이며 화면 출력 메소드인 write()와 writelines() 메소드를 사용할 수 있슴
# writelines() 메소드를 사용하면 리스트와 같은 반복 가능한 객체의 각 요소를 한 줄씩 자동으로 출력
print()
import sys

file = open('input/hello.txt', 'rt')

line_list = file.readlines()
sys.stdout.writelines(line_list)

file.close()

