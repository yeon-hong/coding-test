def solution(n):
    answer = ''
    while n > 0:
        n -= 1

        n, mod = divmod(n, 3)

        answer = '124'[mod] + answer

    return answer