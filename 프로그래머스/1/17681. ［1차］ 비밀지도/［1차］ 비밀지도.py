def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        a = format(i | j, f'0{n}b')
        a = a.replace("1","#")
        a = a.replace("0"," ")
        answer.append(a)

    return answer