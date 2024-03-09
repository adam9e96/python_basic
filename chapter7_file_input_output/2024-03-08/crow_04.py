import requests
from bs4 import BeautifulSoup as bs


# 크롤링을 이용한 환률 계산기 : 다른 나라의 통화를 원으로 계산
def get_exchange_rate(menu: int) -> float:  # 원하는 환률을 가져옴
    url: str = 'https://finance.naver.com/marketindex/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    exchange_rates = soup.select('#exchangeList > li> a.head > div > span.value')  # 환율 가져옴
    exchange_rate: float = float(exchange_rates[menu - 1].text.replace(",", ""))  # , 지우기
    return exchange_rate


print('=== 메 뉴===')
print('1. 미국')
print('2. 일본')
print('3. 유럽')
print('4. 중국')
print('============')
menu = int(input('선택 >>> '))
unit = ['달러', '엔', '유로', '위안']
money = int(input(f'금액 입력 (단위 : {unit[menu - 1]} >>> '))

if menu == 2:  # 일본을 선택했다면? 네이버에서는 100엔 기준 금액을 제공
    money = money / 100
print(get_exchange_rate(menu) * money, '원')

