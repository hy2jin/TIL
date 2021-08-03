# # 2885
# def mul(a, b):
#     tmp = []
#     for i in b[::-1]:
#         print(int(a) * int(i))
#     return int(a) * int(b)
# a = input()
# b = input()
# print(mul(a, b))

# # 2884
# def alarm(h, m):
#     if m < 45:
#         h -= 1
#         m += 15
#         if h == -1:
#             h = 23
#     else:
#         m -= 45
#     print(h, m)
# h, m = map(int, input().split())
# alarm(h, m)

# # 14681
# def quadrant(x, y):
#     if x > 0:
#         if y > 0:
#             return 1
#         else:
#             return 4
#     else:
#         if y > 0:
#             return 2
#         else:
#             return 3
# a = int(input())
# b = int(input())
# print(quadrant(a, b))

# # 1330
# def compare(a, b):
#     if a > b:
#         return '>'
#     elif a < b:
#         return '<'
#     else:
#         return '=='
# a, b = map(int, input().split())
# print(compare(a, b))

# # 2739
# def gugudan(n):
#     for i in range(1, 10):
#         print(f'{n} * {i} = {n*i}')
# n = int(input())
# gugudan(n)

# # 10871
# def less_num(x, seq):
#     tmp = ''
#     for i in seq:
#         if int(i) < x:
#             tmp += i + ' '
#     return tmp[:-1]
# n, x = map(int, input().split())
# seq = input().split()
# print(less_num(x, seq))

# # 1110
# def plus_cycle(n):
#     cnt = 0
#     ori_n = n
#     while True:
#         n = 10 * (n%10) + (n//10 + n%10)%10
#         cnt += 1
#         if ori_n == n:
#             break
#     return cnt
# n = int(input())
# print(plus_cycle(n))

# # 10818
# def min_max(x):
#     print(min(x), max(x))
# a = input()
# b = tuple(map(int, input().split()))
# min_max(b)

# # 2562
# def maxi(numbers):
#     print(max(numbers))
#     print(numbers.index(max(numbers)) + 1)
# tmp = []
# for _ in range(9):
#     tmp.append(int(input()))
# maxi(tmp)

# 8958
def OX(res):
    cnt = 0
    scores = []
    for i in res:
        if i == 'O':
            cnt += 1
            scores.append(cnt)
        else:
            cnt = 0
    return sum(scores)s
a = int(input())
result = []
for _ in range(a):
    res = input()
    print(OX(res))