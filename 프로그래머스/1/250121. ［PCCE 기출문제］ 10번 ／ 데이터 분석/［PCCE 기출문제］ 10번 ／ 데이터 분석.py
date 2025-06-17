def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = { "code":0, "date":1, "maximum":2, "remain":3 }
    idx1, idx2 = dic[ext], dic[sort_by]
    
    for i in data:
        if i[idx1] < val_ext:
                answer.append(i)
    print(answer)
    answer = sorted(answer, key=lambda x: x[idx2])
                
    return answer