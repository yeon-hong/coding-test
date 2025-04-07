def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        time = schedules[i] + 10
        if time % 100 >= 60:
            time += 40
        valid = True
        for j in range(7):
            weekday = (startday - 1 + j) % 7 + 1
            if weekday >= 6: 
                continue
            if timelogs[i][j] > time:
                valid = False
                break
        if valid:
            answer += 1
    return answer
