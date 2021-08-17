import sys
sys.stdin = open('input.txt')
for tc in range(10): # 10개의 테스트케이스
    N = int(input())
    B = list(map(int, input().split())) # B : buildings
    view = 0

    # 건물은 idx가 2부터 N-3인 곳까지 있음
    for i in range(2, N-2):
        # 왼쪽 두개와 오른쪽 두개의 높이를 비교
        left2, left1, right2, right1 = B[i] - B[i-2], B[i] - B[i-1], B[i] - B[i+2], B[i] - B[i+1]
        # 꼭대기층 view 좋으면 +1하고 아래층 view 확인
        while True:
            if left1 > 0 and right1 > 0 and left2 > 0 and right2 > 0:
                view += 1
                left2 -= 1
                left1 -= 1
                right2 -= 1
                right1 -= 1
            else: break # view 안좋은층 있으면 다음 건물로 넘어감
    print('#{} {}'.format(tc+1, view))