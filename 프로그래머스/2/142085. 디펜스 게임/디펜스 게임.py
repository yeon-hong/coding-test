import heapq

def solution(n, k, enemy):
    answer = 0
    
    max_heap = []
    
    for e in enemy:
        n -= e
        heapq.heappush(max_heap, -e)

        if n < 0:  
            if k:
                biggest = -heapq.heappop(max_heap)  
                n += biggest
                k -= 1
            else:
                break
        answer += 1
        
    return answer