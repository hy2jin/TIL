# BOJ 16922 로마 숫자 만들기
from itertools import combinations_with_replacement

N = int(input())
ans = set()
lst = [1, 5, 10, 50]

for combi in combinations_with_replacement(lst, N):
    ans.add(sum(combi))
print(len(ans))