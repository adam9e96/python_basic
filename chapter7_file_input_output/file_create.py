# 1. 메모장에 순수하게 저장 만 하고 닫기
# 순수하게 변수도 사용하지 않고 '생성'만 할 수도 있기는 하다.
# open('./test123.txt', 'wt').close()
# 메서드 체이닝(method chaining)을 이용
# 해당 코드의 목적 :
# 새로운 텍스트 파일을 생성 하거나, 이미 존재하는 파일이 있을 경우 그 내용을 비우고 새로 생성.
# 파일에 데이터를 쓰지 않고 바로 닫기 떄문에, 빈 파일이 생성됨

# 2. 변수에 저장하여 쓰고 저장 후 닫기
# 과정 : open -> write -> close
# 변수에 저장을 하지 않으니 빈파일을 생성하는 등의 기능 말고는 사용할 수 가 없다.
# open()함수를 사용해 생성한 객체를 변수에 담아 줘야 할 거같다.
f = open('./output/test001.txt','wt',encoding='utf-8')   # f라는 변수에 객체를 저장했다.
# print(f)    # <_io.TextIOWrapper name='./output/test001.txt' mode='wt' encoding='utf-8'>
f.write('Hello World')
f.close() # 닫는것 까지 해야 코드가 완성 된다..

# 이제
# 내가 원하는 경로에 원하는 이름의 메모장으로 원하는 내용을 적는 코드를 완성했다.

# 3. 순수하게 메모장에서 읽기고 출력만 하기
# open('./output/test001.txt', 'r', encoding='utf-8').read())
# 이경우 진짜 순수하게 파일객체를 이용해 읽어서 콘솔로 출력하는 기능 말고는 없다.

# 4. 메모장의 내용물을 변수를 이용해 담아서 출력하고 닫기
# 과정 : open -> read -> close
f = open('./output/test001.txt','r',encoding='utf-8')   # rt가 아닌 이유 : t는 디폴트 값임
# print(f)    # <_io.TextIOWrapper name='./output/test001.txt' mode='r' encoding='utf-8'>
f_read = f. read()
#
f.close()
#
print(f_read)


# # 3. 파일의 생성
file = open('./output/my_file.txt','wt') # 빈 파일 생성
print('my_file.txt 파일이 생성되었습니다.')
file.close()

# # my_file_1.txt부터 my_file_10.txt까지 파일 생성
# for i in range(1, 11):
#     file = open(f'./output/my_file{i}.txt', 'wt')
#     print(f'my_file{i}번 파일이 생성되었습니다.')
# file.close()
#
# # my_file_1.txt부터 my_file_10.txt까지 파일 생성
# for i in range(1, 11):
#     file = open(f'../m/my_file{i}.txt', 'wt')
#     print(f'my_file{i}번 파일이 생성되었습니다.')
# file.close()

fish = open('./output/my_file15.txt', 'wt')  # 빈 파일 생성
print('my_file.txt 파일이 생성되었습니다.')
fish.close()

##
with open('./output/my_file_1.txt', 'wt') as file:
    print('my_file_1.txt 파일이 생성되었습니다.')
# 출력 my_file_1.txt 파일이 생성되었습니다.
