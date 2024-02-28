"""
1. 자동으로 실행되는 로또 추첨 프로그램을 다음 지시사항에 따라 구현하세요.

지시사항
1. 1에서 45 사이의 모든 정수를 순서대로 pot 리스트에 저장합니다.
2. 다음 과정을 6번 반복합니다.
 * pot 리스트를 무작위로 섞어줍니다.
 * pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장합니다.
 * 2초 동안 잠시 멈춥니다.
3. jackpot 리스트의 모든 요소를 오름차순 정렬합니다.
4. jackpot 리스트의 모든 요소를 출력합니다.

실행 예)
1번째 당첨번호는 4입니다.
2번째 당첨번호는 34입니다.
3번째 당첨번호는 13입니다.
4번째 당첨번호는 36입니다.
5번째 당첨번호는 44입니다.
6번째 당첨번호는 31입니다.
이번 당첨번호는 [4, 13, 31, 34, 36, 44] 입니다.

2. 다음 지시사항에 따라 UpDown게임을 구현하세요.

지시사항
1. 1에서 100 사이의 정수 중 하나를 임의로 생성하면
사용자는 그 숫자를 맞힐 때까지 값을 예상하여 입력합니다.
2. 사용자가 입력한 값이 정답보다 작으면 Up, 정답보다 크면 Down을 출력합니다.
3. 정답을 맞히면 몇 초 만에 정답을 맞혔는지 출력하세요.
이때 소수 아래 값은 내림 처리하여 정수로 출력하세요.

실행 예)
UpDown게임을 시작합니다.
어떤 값일까요? >>> 30
Up
어떤 값일까요? >>> 70
Down
어떤 값일까요? >>> 60
Down
어떤 값일까요? >>> 50
Up
어떤 값일까요? >>> 55
Up
어떤 값일까요? >>> 56
Up
어떤 값일까요? >>> 57
Up
어떤 값일까요? >>> 58
58! 정답입니다.
34초 만에 성공했습니다.
"""
import math
import random
import time

#  1번

pot = list((range(1, 46)))
# print(pot)
# pot.append(random.sample(range(1, 46), 6))
# print(random.sample(range(1, 46), 6))  # [36, 4, 14, 35, 12, 16] e,g) 로또
# print(pot)

jackpot = list(pot)
for i in range(0, 6):
    random.shuffle(pot)
    # print(pot) # test
# print(pot)

pot.pop()
# jackpot = pot.pop()
print(jackpot)
time.sleep(2)
jackpot.sort()
print(jackpot)

number = list()
for i in range(6):
    number.append(random.choice(jackpot))
    # print(random.choice(seasons))  # 출력 : fall
    print(f'{i + 1}번째 당첨번호는 {number[i]}입니다.')

print(f'이번 당첨번호는 {number} 입니다.')

# 2번.
randomNumber = random.randint(1, 100)
print(randomNumber)  # 출력 : 39

### 1번 답
pot = list(range(1, 46))  # 1에서 45 사이의 모든 정수를 순서대로 pot 리스트에 저장
jackpot = list()
for n in range(0, 6):  # 6번 반복
    random.shuffle(pot)  # pot 리스트를 무작위로 섞어줌
    # pot 리스트의 마지막 숫자를 하나만 빼서 jackpot 리스트에 저장
    jackpot_num = pot.pop()
    jackpot.append(jackpot_num)
    time.sleep(2)
    print(f'{n + 1}번째 당첨번호는 {jackpot_num}입니다.')
jackpot.sort()
print(f'이번 당첨번호는 {jackpot}입니다.')

## 2번 답
num = random.randint(1, 100)  # 1에서 100 사이의 정수 중 하나를 임의로 생성
print('UpDown 게임을 시작합니다.')
print(num)
start = time.time()  # 시작시간
while True:
    answer = int(input('어떤 값일까요? >>> '))
    if answer == num:  # 정답을 맞춘 경우
        print(f'{num}! 정답입니다.')
        break
    if answer > num:
        print(f'Down')
    else:
        print(f'Up')
end = time.time()  # 종료시간
print(f'{math.floor(end - start)}초 만에 성공했습니다.')
