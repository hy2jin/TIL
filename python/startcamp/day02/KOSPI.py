# requests 불러오기
import requests
from bs4 import BeautifulSoup

# 원하는 정보가 있는 주소로 요청을 보내고 응답을 문자열로 반환하여 저장한다.
url = 'https://finance.naver.com/sise/'
response = requests.get(url).text

# bs4를 통해 파이썬이 읽을 수 있는 데이터형으로 변경
# 변경하는 문서가 어떤 형태인지도 같이 작성해 줘야 한다.
# html.parser -> html 문서를 파이썬에서 읽을 수 있도록 만들어준다.
data = BeautifulSoup(response, 'html.parser')
# print(response)
# print(data)
# print(type(response))
# print(type(data))

# 바꾼 정보 중 원하는 것만 뽑아서 출력한다.
kospi = data.select_one('#KOSPI_now')
# print(kospi)
# print(type(kospi))
result = kospi.text
print(type(result))

# 현재의 코스피 지수는 result입니다.
print(f'현재의 코스피 지수는 {result}입니다.')