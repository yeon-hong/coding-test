from collections import Counter

def solution(participant, completion):
    answer = list((Counter(participant) - Counter(completion)).elements())[0]
    
    return answer