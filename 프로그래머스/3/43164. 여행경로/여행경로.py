def solution(tickets):
    answer = []
    tickets.sort()

    visit = [False] * len(tickets)

    def dfs(path):
        if len(path) == len(tickets) + 1:
            nonlocal answer
            answer = path[:]
            return True

        last = path[-1]
        for i, ticket in enumerate(tickets):
            if not visit[i] and ticket[0] == last:
                visit[i] = True
                if dfs(path + [ticket[1]]):
                    return True
                else:
                    visit[i] = False

        return False

    dfs(["ICN"])
    return answer
