from pprint import pprint

import requests  # 웹페이지 요청을 보내고 응답을 받기 위해 사용
from bs4 import BeautifulSoup as bs  # html과 xml 파일을 파싱하기 위한 라이브러리

# 파이썬을 이용하여 네이버웹페이지 HTML 파싱

# 웹 페이지 요청 보내기
url = 'https://www.naver.com/'  # 웹페이지 주소
response = requests.get(url)  # get() 또는 post() 메소드를 이용해서 html 정보를 받아옴.
# requests.get(url): 지정된 URL로 HTTP GET 요청을 보내고, 서버로부터의 응답을 response 객체에 저장합니다.

# html = response.text    # response 객체의 text 속성을 지정하면 html 정보 반환.

# print(response) # <Response [200]>
# print(response.text)
# pprint(response.text,indent=4)

# HTML 파싱
soup = bs(response.text, 'html.parser')
# BeautifulSoup 생성자는 두 개의 인자를 받음
# 파싱할 HTML 문자열(response.text)과 사용할 파서의 종류('html.parser')
# 위 코드는 response.text에서 반환된 HTML을 파싱하여 soup 객체에 저장한다.

# 파싱된 HTML 출력
# print(soup)   # soup 객체를 출력하여 파싱된 HTML 구조를 볼 수 있다.
# 이렇게 실행된ㄱ 결과는 HTML 소스 코드 전체를 출력한다. 출력된 soup 객체를 통해,
# 필요한 데이터를 찾거나, 특정 HTML 요소에 접근하는 등의 추가적인 작업을 수행할 수 있다.
# e.g ) 특정 태그를 찾거나, 클래스 이름으로 요소를 검색하는 것이 가능하다.

pprint(soup.prettify())
