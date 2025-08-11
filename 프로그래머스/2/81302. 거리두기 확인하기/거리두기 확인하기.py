from collections import deque


def solution(places):
    answer = []
    for place in places:
        valid = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    bfs_result = bfs(i, j, place)
                    if bfs_result == False:
                        valid = 0
                        break
                        
                        
                if not valid:
                    break
        answer.append(valid)
    return answer


def bfs(x, y, place):
    visited = [[False]*5 for _ in range(5)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        cx, cy, dist = queue.popleft()
        if 0 < dist <= 2 and place[cx][cy] == 'P':
            return False
        if dist < 2:
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if place[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist+1))
    return True
