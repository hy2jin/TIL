import requests

name = 'lee'
url = f'https://api.agify.io/?name={name}'


# response = requests.get(url).text
# print(response)
# print(type(response))       # <class 'str'>

response = requests.get(url).json()
print(response)
# print(type(response))       # <class 'dict'>


# name의 나이는 age입니다.
name = response['name']
age = response['age']
print(f'{name}의 나이는 {age}살입니다.')