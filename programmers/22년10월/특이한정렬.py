def solution(numlist, n):
    nlist = [[abs(num - n), num] for num in numlist]
    nlist.sort(key = lambda x:(x[0], -x[1]))
    return [lst[1] for lst in nlist]

def solution(numlist, n):
    return sorted(numlist, key=lambda x:(abs(x-n), -x))