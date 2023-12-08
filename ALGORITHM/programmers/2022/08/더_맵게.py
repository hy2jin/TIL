from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        try:
            a = heappop(scoville)
            b = heappop(scoville)
            heappush(scoville, a + (b * 2))
            cnt += 1
        except:
            return -1
    return cnt