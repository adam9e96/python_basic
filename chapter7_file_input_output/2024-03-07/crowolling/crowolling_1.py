# 크롤링 1편
import urllib.request as request

import requests

# 정상 접속.
url = "https://www.python.org"
code = request.urlopen(url)
print(code)  # <http.client.HTTPResponse object at 0x000001DBB2B4D270>

# 비정상 접속. 비정상일 경우 에러 발생.
# url = 'https://www.python.org/1'
# code = request.urlopen(url)
# print(code)

url = "https://www.python.org"
response = requests.get(url)
print(response)  # <Response [200]> . 정상적인 통신이 이루어짐

# 페이지가 없는 경우에도 에러가 발생하지 않고, Response [404]
url = "https://www.python.org/1"
response = requests.get(url)
print(response)  # <Response [404]>

# 응답 코드 : 서버에서 클라이언트로 보내는 코드
# 1XX : 요청을 받았고, 작업 진행 중.
# 2XX : 사용자의 요청이 성공적으로 수행 됨.
# 3XX : 요청은 완료 되었으나, 리다이렉션이 필요.
# 4XX : 사용자의 요청이 잘못됨.
# 5XX : 서버에 오류가 발생함.

# 현재는 거의 90% requests를 사용함

from bs4 import BeautifulSoup as bs
import requests

# pip install beautifulsoup4 : 경고 메시지 출력을 막기 위해 4.10.0 으로 설치

# 서버로 요청을 할 때 브라우저의 정보 (User-Agent) 가 같이 전달됨.
# 서버에서는 브라우저의 정보를 가지고 접속자가 bot 인지 일반 사용자인지 구분함.
# 특정 사이트의 경우 요청하는 브라우저의 정보가 일반 사용자가 아니면 접속을 막는 경우가 있음.
# requests 의 경우 브라우저의 헤더 정보를 수정해서 일반 브라우저 처럼(?) 접속 할 수 있게됨

# 헤더 정보를 확인
url: str = 'https://planet-trade.kr/header_info.php'
# 접속 IP : 58.149.46.252 접속 정보 : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
# 이 정보를 이용해 접근해온 유저의 정보를 알 수 있다.

response = requests.get(url)
soup = bs(response.text, 'html.parser')
# print(soup)
# 접속 IP : 58.149.46.252
# 접속 정보 : python-requests/2.31.0


# 접속 정보를 위장 하는 법

# 2. requests에서 헤더 정보를 졉경할 수 있음.
request_headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 12.0; Win64; x64) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'),
    'Referer': '',
}
resp = requests.get(url, headers=request_headers)
soup = bs(resp.text, 'html.parser')
# print(soup)
# 접속 IP : 58.149.46.252
# 접속 정보 : Mozilla/5.0 (Windows NT 12.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
# Windows NT 12로 변경됨


# requests 사용법
url = 'https://www.naver.com/'
response = requests.get(url)    # get() 또는 post() 메서드를 이용해서 html 정보를 받아옴. # get메소드의 반환형은 Response -> html 파일/소스가 담겨있음

html = response.text    # response 객체의 text 속성을 지정하면 html 정보 반환.
# print(html) # html 소스가 출력.

headers = response.headers  # response 객체의 headers 속성 지정하면 헤더 정보 반환.
# print(headers)
"""
{'Server': 'NWS', 'Date': 'Thu, 07 Mar 2024 03:31:51 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': 'PM_CK_loc=29890f71f677ba5a1b9ecf6c1a0dcac5bbf6f5bce444458b0b94f7ca3da5c0eb; Expires=Fri, 08 Mar 2024 03:31:51 GMT; Path=/; HttpOnly', 'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'X-Frame-Options': 'DENY', 'X-XSS-Protection': '1; mode=block', 'Content-Encoding': 'gzip', 'Strict-Transport-Security': 'max-age=63072000; includeSubdomains', 'Referrer-Policy': 'unsafe-url'}
"""


import requests

# 모든 크롤링이 불법은 아님.
# 하지만 운영자의 의사에 상관없이 무단으로 크롤링하는 것은 불법.
#
# 운영자의 의사를 알수 있는 방법.
# robot.txt 에서 확인
#
# allow는 허용
# disallow는 검색 불가

# https://searchadvisor.naver.com/guide/seo-basic-robots
# https://developers.google.com/search/docs/advanced/robots/intro?hl=ko

urls = ['https://www.naver.com/', 'https://ko.wikipedia.org/']
filename = 'robots.txt'


for url in urls:
    file_path = url + filename
    print(file_path)
    resp = requests.get(file_path)
    print(resp.text)
    print("\n")
## 13시
# BeautifulSoup : 구문을 분석해서 필요한 내용만 추출 할 수 있는 기능을 가지고 있는 외부 패키지
with open('./sample.html','r',encoding='utf-8') as file:
    html = file.read()

soup = bs(html,'html.parser') # html.parser : html 코드를 사용하기 쉽게 BeautifulSoup의 객체로 파싱

print(type(soup))   # <class 'bs4.BeautifulSoup'>   # bs4.BeautifulSoup의 객체가 생성된거임

print(soup) # html 출력

print(soup.find('title').text)  # 문서의 제목
# 출력 : This is title.
print(soup.find('div').text)
# Division의 약자로, 레이아웃을 나누는데 사용.
print(soup.find('div').text)
print(soup.find('h1').text) # .text는 태그는 뺀 하위 문자열만 가져옴
print(soup.find('h1').text.strip())

