before = input()
L = len(before)
i = 1
after = before[0]
if '_' in before:
    # cpp -> java
    while i < L:
        if before[i] == '_':
            after += before[i+1].upper()
            i += 2
        else:
            after += before[i]
            i += 1
else:
    # java -> cpp
    while i < L:
        if before[i].upper() == before[i]:
            pass