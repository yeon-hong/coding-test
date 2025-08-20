from collections import deque

def solution(priorities, location):
    dq = deque([(p, idx) for idx, p in enumerate(priorities)])
    count = 1

    while dq:
        p, idx = dq.popleft()

        if any(p < other_p for other_p, _ in dq):
            dq.append((p, idx))
        else:

            if idx == location:  
                break
            count += 1   
    return count
