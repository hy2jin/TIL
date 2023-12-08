def solution(numbers):
    ans = set()
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            ans.add(numbers[i] + numbers[j])
    return sorted(list(ans))