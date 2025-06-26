def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    intersection = lost_set & reserve_set
    lost_set -= intersection
    reserve_set -= intersection

    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
            
    answer = n - len(lost_set)
    return answer