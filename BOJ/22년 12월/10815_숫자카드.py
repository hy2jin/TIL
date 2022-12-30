import sys
sys.stdin = open("input.txt")

"""
N = int(input())
cards = list(map(int, input().split()))
cards.sort()
_ = input()
nums = list(map(int, input().split()))

def binary_search(n):
    s, e = 0, N - 1
    while s <= e:
        m = (s + e) // 2
        if cards[m] == n:
            ans.append(1)
            return
        if cards[m] < n:
            s = m + 1
        else:
            e = m - 1
    ans.append(0)
    return

ans = []
for n in nums:
    binary_search(n)
print(*ans)
"""

_ = input()
cards = set(input().split())
_ = input()
nums = input().split()

ans = []
for n in nums:
    ans.append(1) if n in cards else ans.append(0)

print(*ans)
