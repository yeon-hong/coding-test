from collections import Counter


def solution(s):
    
    c = 0
    z = 0
    while s != '1':
        counter = Counter(s)
        l = counter['1']
        z += counter['0']
        
        s = bin(l)[2:]
        c += 1
    answer = [c, z]
    return answer