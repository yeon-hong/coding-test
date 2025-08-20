def solution(n):
    dp = [0, 1] + [0] * (n - 1) # 배열 채우기
    for i in range(2, n + 1): # i = 2부터 n까지 반복하면서 계싼
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567