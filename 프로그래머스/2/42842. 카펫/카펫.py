def solution(brown, yellow):
    answer = []
    n = brown//2
    
    for i in range(1, n//2 +1):
        j = n-i

        for x in range(1, int(yellow**0.5)+1):
            if yellow % x != 0:  # 나누어떨어지지 않으면 패스
                continue
                
            y = yellow//x
            
            if j == y+2 and x==i:
                answer+=[j,i+2]

    return answer