from itertools import product

def solution(word):
    answer = 0
    lst =['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range (1, len(lst)+1):
        for p in product(lst, repeat=i):
            words.append("".join(p))
    words.sort()
    
    for i, w in enumerate(words):
        if w == word:
            answer = i+1
            break
    return answer