from collections import deque

def solution(begin, target, words):
    dq = deque([(begin, 0)])  # (현재 단어, 단계)
    visited = set([begin])
    answer = 0
    while dq:
        word, step = dq.popleft()
        
        if word == target:
            answer = step  # 발견 시 step 저장
            break          # while문 탈출
        
        for w in words:
            if sum(c1 == c2 for c1, c2 in zip(word, w)) == len(word)-1:
                if w not in visited:
                    visited.add(w)
                    dq.append((w, step+1))
    
    return answer
