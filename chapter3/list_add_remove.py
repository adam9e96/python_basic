
# 요소의 추가와 삭제

## 요소의 추가
# 새로운 요소를 추가할 때는 append() 와 insert() 메소드를 사용
# append() : 항상 마지막 요소로 추가
# insert() : 추가할 인덱스(위치 정보)를 지정
print()
scores = [50, 40, 30]  # 대괄호로 감싸고 콤마로 구분하면 list임
scores.append(100)  # 마지막 요소에 100을 추가
print(scores)  # [50,40,30,100]
print(scores[1])  # 40
scores.insert(0, 90)  # 인덱스 0에 90을 추가
print(scores)  # [90, 50, 40, 30, 100]
print(scores[1])  # 50


## 삭제
# pop() : 인덱스를 전달하지 않으면 마지막 요소를 삭제,
# 인덱스를 전달하면 전달된 인덱스의 요소를 삭제
scores.pop()  # 마지막 요소를 제거
print(scores)  # [90, 50, 40, 30]
scores.pop(0)
print(scores)  # [50, 40, 30]


