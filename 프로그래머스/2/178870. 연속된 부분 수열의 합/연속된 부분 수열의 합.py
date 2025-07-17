def solution(sequence, k):
    n = len(sequence)
    start = 0
    end = 0
    total = sequence[0]
    answer = []

    while end < n:
        if total < k:
            end += 1
            
            if end < n:
                total += sequence[end]
                
        elif total > k:
            total -= sequence[start]
            start += 1
            
        else:  
            if not answer or (end - start) < (answer[1] - answer[0]):
                answer = [start, end]
            total -= sequence[start]
            start += 1

    return answer

