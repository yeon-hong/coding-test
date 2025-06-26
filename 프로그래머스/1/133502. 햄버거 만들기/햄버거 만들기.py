def solution(ingredient):
    answer = 0
    result = []
    
    for x in ingredient:
        result.append(x)

        if len(result) >= 4 and result[-4:] == [1, 2, 3, 1]:
            del result[-4:] 
            answer += 1
            
    return answer