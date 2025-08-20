def solution(s):
    s = s.split(' ')
    
    for i, st in enumerate(s):
        if st:  # 빈 문자열이 아니면
            s[i] = st[0].upper() + st[1:].lower()
            
    answer = ' '.join(s)
    return answer