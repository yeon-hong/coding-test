from collections import deque 

def solution(maps):                                    
    n, m = len(maps), len(maps[0])                       # 지도 행(n), 열(m) 크기 구하기
    visited = [[False] * m for _ in range(n)]            # 방문 여부를 체크할 2차원 배열 초기화
    result = []                                          # 결과를 담을 리스트 초기화

    for i in range(n):                                   # 지도 전체 순회
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':  # 방문하지 않았고 바다가 아닌 경우
                result.append(bfs(i, j, maps, visited))  # BFS 탐색 결과를 결과 리스트에 추가

    return sorted(result) if result else [-1]            # 결과가 있으면 오름차순 정렬 후 반환, 없으면 [-1]

def bfs(x, y, maps, visited):
    n, m = len(maps), len(maps[0])                       # 지도 크기 저장
    queue = deque()                                      # BFS 탐색용 큐 초기화
    queue.append((x, y))                                 # 시작 좌표 큐에 추가
    visited[x][y] = True                                 # 시작 좌표 방문 처리
    total_food = int(maps[x][y])                         # 현재 위치의 식량량으로 초기화

    while queue:                                         # 큐가 빌 때까지 반복
        cx, cy = queue.popleft()                         # 큐에서 현재 좌표 꺼내기

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:    # 상하좌우 네 방향으로 탐색
            nx, ny = cx + dx, cy + dy                    # 새로운 좌표 계산

            if 0 <= nx < n and 0 <= ny < m:                      # 지도 범위 내에 있고
                if not visited[nx][ny] and maps[nx][ny] != 'X':  # 방문하지 않았으며 땅인 경우
                    visited[nx][ny] = True                       # 방문 처리
                    total_food += int(maps[nx][ny])              # 식량량 누적
                    queue.append((nx, ny))                       # 다음 탐색을 위해 큐에 추가

    return total_food 
