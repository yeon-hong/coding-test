def solution(dartResult):
    answer = 0
    scores = []
    i = 0
    while i < len(dartResult):
        
        if dartResult[i] == '1' and i+1 < len(dartResult) and dartResult[i+1] == '0':
            num = 10
            i += 2
        else:
            num = int(dartResult[i])
            i += 1

        bonus = dartResult[i]
        if bonus == 'S':
            num **= 1
        elif bonus == 'D':
            num **= 2
        elif bonus == 'T':
            num **= 3
        i += 1


        if i < len(dartResult) and dartResult[i] in ['*', '#']:
            if dartResult[i] == '*':
                num *= 2
                if scores:
                    scores[-1] *= 2
            elif dartResult[i] == '#':
                num *= -1
            i += 1

        scores.append(num)

    print(sum(scores))
    return sum(scores)