def solution(park, routes):
    obstacle = []
    
    move = {
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1)
    } 
    
    for row in range(len(park)):
        for col in range(len(park[0])):
            if park[row][col] == 'S':
                start = (row, col)
            elif park[row][col] == 'X':
                obstacle.append((row, col))
                
    
    for route in routes:
        can_move = True
        direction, steps = route.split()
        coord = move[direction]
        temp = start
        for check in range(int(steps)):
            moving = tuple(x + y for x, y in zip(temp, coord))
            if (moving in obstacle or
                moving[0] < 0 or moving[0] >= len(park) or
                moving[1] < 0 or moving[1] >= len(park[0])):
                can_move = False
                break
            else:
                temp = tuple(x + y for x, y in zip(temp, coord))
        if can_move:
            start = temp
            
    answer = list(start)
    return answer