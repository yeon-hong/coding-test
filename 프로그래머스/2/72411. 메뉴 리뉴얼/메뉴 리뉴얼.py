from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for c in course:
        combs = []
        for order in orders:
            order = ''.join(sorted(order)) 
            combs += combinations(order, c)  
        
        counter = Counter(combs)
        if not counter:
            continue
        
        max_count = max(counter.values())
        if max_count < 2:
            continue
        
        for menu, cnt in counter.items():
            
            if cnt == max_count:
                
                result.append(''.join(menu))

    return sorted(result)