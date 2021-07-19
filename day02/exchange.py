# 현재 원/달러의 환율은 result입니다.
# requests, bs4 불러오기
import requests
from bs4 import BeautifulSoup

# 요청보내기 위한 url
url = 'https://finance.naver.com/marketindex/'

# 위 url로 요청을 보내기
response = requests.get(url).text
# print(response)
# print(type(response))       # <class 'str'>

# 응답받은 문자열을 text로 변환 후 보기 편하게 BeautifulSoup로 변환
data = BeautifulSoup(response, 'html.parser')
# print(type(data))       # <class 'bs4.BeautifulSoup'>

# BeautifulSoup의 데이터타입은 CSS 어쩌구 이용 어쩌구 해서 뽑아올 수 있다
# Copy selector

# 해당 페이지에서 원하는 값만 뽑아서 출력(태그가 긁어짐)
exchange_rate = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# print(exchange_rate)

# 태그를 제외한 해당하는 text만 출력
result = exchange_rate.text
print(f'현재 원/달러의 환율은 {result}입니다.')


# 엔화 출력
exchange_yen = data.select_one('#exchangeList > li > a.head.jpy > div > span.value').text
print(f'현재 원/엔의 환율은 {exchange_yen}입니다.')