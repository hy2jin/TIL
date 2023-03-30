def solution(numbers, hand):
    ans = ''                        # 답
    lnow, rnow = (3, 0), (3, 2)     # 현재 손가락 위치
    dic = {2: 0, 5: 1, 8: 2, 0: 3}  # 2580의 행

    for n in numbers:
        if n in [1, 4, 7]:
            ans += 'L'                  # 왼손
            if n == 1: lnow = (0, 0)    # 손가락 위치
            elif n == 4: lnow = (1, 0)
            else: lnow = (2, 0)
        elif n in [3, 6, 9]:
            ans += 'R'                  # 오른손
            if n == 3: rnow = (0, 2)    # 손가락 위치
            elif n == 6: rnow = (1, 2)
            else: rnow = (2, 2)
        else:
            l = abs(1-lnow[1]) + abs(dic[n]-lnow[0])    # 왼손거리
            r = abs(1-rnow[1]) + abs(dic[n]-rnow[0])    # 오른손거리
            if l == r:
                if hand == 'left': ans += 'L'
                else: ans += 'R'
            elif l < r:
                ans += 'L'
            else:
                ans += 'R'
            if ans[-1] == 'R':
                rnow = (dic[n], 1)
            else:
                lnow = (dic[n], 1)
    return ans