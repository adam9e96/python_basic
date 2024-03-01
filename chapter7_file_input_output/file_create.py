# 3. 파일의 생성
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
