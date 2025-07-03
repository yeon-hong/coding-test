def solution(board, moves):
    answer = 0
    result = []
    top = [-1]*len(board)
    for col in range(len(board[0])): 
        for row in range(len(board)):  
            if board[row][col] != 0:
                top[col] = row
                break
    
    for i in moves:
        if top[i-1] != -1:
            result.append(board[top[i-1]][i-1])
            if top[i-1] + 1 < len(board):
                top[i-1] += 1
            else:
                top[i-1] = -1

        while len(result) >= 2 and result[-1] == result[-2]:
            answer += 2
            result=result[:-2]

    return answer