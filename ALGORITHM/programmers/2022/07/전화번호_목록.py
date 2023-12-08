# 접두어가 있으면 false / 접두어가 없으면 true

# 정석으로 해시 사용
def solution(phone_book):
    dic = {}
    for phone in phone_book:
        dic[phone] = 1

    for phone in phone_book:
        tmp = ''
        for num in phone:
            tmp += num
            if tmp in dic and tmp != phone:
                return False
    return True

# startswith 사용하는 방법
def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            return False
    return True
