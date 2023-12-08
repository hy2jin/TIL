from collections import Counter

def solution(X, Y):
    ans = ''
    
    xCounter = Counter(X)
    yCounter = Counter(Y)
    
    for i in range(9, -1, -1):
        n = str(i)
        ans += n * min(xCounter[n], yCounter[n])
        
    if not ans:
        return '-1'
    if len(ans) == ans.count('0'):
        return '0'
    return ans


# def solution(X, Y):
#     xArr = [0] * 10
#     yArr = [0] * 10
#     for x in X:
#         xArr[int(x)] += 1
#     for y in Y:
#         yArr[int(y)] += 1

#     tmp = ''
#     for i in range(10):
#         if xArr[i] == 0 or yArr[i] == 0:
#             continue
#         tmp = str(i) * min(xArr[i], yArr[i]) + tmp

#     if len(tmp) == 0:
#         return '-1'
#     if tmp.count('0') == len(tmp):
#         return '0'
#     return tmp
