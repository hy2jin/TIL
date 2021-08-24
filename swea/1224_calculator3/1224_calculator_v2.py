'''
함수로 만들어서 사용
'''

import sys
sys.stdin = open('input.txt')


def infix_to_postfix(infix):
    stack = []          # 우선순위 확인
    postfix = ''        # 후위표기법 담을 변수

    for w in infix:
        if w.isdigit():                 # 숫자면 postfix
            postfix += w
        elif not stack or w == '(':     # 스택이 비었거나 여는 괄호면 stack
            stack.append(w)

        elif w == '*' or w == '/':      # */ 보다 우선순위가 높거나 같은건 */
            while stack and stack[-1] in '*/':
                postfix += stack.pop()
            stack.append(w)
        elif w == '+' or w == '-':      # +- 보다 우선순위가 높거나 같은건 */+- ==> 여는괄호 빼고 전부
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.append(w)

        else:       # 닫는 괄호는 버리고 / 여는 괄호가 나올때까지 pop 하고 / 여는괄호도 버림
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

    while stack:
        postfix += stack.pop()
    return postfix


def postfix_cal(postfix):
    stack = []
    for p in postfix:
        if p.isdigit():         # 숫자
            stack.append(int(p))
        else:                   # 연산자
            b = stack.pop()
            a = stack.pop()
            if p == '*':
                stack.append(a * b)
            elif p == '/':
                stack.append(a // b)
            elif p == '+':
                stack.append(a + b)
            elif p == '-':
                stack.append(a - b)
    return stack[0]


for tc in range(1, 11):
    n = int(input())
    postfix = infix_to_postfix(input())
    ans = postfix_cal(postfix)
    print('#{} {}'.format(tc, ans))
