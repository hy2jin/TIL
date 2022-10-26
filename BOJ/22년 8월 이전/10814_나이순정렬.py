# BOJ 10814 나이순 정렬
'''
lst[i][0] = int(lst[i][0]) 과정이 필수!
-> string과 int는 sort의 결과가 다르다
'''
import sys
sys.stdin = open('input.txt')

lst = []
for i in range(int(input())):
    lst.append(input().split() + [i])
    lst[i][0] = int(lst[i][0])
lst.sort(key=lambda x:(x[0], x[2]))
for l in lst:
    print(l[0], l[1])