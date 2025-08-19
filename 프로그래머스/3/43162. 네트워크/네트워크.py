def solution(n, computers):
    visit = [False] * n
    answer = 0
    
    def dfs(v):
        visit[v] = True
        for nxt in range(n):
            if computers[v][nxt] == 1 and not visit[nxt]:
                dfs(nxt)
    
    for i in range(n):
        if not visit[i]:
            dfs(i)
            answer += 1

    return answer
