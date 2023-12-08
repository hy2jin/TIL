def is_palin(word):
    l = len(word)//2
    for i in range(len(word)):
        if word[i] != word[-1-i]:
            return False
    return True

for _ in range(int(input())):
    word = input()
    i, j = 0, len(word)-1
    L = R = 0
    ans = 0
    while i <= j:
        if word[i] == word[j]:
            i += 1
            j -= 1
        elif is_palin(word[i+1:j+1]):
            ans = 1
            break
        elif is_palin(word[i:j]):
            ans = 1
            break
        else:
            ans = 2
            break
    print(ans)