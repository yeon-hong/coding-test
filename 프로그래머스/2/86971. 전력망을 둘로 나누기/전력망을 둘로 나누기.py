def solution(n, wires):
    def dfs(start, graph, visited):
        count = 1
        visited[start] = True
        for neighbor in graph[start]:
            
            if not visited[neighbor]:
                count += dfs(neighbor, graph, visited)
        return count

    answer = n
    for i in range(len(wires)):
        # 간선 하나 제거
        temp_wires = wires[:i] + wires[i+1:]
        
        # 그래프 만들기
        graph = [[] for _ in range(n+1)]

        for a, b in temp_wires:

            graph[a].append(b)
            graph[b].append(a)

        # DFS로 한쪽 트리 개수 세기
        visited = [False] * (n+1)
        count = dfs(1, graph, visited)
        answer = min(answer, abs(n - 2*count))


    return answer
