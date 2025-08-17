from collections import deque

def solution(priorities, location):
    dq = deque([(p, idx) for idx, p in enumerate(priorities)])
    count = 0

    while dq:
        p, idx = dq.popleft()

        if any(p < other_p for other_p, _ in dq):
            dq.append((p, idx))
        else:

            count += 1
            if idx == location:  
                break
                
    return count
