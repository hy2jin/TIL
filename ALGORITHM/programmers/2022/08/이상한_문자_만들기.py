def solution(s):
    words = s.split(' ')
    for idx in range(len(words)):
        word = words[idx]
        tmp = ''
        for i in range(len(word)):
            if i%2:
                tmp += word[i].lower()
            else:
                tmp += word[i].upper()
        words[idx] = tmp
    return ' '.join(words)