numbers = [0, 1, 2, 3, 4, 5]
sub_numbers = numbers[1:3]
print(sub_numbers)  # [1, 2]

squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 리스트 연결
# 리스트 연결(Concatenation)과 반복(Repetition)
# : `+` 연산자로 리스트를 연결하거나 `*` 연산자로 리스트를 반복할 수 있습니다.
list1 = [1, 2, 3]
list2 = [4, 5, 6]


# 3. 리스트 연결
combined_list = list1 + list2
print(combined_list)  # [1, 2, 3, 4, 5, 6]
# 리스트 반복
repeated_list = list1 * 3
print(repeated_list)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] # list1 요소를 3번 반복.

# 4. 리스트 정렬(Sorting)
# `sort()` 메소드로 리스트를 정렬합니다.
# `sorted()` 함수를 사용해도 되지만, 이는 새로운 리스트를 생성한다.

random_numbers = [5, 1, 4, 3, 2]
random_numbers.sort() # 리스트 정렬
print(random_numbers)  # [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
# 슬라이싱을 이용한 또 다른 방법
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])  # [5, 4, 3, 2, 1]

animals = ['dog', 'cat', 'bird', 'fish']
index_of_cat = animals.index('cat')
print(index_of_cat)  # 1

letters = ['a', 'b', 'c', 'a', 'b', 'a']
count_of_a = letters.count('a')
print(count_of_a)
