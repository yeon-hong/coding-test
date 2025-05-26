def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 2 if j != i // j else 1
                
        if count > limit:
            count = power
            
        answer +=count
        
    return answer