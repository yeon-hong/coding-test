import math

def solution(a, b):
 # 기약분수로 만들기
    g = math.gcd(a, b)
    b //= g
    
    # 2와 5를 제외한 모든 소인수 제거
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    # 남은 수가 1이면 유한소수, 아니면 무한소수
    if b == 1:
        return 1   # 유한소수
    else:
        return 2  # 무한소수