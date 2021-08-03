# Flask 불러오기
# Flask는 파이썬이 기본으로 가지고 있는 모듈이 아니므로 설치해야한다 ==> pip install Flask

from flask import Flask, render_template, request
import requests

TOKEN = '1874551538:AAGxktk_aPVxwGU5cs2guHdnbWeB7FlXDEM'
url = f'https://api.telegram.org/bot{TOKEN}'

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Flask로 어떤 문서를 응답할 때, return에 작성하는 것이 아니라
# 특정 문서자체를 불러와서 응답해 줄 수 있다 ==> render_template
# flask가 가지고 있는 render_template를 가져오기 (위에서)
# html문서 하나 만들고, 그 문서를 보여주는 페이지 만들기
@app.route('/ssafy')
def ssafy():
    # ssafy.html을 rendering 하기
    return render_template('ssafy.html')


# 로그인이든 아니면 채팅이든
# 내가 입력한 값을 보낼 수 있는 메시지를 보낼 수 있고
# 보내온 메시지를 받아서 어떤 행위를 실행하는 코드
# write함수(메시지를 입력하는 곳), send(메시지를 받는 곳)
# 주소 함수이름이랑 동일하게 작성하기 / html 이름도 함수 이름이랑 동일하게 작성하기
# 안의 내용은 일단 제목만 입력해서 두 페이지 정상작동하는지 확인

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    # 사용자가 요청보낸 정보 확인 할 수 있는 request 불러오기
    # from flask import request -> 최상단에 작성
    # print(request)      # <Request 'http://127.0.0.1:5000/send?message=안녕하세요' [GET]>
    # print(dir(request))
    message = request.args.get('message')

    # 텔레그램 챗봇 api url, 내 챗봇 토큰 필요 ==> 위에 적음

    # 메시지 보낼 사람 chat_id 필요
    chat_id = 1814392800
    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={message}'

    # 파이썬으로 요청보내느 requests 필요
    requests.get(send_message_url)
    return render_template('send.html')


# POST 방식의 요청만 받겠다
@app.route('/telegram', methods = ['POST'])
def telegram():
    # 요청 정보는 request에 들어있다.
    response = request.get_json()
    # print(response)
    # response에 chat_id, text 들어있다

    # 1.
    # 사용자가 챗봇한테 보낸 메시지 똑같이 돌려보내주는 코드
    chat_id = response['message']['from']['id']
    text = response['message']['text']

    # 2.
    # text에 들어있는 값이 '누구야' 일때 '저는 ~~님의 챗봇입니다.' 반환
    # 조건문을 넣어주면 될 것 같다
    if text == '누구야?':
        text = '저는 이혜진님의 챗봇입니다.'

    # 3.
    # 어제 작성한 미세먼지 API 코드도 같이 가지고 와서 '미세먼지'라고 입력 받으면
    # 미세먼지 정보를 알려주는 코드 작성
    elif text == '미세먼지':
        key = 'A5LUlWkUcDs9f7krKYjN6gI%2BnphNSxmzh9ks3TA%2BAs6rDfXE92f3DWiwt6Rs3vGEKpSkBFjVKPcHDCn%2BQsmLWA%3D%3D'
        dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName=경북&ver=1.0'
        dust_response = requests.get(dust_url).json()
        # 경북의 모든 정보 items에 담기
        items = dust_response['response']['body']['items']
        for value in items:
            if value['stationName'] == '연일읍':
                sido_name = value['sidoName']
                station_name = value['stationName']
                dust = value['pm10Value']
        text = f'{sido_name} {station_name}의 메서먼지 농도는 {dust}입니다.'

    send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_message_url)

    '''
    {
        'update_id': 847325787, 
        'message': {
            'message_id': 15, 
            'from': {
                'id': 1814392800, 
                'is_bot': False, 
                'first_name': '혜진', 
                'last_name': '이', 
                'language_code': 'ko'
            }, 
            'chat': {
                'id': 1814392800, 
                'first_name': '혜진', 
                'last_name': '이', 
                'type': 'private'
            },
            'date': 1626413425,
            'text': '되나?'
        }
    }
    '''
    # 응답은 본문과 status_code 200을 같이 보내준다.
    return '', 200












if __name__ == '__main__':
    app.run(debug = True)