# BOJ 4949 균형잡힌 세상
import sys
sys.stdin = open('input.txt')
dic = {'(': ')', '[': ']'}
while True:
    string = input()
    stack = []
    if string == '.':
        break
    ans = 'no'
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        if s == ')' or s == ']':
            if not stack:
                break
            p = stack.pop()
            if s != dic[p]:
                break
        if s == '.':
            if stack:
                break
    else:
        ans = 'yes'
    print(ans)