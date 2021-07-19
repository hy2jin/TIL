# 터미널 단축키 ctrl + `
# 숫자
number = 3
print(type(number))

# 문자열
string = '문자열'
print(type(string))

# boolean
boolean = True
print(type(boolean))

# 형변환
string_number = '58'
print(type(int(string_number)))

# f-string / string interpolation
name = '홍길동'
print(f'{name}입니다. 반갑습니다.')


'''
리스트
'''
# 리스트 선언
my_list = ['java', 'python']
print(my_list[0])

# 리스트 원소 변경
my_list[0] = 'django'
print(my_list)

# 리스트 길이
print(len(my_list))


'''
딕셔너리
'''
my_info = {
    'name' : '이혜진',
    'age' : 13
}
print(my_info)

# 딕셔너리는 원소 접근 방법이 2가지가 있다
# 가지고 있지 않은 key로 접근하면 keyerror가 발생한다.
print(my_info['name'])
# print(my_info['location'])

# 딕셔너리가 가지고 있는 get함수
print(my_info.get('name'))
print(my_info.get('location'))
# get()함수를 사용했을 때 없는 key로 접근하면 None을 출력한다.

# 원소변경
my_info['name'] = '홍길동'
print(my_info)


'''
딕셔너리 실습
'''
coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}

# 2-1. 코인의 정보에서 BTC의 최대 가격을 출력하시오.
BTC_dic = coin['BTC']
# print(BTC_dic)
print(BTC_dic['max_price'])
print(coin['BTC']['max_price'])

# 2-2. BTC의 시가와(opening price) XRP의 시가를 더한 결과를 출력하시오.
XRP_dic = coin['XRP']
print(BTC_dic['opening_price'] + XRP_dic['opening_price'])
print(int(coin['BTC']['opening_price']) + float(coin['XRP']['opening_price']))