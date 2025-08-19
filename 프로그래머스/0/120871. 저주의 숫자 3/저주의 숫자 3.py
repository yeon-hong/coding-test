def solution(n):
    count = 0
    num = 1
    while True:
        if num % 3 != 0 and '3' not in str(num):
            count += 1
        if count == n:
            return num
        num += 1
    return num