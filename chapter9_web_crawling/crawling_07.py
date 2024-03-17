import requests
from bs4 import BeautifulSoup as bs  # <--은 지금 안씀 html 파싱을 안함
import os.path

from bs4 import BeautifulSoup

# 이미지 가져오기
# 파이썬 공식 홈페이지에서 이미지 링크 가져옴

url = 'https://www.python.org/static/img/python-logo@2x.png'
response = requests.get(url)

# 1. 파일 이름 가지고 오기
image_file_name = os.path.basename(url)  # 파일 이름 가져오기
print(image_file_name)  # python-logo@2x.png
# print(dir(os.path))

# 2. 파일 저장 (경로는 output_image) . url만 알면 response.content 를 쓰면 된다.
with open(f'./output_image/{image_file_name}', 'wb') as image_file:  # 여기서 특이한점은 'wb'
    image_file.write(response.content)
    print('이미지 파일로 저장하였습니다.')

# 2. 할리스커피에서 태그를 이용해서 이미지 저장
url = 'https://www.hollys.co.kr/menu/espresso.do'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())  # 나오긴 잘나옴

# 1. 커피이미지 태그 가져오기
image_tag = soup.select_one('#menuView1_877 > img')  # id
# image_tag2 = soup.select_one('.menu_view01 > img')  # class
print('HTML 요소:', image_tag.get("src"))
# print(f'HTML 요소: {image_tag2.get("src")}')
# //admin.hollys.co.kr/upload/menu/etc/menuEtc_202308310540309360.png

# https://admin.hollys.co.kr/upload/menu/etc/menuEtc_202308310540309360.png
# 2. 이미지 경로 가져오기
img_source = image_tag.get('src')
# img_source = image_tag.attrs['src'] # 둘다 됨
print('이미지 파일 경로: ', img_source)  # 원래는 안나와야 되는데 https 프로토콜을 알아서 붙여줘서 출력은 됨

# http
# https

# 3. 이미지 저장하기
response = requests.get('https:' + img_source)
with open('./output_image/hollys_coffee.png', 'wb') as image_file:
    image_file.write(response.content)
print('이미지 파일로 저장하였습니다.')
