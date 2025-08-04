def solution(rows, columns, queries):
    answer = []
    matrix = [[x + columns * i for x in range(1, columns + 1)] for i in range(rows)]

    for s in queries:
        x1, y1, x2, y2 = [x - 1 for x in s]
        path = []

        for y in range(y1, y2 + 1):
            path.append((x1, y))
        for x in range(x1 + 1, x2 + 1):
            path.append((x, y2))
        for y in range(y2 - 1, y1 - 1, -1):
            path.append((x2, y))
        for x in range(x2 - 1, x1, -1):
            path.append((x, y1))


        values = [matrix[x][y] for x, y in path]
        

        rotated = [values[-1]] + values[:-1]

        for (x, y), val in zip(path, rotated):
            matrix[x][y] = val


        answer.append(min(rotated))
    
    return answer
