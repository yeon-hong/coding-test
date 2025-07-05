def solution(numbers, hand):
    answer = ''
    
    keypad =[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,1)]
    l = (3,0)
    r = (3,2)
    for num in numbers:
        target = keypad[num-1]
        if num in [1,4,7]:
            l = target
            answer += 'L'
        elif num in [3,6,9]:
            r = target
            answer += 'R'
        else:
            l_distance = abs(l[0] - target[0]) + abs(l[1] - target[1])
            r_distance = abs(r[0] - target[0]) + abs(r[1] - target[1])
            if l_distance < r_distance:
                answer += 'L'
                l = target
            elif l_distance > r_distance:
                answer += 'R'
                r = target
            elif l_distance == r_distance:
                if hand == 'right':
                    answer += 'R'
                    r = target
                else:
                    answer += 'L'
                    l = target
    return answer