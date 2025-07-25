from collections import deque

def solution(maps):
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
    to_lever = bfs(start, lever, maps)
    to_exit = bfs(lever, exit, maps)
    
    if to_lever == -1 or to_exit == -1:
        return -1
    else:
        return to_lever + to_exit

def bfs(start, end, maps):
    rows, cols = len(maps), len(maps[0])                          # 미로의 행과 열 개수 저장
    visited = [[False] * cols for _ in range(rows)]               # 방문 여부를 저장하는 2차원 리스트 초기화
    queue = deque()                                               # BFS 수행을 위한 큐 생성
    queue.append((start[0], start[1], 0))                         # 시작 좌표와 거리 0을 큐에 넣음
    visited[start[0]][start[1]] = True                            # 시작 좌표 방문 처리

    directions = [(-1,0), (1,0), (0,-1), (0,1)]                   # 상, 하, 좌, 우로 이동하기 위한 방향 벡터 리스트

    while queue:                                                  # 큐가 빌 때까지 반복
        x, y, distance = queue.popleft()                          # 큐에서 현재 위치와 누적 거리 꺼냄

        if (x, y) == end:                                         # 현재 위치가 목표 위치이면
            return distance                                       # 누적 거리(최단 거리) 반환

        for dx, dy in directions:                                 # 상하좌우 각 방향으로 이동 시도
            nx, ny = x + dx, y + dy                               # 다음 위치 계산

            if 0 <= nx < rows and 0 <= ny < cols:                 # 다음 위치가 미로 내부인지 확인
                if not visited[nx][ny] and maps[nx][ny] != 'X':   # 방문하지 않았고 벽이 아니라면
                    visited[nx][ny] = True                        # 방문 처리
                    queue.append((nx, ny, distance + 1))          # 다음 위치와 거리+1을 큐에 추가

    return -1                                                     # 목표 지점에 도달할 수 없을 경우 -1 반환
