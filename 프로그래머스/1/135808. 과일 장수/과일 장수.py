def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    box = [score[i:i+m] for i in range(0, len(score) - len(score) % m, m)]

    for i in box:
        answer += i[m-1]*m
    return answer