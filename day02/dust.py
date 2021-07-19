# sido_name의 미세먼지 농도는 dust입니다.
import requests

sidoname = input('전국, 서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종 중에서 선택해 주세요: ')
# sidoname = '경북'
key = 'A5LUlWkUcDs9f7krKYjN6gI%2BnphNSxmzh9ks3TA%2BAs6rDfXE92f3DWiwt6Rs3vGEKpSkBFjVKPcHDCn%2BQsmLWA%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=100&pageNo=1&sidoName={sidoname}&ver=1.0'

response = requests.get(url).json()

# 경북의 모든 데이터 찾기
datas = response['response']['body']['items']
# print(datas)

# 첫번째 지역 정보 가져오기
sido_name = datas[0]['stationName']
dust = datas[0]['pm10Value']
print(f'{sido_name}의 미세먼지 농도는 {dust}입니다.')


# 연일읍 찾기
items = response['response']['body']['items']
for value in items:
    if value['stationName'] == '연일읍':
        sido_name = value['sidoName']
        station_name = value['stationName']
        dust = value['pm10Value']
print(f'{sido_name} {station_name}의 메서먼지 농도는 {dust}입니다.')