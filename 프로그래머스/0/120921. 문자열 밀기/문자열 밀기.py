def solution(A, B):
    answer = 0
    while A != B:
        if answer > len(B):
            answer = -1
            break
        A = A[-1] + A[:-1]
        answer += 1
    return answer