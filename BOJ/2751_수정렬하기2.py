# BOJ 2751 수 정렬하기 2
'''
속도가 중요하다고 판단하여 readline 사용
-> pypy로 제출하면 readline 없이도 통과하지만 python3으로는 readline없이 통과 불가능
'''
import sys
N = int(sys.stdin.readline())
lst = sorted([int(sys.stdin.readline()) for _ in range(N)])
for i in lst:
    print(i)