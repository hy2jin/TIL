# BOJ 1259 팰린드롬수
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    N = input().rstrip()
    if N == '0': break
    if N == N[::-1]: print('yes')
    else: print('no')