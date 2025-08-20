from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    count_list = sorted(count.values(), reverse=True)
    
    for v in count_list:
        k -= v
        answer += 1
        if k <= 0:
            break
    
    return answer