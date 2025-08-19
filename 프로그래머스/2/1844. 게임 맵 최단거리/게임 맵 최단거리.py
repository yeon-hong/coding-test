from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visit = [[False] * m for _ in range(n)]
    d = [(1,0),(0,1),(0,-1),(-1,0)]
    
    queue = deque([(0, 0, 1)])  # (x, y, 이동거리)
    visit[0][0] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 목표 도착
        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in d:
            rx, ry = x + dx, y + dy
            if 0 <= rx < n and 0 <= ry < m:  # 범위 체크
                if not visit[rx][ry] and maps[rx][ry] == 1:
                    visit[rx][ry] = True
                    queue.append((rx, ry, dist+1))
    
    return -1  # 도달 불가능한 경우
