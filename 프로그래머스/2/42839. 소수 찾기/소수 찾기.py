from itertools import permutations

def solution(numbers):
    answer = 0
    combination = set()
    
    
    for r in range(1, len(numbers)+1):
        for p in permutations(numbers, r):
            combination.add(int(''.join(p)))
    
    for num in combination:
        if num < 2:
            continue
            
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            answer +=1        
    return answer