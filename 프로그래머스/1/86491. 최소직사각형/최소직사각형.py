def solution(sizes):
    answer = 0
    l=[]
    s=[]
    for x, y in sizes:
        l.append(max(x,y))
        s.append(min(x,y))

    answer = max(l)*max(s)
    return answer