def solution(keymap, targets):
    answer = []
    for string in targets:
        count = 0 
        for char in string:
            min_press = float('inf')
            for i in keymap:
                if char in i:
                    min_press = min(min_press, i.index(char)+1)
                    
            if min_press == float('inf'):
                count = -1
                break
            count += min_press
        answer.append(count)
    return answer