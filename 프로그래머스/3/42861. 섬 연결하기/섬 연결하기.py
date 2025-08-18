def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[b] = a
            return True
        return False
    
    answer = 0
    for s, e, v in costs:
        if union(s, e):
            answer += v
    return answer