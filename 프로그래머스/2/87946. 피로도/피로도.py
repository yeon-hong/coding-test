from itertools import permutations

def solution(k, dungeons):
    answer = -1
    seq_list = []
    for i in range(1, len(dungeons)+1):
        for p in permutations(dungeons, i):
            seq_list.append(tuple(map(tuple, p)))

    seq_list.sort(key=lambda x: len(x), reverse=True)

    for s in seq_list:
        n=k
        for m, c in s:
            if n >= m:
                n = n-c

            else:
                break
        else:
            answer = len(s)
            break
            
    return answer