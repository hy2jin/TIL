# requests 불러오기
import requests
from pprint import pprint

# 봇 토큰, 요청 통합 URL 변수에 담기
TOKEN = '1874551538:AAGxktk_aPVxwGU5cs2guHdnbWeB7FlXDEM'
url = f'https://api.telegram.org/bot{TOKEN}'

# 내 챗봇에 메세지 보낸 사람 정보 알아내기 (getUpdates)
get_updates_url = f'{url}/getUpdates'
response = requests.get(get_updates_url).json()

# 그 사람이 보낸 메세지와 그 사람의 chat_id 알아내기
# pprint(response)      # 예쁘게 프린트하기
chat_id = response['result'][-1]['message']['from']['id']
text = response['result'][-1]['message']['text']
print(chat_id, text)

# 메시지 보낸 사람에게 그 사람이 보낸 메시지 다시 돌려보내기
# sendMessage method의 필수 params인 chat_id와 text를 넣기
send_message_url = f'{url}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(send_message_url)
