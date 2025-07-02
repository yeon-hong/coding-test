from collections import Counter

def solution(X, Y):
    
    count_x = Counter(X)
    count_y = Counter(Y)
    
    temp = []
    for key in count_x:
        
        if key in count_y:
        
            temp.append(key * min(count_x[key],count_y[key]))
    
    temp = sorted(temp, reverse=True)
    answer = ''.join(temp)
    if not temp:
        return "-1"
    
    if set(answer) == {'0'}:
        return "0"
    
    return answer