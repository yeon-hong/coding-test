def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        a = format(i | j, f'0{n}b')
        b = ""
        for k in a:
            b += "#" if k == "1" else " "
        answer.append(b)

    return answer