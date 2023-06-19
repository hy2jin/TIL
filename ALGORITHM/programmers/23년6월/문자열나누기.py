def solution(s):
    idx = ans = 0               # x의 index, 답

    while idx < len(s):
        x = 1                   # x의 수
        y = 0                   # x가 아닌 수
        for i in range(idx + 1, len(s)):
            if s[idx] == s[i]: x += 1
            else: y += 1

            if x == y:
                ans += 1
                idx = i + 1
                break
        else:                   # break로 끝난게 아님 -> for문을 다 돌았으면 지금꺼 +1 해서 리턴
            return ans + 1
    return ans                  # break해서 while로 올라갔는데 idx가 len(s)가 됨 -> 그대로 출력