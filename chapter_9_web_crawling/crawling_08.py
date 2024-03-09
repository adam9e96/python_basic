import requests
from bs4 import BeautifulSoup as bs  # <--은 지금 안씀 html 파싱을 안함
import os.path

# 야후 이미지 검색 이용.
url = 'https://images.search.yahoo.com/search/images;_ylt=Awr.zyvbp.pl61MBC6hXNyoA;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=stock&fr2=piv-web&fr=yfp-t'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)

# 이미지 태그 찾은 case
# tag_image = soup.select('li.ld a > img')
# tag_image = soup.select('li.ld a > img')
tag_image = soup.select('li a > img')
# tag_image = soup.select_one('ul > li > a > img').get('data-src')
# print(tag_image)
# pprint.pprint(tag_image)

# 2. 이미지 저장
dir_save = './output_image/yahoo'  # 저장 경로
# dir_save = '../chapter7_file_input_output/2024-03-08/output_image/yahoo/'  # 저장 경로

for idx, tag in enumerate(tag_image, 1):
    response = requests.get(tag.get('data-src'))
    with open(f'{dir_save}/{idx}.png', 'wb') as image_file:
        image_file.write(response.content)
        print(f'{idx}/{len(tag_image)}')
print(f'{len(tag_image)}개의 이미지 파일 저장 성공 ')

# for idx, tag in enumerate(tag_image):
#     # print(tag.get('data-src'))
#     response = requests.get(tag.get('data-src'))
#     with open(f'{dir_save}{idx + 1}.png', 'wb') as image_file:
#         image_file.write(response.content)
#         print(f'{idx + 1} /{len(tag_image)}')
#         if idx + 1 == len(tag_image):
#             print('100% 저장완료.')
