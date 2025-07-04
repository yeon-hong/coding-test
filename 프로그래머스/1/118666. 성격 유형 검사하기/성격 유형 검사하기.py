def solution(survey, choices):
    answer = ''
    choice_score = {
    1: 3,   
    2: 2,   
    3: 1,   
    4: 0,   
    5: 1,   
    6: 2,   
    7: 3    
    }
    
    Personality_type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}  
    
    for types, choice in zip(survey, choices):
        
        if choice < 4:  
            Personality_type[types[0]] += choice_score[choice]
        elif choice > 4:  
            Personality_type[types[1]] += choice_score[choice]
    
    items = list(Personality_type.items())
    
    for i in range(0, len(items), 2):
        (k1, v1) = items[i]
        (k2, v2) = items[i+1]
        if v1 < v2:
            answer += k2
        else:
            answer += k1
    return answer