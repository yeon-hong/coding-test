import math

def solution(arr):
    # 배열 첫 번째 수를 초기 LCM으로 설정
    lcm_value = arr[0]
    
    # 배열의 나머지 수들과 차례대로 LCM 계산
    for num in arr[1:]:
        lcm_value = lcm_value * num // math.gcd(lcm_value, num)
    
    return lcm_value
