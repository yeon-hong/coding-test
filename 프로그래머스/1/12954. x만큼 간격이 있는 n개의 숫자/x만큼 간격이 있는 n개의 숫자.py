def solution(x, n):
    answer = []
    c=1
    
    while c <= n:
        answer.append(x*c)
        c+=1
    return answer