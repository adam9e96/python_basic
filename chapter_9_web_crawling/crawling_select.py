import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : select_one() 메소드 이용하기

# find가 원하는 태그를 찾는게 목적이라면 select 는 CSS selector로 tag 객체를 찾아 반환
# select_one() 은 원하는 태그 하나만 가져오고, 태그가 많은 경우에는 맨 앞의 것만 가져옴

# 1. 대구광역시 위키피디아에서 상징 -> 시조 -> 독수리 들고 오기
url: str = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

# select 계열의 메서드는 css selector 이용 가능.
# '.' -> class 속성, '#' -> id 속성
# class : 하나의 html 에서 여러 태그에 중복 사용 가능
# id : 하나의 html에서 한번만 사용. 권장사항

# mw-parser-output 클래스 속성을 가진 태그의 자식 요소 중 ul 태그만 가져옴
tag_symbol = soup.select_one('.mw-parser-output ul')
print(tag_symbol) # 출력

# 2. 대구광역시 위키피디아에서 공원 들고 오기 # 일단 PASS
# url: str = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')

# tag_prak = soup.select_one('#mw-content-text > div.mw-content-ltr.mw-parser-output')
# print(tag_prak)

# 3. 다음 > 뉴스 > IT > 오늘의 연재 의 첫번쨰 글 제목과 신문사 들고오기
url: str = 'https://news.daum.net/digital#1'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
tag_series = soup.select_one('.list_todayseries li')
# print(tag_series)

# print()
tag_series_title = soup.select_one('.link_txt').text
# print(f'제목: {tag_series_title}')

tag_series_press = soup.select_one('.txt_info').text
# print(f'신순마: {tag_series_press}')

# 할리스 커피 매장 검색

url: str = 'https://www.hollys.co.kr/store/korea/korStore2.do'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup.prettify())  # html 문서를 제대로 가져 왔는지 테스트 출력

# 매장 테이블 가져오기 이런류 태그는 주로 li나 table 태그를 자주 사용함
stores = soup.select_one('#contents > div.content > fieldset > fieldset > div.tableType01 > table')

# print(stores)

first_store = stores.select_one('#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr:nth-child(1)')
# print(first_store)

# td:nth-child(1) -> td 태그중 첫번째 . 태그숫자는 1번부터 시작함
second_store_name = first_store.select_one('td:nth-child(2)')# 위치상 3번인데 1번은 주석처리되어 2번검색하면 나옴
print(second_store_name.text)

second_store_address = first_store.select_one('td:nth-child(4)')
print(second_store_address.text)

