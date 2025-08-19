def solution(lines):
    # -100 ~ 100 범위 내 좌표를 표시할 수 있는 배열
    arr = [0] * 201  # index 0 → 좌표 -100, index 200 → 좌표 100
    
    for s, e in lines:
        for i in range(s, e):  # [s, e) 구간
            arr[i + 100] += 1  # 좌표를 +100 해서 index 맞춤
    
    answer = 0
    for v in arr:
        if v >= 2:  # 두 개 이상 선분이 덮고 있으면 겹치는 부분
            answer += 1
    
    return answer
