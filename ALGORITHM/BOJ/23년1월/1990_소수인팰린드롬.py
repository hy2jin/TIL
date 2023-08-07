# 직접 for문을 돌려서 팰린드롬인 수를 만들고
# 일의 자리 수가 짝수가 아니고
# a이상 b 이하이고 소수인 수 출력 하는 방법도 있음

def isPalindrome(num: str) -> bool:
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True

def isPrime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

a, b = map(int, input().split())
# 10,000,000 이상에선 팰린드롬이면서 소수인 수가 없다고 하는데 이건 검색해서 알아냄..
# 이거 안해도 정답은 나오는데 시간이 444ms 에서 3192ms 가 됨
if b > 10000000: b = 10000000

for n in range(a, b + 1):
    # 소수가 먼저인지 보면 시간초과 -> 팰린드롬인 수가 소수의 수보다 적으면 이런가?
    # if isPrime(n) and isPalindrome(str(n)):
    if isPalindrome(str(n)) and isPrime(n):
        print(n)
print(-1)
