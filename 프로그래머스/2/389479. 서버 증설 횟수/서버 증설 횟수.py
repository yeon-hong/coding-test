def solution(players, m, k):
    answer = 0
    sever = 0
    times = {}
    for i in range(len(players)):
        users = players[i]
        
        if i in times:
            sever -= times[i]
            
        mul = users//m
        if mul > sever:
            c = mul - sever
            answer += c
            sever += c
            times[i+k] = c

    return answer  