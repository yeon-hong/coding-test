def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)  
    
    for e in emergency:
        rank = sorted_emergency.index(e) + 1
        answer.append(rank)
        
    return answer