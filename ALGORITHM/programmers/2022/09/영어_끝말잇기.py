def solution(n, words):
    dic = {k: 0 for k in words}
    dic[words[0]] = 1
    for i in range(1, len(words)):
        word = words[i]
        if dic[word] == 0 and words[i-1][-1] == word[0]:
            dic[word] = 1
        else:
            a, b = divmod(i+1, n)
            if b: a += 1
            else: b = n
            return [b, a]
    return [0, 0]
        