## 크롤링

- 크롬이 주소에 대한 요청을 보내고, 그 응답 결과를 웹 화면으로 예쁘게 보여준다.

#### import requests

1. requests.get(주소) : '주소'에 요청(requests)보내서, 정보를 받아줘(get)
2. requests.get(주소).text : '주소'에 요청(requests)보내서, 정보를 받아서(get), 글(text)만 뽑아줘
3. requests.get(주소).status_code :  : '주소'에 요청(requests)보내서, 정보를 받아서(get), 상태(status_code)만 뽑아줘

- 2xx : 요청과 응답 성공
- 4xx : 요청이 잘못됨
- 5xx : 서버측에 문제가 있음



#### from bs4 import BeautifulSoup

1. BeautifulSoup(response) : 받은 문서를 보기 좋게 만들어줘
2. BeautifulSoup.select(response) : 문서 안에 있는 특정 내용을 뽑아줘(select)
3. BeautifulSoup.select_one(정보경로) : 문서 안에 있는 특정 내용을 하나만 뽑아줘(select_one)



#### API

- 편지같이 정해져 있는 약속(ex.보내는 사람, 받는 사람 등등 정해진 약속에 맞춰서 작성을 해야 함)