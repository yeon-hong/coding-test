def solution(n, m, section):
    answer = 0
    start = 0
    for s in section:
        if s > start:
            answer += 1
            start = s + m - 1
    return answer
