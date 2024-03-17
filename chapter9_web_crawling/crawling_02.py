# beautifulsoup4 주요 메서드
# find, findall, select, selectall 을 주로 씀
import pprint

import requests
from bs4 import BeautifulSoup as bs

# BeautifulSoup 실습 : find() 메소드 이용 하기

# 1) find() 메소드
# 지정된 태그들 중에서 가장 첫 번째 태그만 가져오는 메소드(하나의 값만 반환). 문자열 형태로 반환.
# 일반적으로 하나의 태그만 존재하는 경우에 사용. 만약 여러 태그가 있으면 첫 번째 태그만 가져옴.

# 위키피디아 '대구광역시' 페이지
url = 'https://ko.wikipedia.org/wiki/%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C'
resp = requests.get(url)
soup = bs(resp.text, 'html.parser')
# print(soup.prettify().strip()) # 파싱 제대로 되었는지 확인

first_img = soup.find(name='img')  # img 태그 중에 제일 먼저 나오는 것
# print(type(first_img))  # <class 'bs4.element.Tag'>

# print(first_img)  # <img alt="" aria-hidden="true" class="mw-logo-icon" height="50" src="/static/images/icons/wikipedia.png" width="50"/>

target_img = soup.find(name='img', attrs={'alt': 'Daedongyeojido (Gyujanggak) 17-02.jpg'})
# print(type(target_img)) # <class 'bs4.element.Tag'>
# print(target_img)

#######################
# BeautifulSoup 실습 : find_all() 메소드 이용하기

# find_all() 메소드
# 지정한 태그들을 모두 가져오는 메소드. 가져온 태그들은 모두 리스트에 보관


# url: str = 'https://namu.wiki/w/%EC%97%AD%EC%98%A8%EB%8F%84'    # 나무위키 최근
# resp = requests.get(url)
# soup = bs(resp.text, 'html.parser')
# print(soup)
# pprint.pprint(soup,indent=4)

url: str = 'https://sports.news.naver.com/index.nhn'
resp = requests.get(url)
soup = bs(resp.text, 'html.parser')  # html 방식으로 가져온것을 soup에 담음

# today_list = soup.find('ul',{'class':'today_list'}).find_all('strong',{'class':'title'})
today_list = soup.find('ul', {'class': 'today_list'})
# print(today_list)

today_list_title = today_list.find_all('strong', {'class', 'title'})

# print(today_list_title)

# pprint.pprint(today_list_title)
# pretty print

# for title in today_list_title:
#     print(title.text.strip())

# for title in today_list_title:
# print(title.text.strip())  # 양쪽 공백 제거
# '커리 29점' GSW, 압도적 화력으로 MIL 제압
# '류현진은 류현진! ' 3이닝-KKK-최고 143㎞… '청백전인데' 6만 야구팬이 지켜봤다
# '헌신한 김민재는 뒷전' 투헬 이어 케인까지 '다이어 밀어주기' 동참…"英 대표팀에서 큰일 했던 선수"
# '사생활 논란' 나균안 '포스트 이정후' 이주형 등 '팀 코리아' 합류 불발…'vs MLB' 류중일호 35인 확정
# 맨체스터 유나이티드 '새 감독'으로 급부상…랫클리프 구단주가 직접 추진한다
# FC서울 '폭풍영입'…린가드 이어 국가대표 출신 강상우 품었다


# 다음 뉴스
url = 'https://news.daum.net/'
resp = requests.get(url)
soup = bs(resp.text, 'html.parser')

# a 태그의 갯수 출력.
# print('1. a 태그의 갯수')
# print(len(soup.find_all('a')))  # 124
# print()

# a 태그 20개만 출력
print('2. a 태그 20개만 출력')
# for news in soup.find_all('a')[:20]:
#     print(news.text.strip())

# a 태그 5개 출력
# print('3. a 태그 링크 5개 출력')
# for i in soup.find_all('a')[:5]:
#     print(i.attrs['href'])
#     print(i.get('href'))
# print("=" * 20)

# 특정 클래스 속성을 출력하기
# print('4. 특정 클래스 속성을 출력')
# print(soup.find_all('div', {'class': 'item_issue'}))
# print("=" * 20)

# 링크를 텍스트 파일로 저장
print('5. 링크를 텍스트 파일로 저장')
file = open('./output/crawling_02_links.txt', 'w')  # 쓰기 전용 파일 생성.

for i in soup.find_all('div', {'class': 'item_issue'}):
    # print(i.find('a'))
    # print('-' * 20)
    # print(i.find('a').get('href'))
    file.write(i.find('a').get('href') + '\n')
file.close()
print('저장성공')
# 문제 : with 사용. 뉴스 타이틀 추출. 파일명은 news_title.txt
# 넘버링 붙도록 예) 1. 日증시, 차익매물에 사흘만에 40,000 아래로...장중엔 한떄 최고(종합)

file_name: str = 'crawling_02_news_title.txt'
with open(f'./output/{file_name}', 'w', encoding='utf-8') as file:
    for i,news in enumerate(soup.find_all('div', {'class': 'item_issue'})):
        # print(i.find('a').get(''))
        # print(i.find('a').get('strong'))
        print(news.find_all("a")[1].text.strip())
        # print(news.find_all('a')[1].text.strip())
        file.write(f'{i+1}.{news.find_all("a")[1].text.strip()}\n')
        # print('*' * 20)
print()
