def solution(n):
    prime = [1] * (n+1)
    for i in range(2, int(n**0.5)+1):
        for j in range(i+i, n+1, i):
            if j%i == 0:
                prime[j] = 0
    return sum(prime) - 2