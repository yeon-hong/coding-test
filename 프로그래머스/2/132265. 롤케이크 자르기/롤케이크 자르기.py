def solution(topping):
    answer = 0
    left_set = set()
    right_count = {}
    
    # 오른쪽 부분의 각 토핑 개수 계산
    for t in topping:
        right_count[t] = right_count.get(t, 0) + 1
    
    for i in range(len(topping) - 1):
        # 왼쪽에 토핑 추가
        left_set.add(topping[i])
        
        # 오른쪽에서 토핑 제거
        right_count[topping[i]] -= 1
        if right_count[topping[i]] == 0:
            del right_count[topping[i]]
        
        # 양쪽의 고유 토핑 수가 같으면 카운트
        if len(left_set) == len(right_count):
            answer += 1
            
    return answer