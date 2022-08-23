def solution(price, money, count):
    ans = 0
    for i in range(1, count+1):
        ans += price*i
    if ans > money:
        return ans-money
    return 0