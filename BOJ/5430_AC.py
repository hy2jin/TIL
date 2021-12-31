# BOJ 5430 AC
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline
'''
R: 배열에 있는 숫자의 순서 뒤집기
D: 첫 번째 숫자 버리기
배열이 비어있는데 D를 사용하면 에러 발생
'''

for _ in range(int(input())):
    func = input().rstrip()
    D_cnt = func.count('D')
    n = int(input())
    lst = input()[1:-2].split(',')
    if D_cnt > n:           # error 걸러내기
        print('error')
        continue
    Q = deque(lst)
    se = True               # 똑바로(True) or 거꾸로(False)
    for f in func:
        if f == 'R':        # 순서 뒤집기
            se = not (se)
        elif se:            # 앞에 숫자 버리기
            Q.popleft()
        else:               # 뒤에 숫자 버리기
            Q.pop()
    ans = list(Q) if se else list(Q)[::-1]
    print('[' + ','.join(ans) + ']')
