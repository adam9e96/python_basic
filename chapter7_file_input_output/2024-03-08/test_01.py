import requests
from bs4 import BeautifulSoup as bs

# 연습용
url: str = ''
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)

tag_series = soup.select_one(
    '.#container > section.left_content > article:nth-child(3) > div.gall_listwrap.list > table > tbody')
print(tag_series)
