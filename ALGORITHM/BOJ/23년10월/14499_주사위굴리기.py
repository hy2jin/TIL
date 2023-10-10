import sys
sys.stdin = open('input.txt')

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cube = { 'u': 1, 'f': 2, 'r': 3 }
cubeNum = [0] * 7
def moveCube(direc):
    u = cube['u']; f = cube['f']; r = cube['r'];
    if direc ==0:       # 동(오)
        cube['r'] = u; cube['u'] = 7 - r
    elif direc == 1:    # 서(왼)
        cube['u'] = r; cube['r'] = 7 - u
    elif direc == 2:    # 북(위)
        cube['u'] = f; cube['f'] = 7 - u
    else:               # 남(아래)
        cube['f'] = u; cube['u'] = 7 - f

DIR = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for order in input().split():
    d = int(order) - 1
    nx, ny = x + DIR[d][0], y + DIR[d][1]
    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        moveCube(d)
        print(cubeNum[cube['u']])
        if arr[x][y] == 0:
            arr[x][y] = cubeNum[7 - cube['u']]
        else:
            cubeNum[7 - cube['u']] = arr[x][y]
            arr[x][y] = 0
