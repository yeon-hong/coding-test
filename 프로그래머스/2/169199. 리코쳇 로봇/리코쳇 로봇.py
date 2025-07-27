from collections import deque

def solution(board):
    n, m = len(board), len(board[0])                                 # 보드의 행, 열 크기
    visited = [[False]*m for _ in range(n)]                          # 방문 여부를 저장할 2차원 배열
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]                             # 상, 하, 좌, 우 방향 벡터

    # 시작점(R)과 목표점(G) 찾기
    for i in range(n):                                              
        for j in range(m):
            if board[i][j] == 'R': start = (i, j)                    # 시작 위치 저장
            if board[i][j] == 'G': goal = (i, j)                     # 목표 위치 저장

    q = deque()                                                      # BFS를 위한 큐
    q.append((start[0], start[1], 0))                                # (행, 열, 이동횟수)
    visited[start[0]][start[1]] = True                               # 시작 위치 방문 처리
    
    while q:
        x, y, cnt = q.popleft()                                      # 현재 위치와 이동 횟수

        if (x, y) == goal:
            return cnt                                               # 목표에 도달하면 이동 횟수 반환

        for dx, dy in dirs:                                          # 4방향 탐색
            nx, ny = x, y

            # 벽 또는 장애물에 부딪힐 때까지 계속 이동
            while 0 <= nx+dx < n and 0 <= ny+dy < m and board[nx+dx][ny+dy] != 'D':
                nx += dx
                ny += dy

            if not visited[nx][ny]:                                  # 아직 방문하지 않았다면
                visited[nx][ny] = True                               # 방문 처리
                q.append((nx, ny, cnt+1))                            # 큐에 다음 위치와 이동 횟수 추가

    return -1                                                        # 목표에 도달할 수 없는 경우
