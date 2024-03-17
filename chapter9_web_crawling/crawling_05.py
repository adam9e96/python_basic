import requests
from bs4 import BeautifulSoup as bs

# 네이버 환율 크롤링
# 네이버에서 '환율'
url: str = 'https://finance.naver.com/marketindex/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.prettify())  # 제대로 전체를 긁어왔는지 테스트

# 국가를 가져오기
nations = soup.select('#exchangeList > li > a.head > h3 > span')
# print(nations)

# 환율 가져오기
exchange_rates = soup.select('#exchangeList > li> a.head > div > span.value')  # 환율 가져옴
# print(exchange_rates.text)

# 미국 USE : 1,326.40
# 일본 JPY(100엔) : 896.55


# for idx, item in enumerate(exchange_rates):
#     print(f'{item.text} : {exchange_rates[idx].text}')
# for idx, item in enumerate(nations):
#     print(f'{item.text} : {exchange_rates[idx].text}')


