def solution(n):
    if n <= 2:
        return n
    
    a, b = 1, 2  # f(1)=1, f(2)=2
    for _ in range(3, n+1):
        a, b = b, (a + b)
    
    return b % 1234567
