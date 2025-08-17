def solution(arr):
    answer = []
    temp = -1
    for n in arr:
        if n != temp:
            answer.append(n)
        temp = n
    return answer