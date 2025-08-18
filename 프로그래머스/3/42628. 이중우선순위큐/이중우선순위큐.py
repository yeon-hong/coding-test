import heapq

def solution(operations):
    answer = [0,0]
    hq = []
    
    for s in operations:
        command, num = s.split(' ')
        if command == 'I':
            heapq.heappush(hq, int(num))
        
        elif command == 'D':
            if num == '1' and hq:
                hq = list(hq)
                hq.remove(max(hq))
                heapq.heapify(hq)
                
            elif num == '-1'and hq: 
                heapq.heappop(hq)
    if hq:
        answer[0] = max(hq)
        answer[1] = min(hq)
    return answer