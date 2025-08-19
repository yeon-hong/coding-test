def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    
    # 시작점
    dp[0][0] = 1
    
    # 물에 잠긴 좌표 표시
    puddles = set((y-1, x-1) for x, y in puddles)
    
    for i in range(n):
        for j in range(m):
            if (i, j) in puddles:  # 웅덩이면 경로 불가
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            #dp[i][j] %= 1000000007
    
    return dp[n-1][m-1] % 1000000007
