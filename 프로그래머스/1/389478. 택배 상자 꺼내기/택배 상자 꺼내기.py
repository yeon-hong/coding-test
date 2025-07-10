def solution(n, w, num):
    answer = 0
    boxs = []
    temp = []
    reverse = False
    idx = -1
    for i in range(1,n+1):
        if reverse:
            temp.insert(0,i)
        else:
            temp.append(i)
            
        if len(temp) == w:
            if num in temp:
                idx = temp.index(num)
            if idx != -1:
                answer += 1 
            boxs.insert(0,temp)
            temp = []
            reverse = not reverse

    if temp:
        boxs.insert(0,temp)
        if reverse:
            if len(temp) >= w - idx:
                answer += 1 
            
        else:
            if len(temp) >= idx + 1:
                answer += 1 
    
    return answer