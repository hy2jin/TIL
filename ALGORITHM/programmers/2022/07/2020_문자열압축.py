def solution(s):
    answer = len(s)     # 최대 길이는 현재 문자열의 길이
    if len(s) == 1:     # 길이가 1인 경우와 그 외
        return 1

    for n in range(1, len(s)//2 + 1):       # n은 패턴의 길이 -> 최대는 문자열 길이의 절반
        newstring = ''                      # 압축한 문자열
        cnt = 1                             # 앞에 적을 정수
        patternS = s[:n]                    # 반복되는 패턴의 형태
        
        for i in range(n, len(s)+n, n):     # index n부터 문자열길이+n-1까지 n의 간격으로 시작점
            if patternS == s[i:i+n]:        # 뒤에 같은 패턴이 있으면 cnt더하고 다음 확인
                cnt += 1

            else:                           # 뒤에 같은 패턴이 없으면
                if cnt == 1:                # 1은 생략
                    newstring += patternS
                else:                       # 정수 붙여주기
                    newstring += str(cnt)+patternS
                patternS = s[i:i+n]         # 다음 패턴
                cnt = 1
        answer = min(answer, len(newstring))
    return answer
