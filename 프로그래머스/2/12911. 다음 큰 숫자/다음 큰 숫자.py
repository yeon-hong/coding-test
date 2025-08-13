from collections import Counter


def solution(n):
    cn = Counter(bin(n)[2:])
    n += 1
    
    while True:
        ck = Counter(bin(n)[2:])
        if ck['1'] == cn['1']:
            break
        n += 1
    return n