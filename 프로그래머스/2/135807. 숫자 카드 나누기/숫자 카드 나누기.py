import math
from functools import reduce

def solution(arrayA, arrayB):
    divisors_a = divisors(arrayA)
    divisors_b = divisors(arrayB)

    
    num_a = is_not_divisor(divisors_a, arrayB)
    num_b = is_not_divisor(divisors_b, arrayA)
    print(num_a , num_b)
    
    answer = max(num_a,num_b)
    return answer

def divisors(arr):
    gcd = reduce(math.gcd, arr)
    divisors = set()
    for i in range(1, int(gcd**0.5) + 1):
            if gcd % i == 0:
                divisors.add(i)
                divisors.add(gcd // i)
                
    return sorted(divisors)

def is_not_divisor(divisors, arr):
    result = 0
    for div in divisors:
        for num in arr:
            if num % div == 0:
                break
                
        else:
            result = max(result, div)
    return result