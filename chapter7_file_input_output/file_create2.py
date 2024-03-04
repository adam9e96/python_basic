# 1. 텍스트 파일에 문자열 쓰기:
with open('example.txt', 'w') as file:
    num_characters = file.write('Hello, World!')
    print(f'Written {num_characters} characters')
# 출력 : Written 13 characters

# 2. 파일에 여러 줄 추가하기:
with open('example.txt', 'a') as file:
    lines = ['First line\n', 'Second line\n']
    for line in lines:
        file.write(line)
# example.txt 파일 내용
# Hello, World!First line
# Second line

# 3. 바이너리 파일 쓰기
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03')
