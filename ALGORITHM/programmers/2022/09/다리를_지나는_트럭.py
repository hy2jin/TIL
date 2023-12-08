from collections import deque

def solution(bridge_length, weight, truck_weights):
    ans = 0
    bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    total = 0
    
    while bridge:
        ans += 1
        total -= bridge.popleft()
        if waiting:
            if total + waiting[0] <= weight:
                total += waiting[0]
                bridge.append(waiting.popleft())
            else:
                bridge.append(0)
    return ans