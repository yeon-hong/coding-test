def solution(triangle):
    # triangle 자체를 dp 테이블로 활용
    n = len(triangle)
    
    # 아래에서 두 번째 줄부터 올라오기
    for i in range(n-2, -1, -1):          # 마지막 줄 바로 위에서 시작
        for j in range(len(triangle[i])): # 해당 줄의 원소들
            # 현재 값 + (아래 두 값 중 큰 값)
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    # 꼭대기까지 갱신되면 triangle[0][0] 이 최대합
    return triangle[0][0]
