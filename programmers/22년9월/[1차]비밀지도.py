def solution(n, arr1, arr2):
    lst1 = []
    for num in arr1:
        tmp = bin(num)[2:]
        tmp = '0' * (n - len(tmp)) + tmp
        lst1.append(tmp)
    lst2 = []
    for num in arr2:
        tmp = bin(num)[2:]
        tmp = '0' * (n - len(tmp)) + tmp
        lst2.append(tmp)
    ans = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if lst1[i][j] == '0' and lst2[i][j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        ans.append(tmp)
    return ans
