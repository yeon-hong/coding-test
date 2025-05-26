def solution(answers):
    answer = []

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1 = c2 = c3 =0
    
    for idx, ans in enumerate(answers):
        if ans == p1[idx % len(p1)]:
            c1 += 1
        if ans == p2[idx % len(p2)]:
            c2 += 1
        if ans == p3[idx % len(p3)]:
            c3 += 1

    max_score = max(c1, c2, c3)
    
    if c1 == max_score:
        answer.append(1)
    if c2 == max_score:
        answer.append(2)
    if c3 == max_score:
        answer.append(3)
        
    return answer