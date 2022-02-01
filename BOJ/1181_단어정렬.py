# BOJ 1181 단어 정렬
'''
함정은 같은 단어가 여러 번 입력된 경우 한번만 출력한다는 것 -> set()를 이용함
'''
import sys
sys.stdin = open('input.txt')

lst = []
chk = set()
for i in range(int(input())):
    tmp = input()
    if tmp not in chk:
        chk.add(tmp)
        lst.append((len(tmp), tmp))
lst.sort()
for l in lst:
    print(l[1])