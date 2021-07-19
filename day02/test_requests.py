# 파이썬으로 요청 보내기 위한 준비
# requests 라는 모듈을 사용 할거다.
# 그러기 위해서 불러온다
import requests

# requests로 https://www.naver.com 으로 요청 보낸 결과 출력
print(requests.get('https://www.naver.com'))

# alt + 방향키 위 아래로 한줄 복사
print(requests.get('https://www.naver.com').text)
print(requests.get('https://www.naver.com').status_code)
print(type(requests.get('https://www.naver.com').status_code))