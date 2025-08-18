def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n):
        t = prices[i]
        s = 1
        for j in range(i+1,n):
            if t > prices[j] or j==n-1:
                answer.append(s)
                break
            s+=1
    answer.append(0)        
    return answer