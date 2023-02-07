string = input()
L = len(string)

def ispal(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

if string == string[0] * L:
    print(-1)
elif ispal(string):
    print(L - 1)
else:
    print(L)