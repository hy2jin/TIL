def solution(sizes):
    large = small = 0
    for size in sizes:
        large = max(large, max(size))
        small = max(small, min(size))
    return large * small