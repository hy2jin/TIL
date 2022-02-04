# BOJ 2869 달팽이는 올라가고 싶다
'''
달팽이가 정상에 도착하면 미끄러지지 않는 조건이 중요!
-> H / (up-down)이 아닌 (H-down) / (up-down) 로 계산하고
남은 높이가 있으면 하루를 더해준다
'''
up, down, H = map(int, input().split())
d, h = divmod(H-down, up-down)
if h: d += 1
print(d)