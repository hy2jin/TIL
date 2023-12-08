# BOJ 14244 트리 만들기
n, m = map(int, input().split())

for i in range(1, m+1):
    print(0, i)
for j in range(m, n-1):
    print(j, j+1)

# 6, 3으로 그림 그려보기
