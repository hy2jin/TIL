# setWebHook 요청 보내기 위한 requests
import requests

# token, url, ngrok url
TOKEN = '1874551538:AAGxktk_aPVxwGU5cs2guHdnbWeB7FlXDEM'
url = f'https://api.telegram.org/bot{TOKEN}'

# ngrok http 5000 -> 우클릭
# ngrok_url = 'https://6044ab997c01.ngrok.io'
python_anywhere = 'https://hy2jinl22.pythonanywhere.com'
set_webgook_url = f'{url}/setWebhook?url={python_anywhere}/telegram'

# telegram이 내 ngrok/telegram으로 요청을 보내고, 200 응답 받아간다
response = requests.get(set_webgook_url)
print(response.text)