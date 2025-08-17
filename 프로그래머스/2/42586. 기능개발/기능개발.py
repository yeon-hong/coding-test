def solution(progresses, speeds):
    answer = []
    arr = [(100 - p+s - 1)//s for p, s in zip(progresses, speeds)]

    m = arr[0] 
    count = 1

    for day in arr[1:]:
        if day <= m:

            count += 1
        else:

            answer.append(count)
            m = day
            count = 1


    answer.append(count)
        
    return answer