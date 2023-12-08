def solution(quiz):
    ans = []
    for qu in quiz:
        qu = qu.split(' = ')
        if '+' in qu[0]:
            a, b = qu[0].split(' + ')
            left = int(a) + int(b)
        else:
            a, b = qu[0].split(' - ')
            left = int(a) - int(b)
        q = 'O' if left == int(qu[1]) else 'X'
        ans.append(q)
    return ans
        

# def solution(quiz):
#     ans = []
#     for qu in quiz:
#         qu = qu.split("=")
#         q = "O" if eval(qu[0]) == int(qu[1]) else "X"
#         ans.append(q)
#     return ans
