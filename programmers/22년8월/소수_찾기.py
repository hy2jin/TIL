from itertools import permutations as pm

def solution(numbers):
    N = len(numbers)
    
    # 소수 리스트 만들기
    M = max(numbers, key=lambda x:int(x))
    chkN = int(N*M)+1
    primeList = [1] * chkN
    primeList[0] = primeList[1] = 0
    for i in range(2, chkN//2 + 1):
        for j in range(i*2, chkN, i):
            primeList[j] = 0

    # 소수인지 확인
    ans = set()
    for cnt in range(1, N+1):
        for num in pm(numbers, cnt):
            num = int(''.join(list(num)))
            if primeList[num]:
                ans.add(num)
    return len(ans)