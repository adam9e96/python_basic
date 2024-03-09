import requests
from bs4 import BeautifulSoup as bs

#
url: str = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.prettify())

data = soup.select('table tbody tr')[0]
print(data)
