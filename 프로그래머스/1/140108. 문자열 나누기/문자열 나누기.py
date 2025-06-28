def solution(s):
    answer = 1
    count_x = 0
    count_y = 0
    for i in range(len(s)-1):

        if i == 0:
            x = s[i]
            count_x += 1
            print(x)
            continue
            
        if s[i] == x:
            count_x += 1
            
        
        else:
            count_y += 1
            if count_x == count_y:
                print(i, count_x)
                answer += 1
                x = s[i+1]
                count_x = 0
                count_y = 0
                print(x)
            
    return answer