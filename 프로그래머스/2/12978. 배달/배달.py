import heapq
from collections import defaultdict

def solution(N, road, K):
    # 1. 그래프 생성
    graph = defaultdict(list)
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    # 2. 다익스트라 초기화
    distance = [float('inf')] * (N + 1)
    distance[1] = 0  # 1번 마을에서 출발
    heap = [(0, 1)]  # (소요시간, 현재마을)3
    0

    # 3. 다익스트라 실행
    while heap:                                             # heap이 비어있지 않은 동안 반복 (방문할 노드가 남아있음)
        cur_dist, cur_node = heapq.heappop(heap)            # 가장 짧은 거리의 노드를 꺼냄 (cur_dist: 현재까지 거리, cur_node: 현재 노드)

        if cur_dist > distance[cur_node]:                   # 이미 더 짧은 거리로 방문했으면 무시
            continue

        for neighbor, cost in graph[cur_node]:              # 현재 노드에 연결된 이웃 노드(neighbor)와 거리(cost)를 순회
            new_dist = cur_dist + cost                      # 이웃 노드까지 가는 누적 거리 계산

            if new_dist < distance[neighbor]:               # 계산된 거리가 기존 거리보다 짧으면 갱신
                distance[neighbor] = new_dist               # 최단 거리 테이블 갱신
                heapq.heappush(heap, (new_dist, neighbor))  # 새로운 거리 정보로 heap에 추가


    # 4. K시간 이하 배달 가능한 마을 수
    return sum(1 for d in distance if d <= K)
