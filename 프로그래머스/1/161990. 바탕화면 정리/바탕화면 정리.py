def solution(wallpaper):
    
    files = []
    
    for col in range(len(wallpaper)): 
        for row in range(len(wallpaper[0])):  
            if wallpaper[col][row] == '#':
                files.append((col,row))
                
    print(files)
    x_list, y_list = zip(*files) 

    answer =[min(x_list), min(y_list), max(x_list) + 1, max(y_list) + 1]
    return answer