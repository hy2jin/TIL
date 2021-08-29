# BOJ 10158 개미
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x = (2*w) - (p+t)%(2*w) if (p+t)%(2*w) > w else (p+t)%(2*w)
y = (2*h) - (q+t)%(2*h) if (q+t)%(2*h) > h else (q+t)%(2*h)
print(x, y)