import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            break
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)

        heapq.heappush(scoville, f+s*2)
        answer += 1
        
    return answer