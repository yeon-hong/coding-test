def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            value = photo[i][j]
            if value in name:
                index = name.index(value)
                sum += yearning[index]
        answer.append(sum)
    return answer