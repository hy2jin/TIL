# def solution(elements):
#     arr = elements + elements
#     N = len(elements)
#     ans = set()
    
#     for i in range(N):          # 길이가 i + i
#         for j in range(N):      # 시작위치가 j
#             ans.add(sum(arr[j : j + i + 1]))
            
#     return len(ans)


def solution(elements):
    N = len(elements)
    ans = set()

    for i in range(N):
        SUM = elements[i]
        ans.add(SUM)
        for j in range(i + 1, i + N):
            SUM += elements[j % N]
            ans.add(SUM)
    return len(ans)