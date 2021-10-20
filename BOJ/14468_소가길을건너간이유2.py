# BOJ 14468 소가 길을 건너간 이유2
import sys
sys.stdin = open('input.txt')

string = input()
# ABCCABDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ
idx = [[] for _ in range(26)]
for i in range(52):
    s = string[i]
    idx[ord(s)-65].append(i)
# print(idx)
cnt = 0
for i in range(25):
    left = idx[i]
    for j in range(i+1, 26):
        right = idx[j]
        if left[0] < right[0] < left[1] < right[1]:
            cnt += 1
        elif right[0] < left[0] < right[1] < left[1]:
            cnt += 1
print(cnt)
