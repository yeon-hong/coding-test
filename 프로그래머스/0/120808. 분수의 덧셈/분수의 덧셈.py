import math

def solution(numer1, denom1, numer2, denom2):
    # 공통 분모
    lcm = denom1 * denom2 // math.gcd(denom1, denom2)
    
    # 분자 계산
    a1 = lcm // denom1
    a2 = lcm // denom2
    numer = a1 * numer1 + a2 * numer2
    
    # 기약분수 만들기
    g = math.gcd(numer, lcm)
    return [numer // g, lcm // g]
