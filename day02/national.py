import requests

name = 'lee'
url = f'https://api.nationalize.io/?name={name}'


# 응답받은 값을 json 함수를 통해 dict로 변환하고 확인하기
response = requests.get(url).json()
print(response)


name = response['name']
country_id = response['country'][0]['country_id']
probability = response['country'][0]['probability'] * 100


# round 내장함수로 반올림 가능
# round(float, 반올림하고자 하는 위치)
print(f'{name}의 국가는 {round(probability, 2)}% 확률로 {country_id}입니다.')