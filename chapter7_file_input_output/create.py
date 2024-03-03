# with(open('./output/연습용1.txt', 'w')) as file2:
#     file2.write('Hello World2\n')
#     print('성공')
#
# with(open('./output/연습용1.txt','at')) as file2:
#     file2.write('abc')
#     print('성공2')

file = open('./output/연습용1.txt','r')

sd = file.read()
print(sd)

file = open('./output/연습용1.txt','r')
print('1')
scd = file.readlines()
print(scd,end='')