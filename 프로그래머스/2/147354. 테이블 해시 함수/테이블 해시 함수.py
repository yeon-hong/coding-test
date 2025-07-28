def solution(data, col, row_begin, row_end):
    answer = 0
    data_sorted = sorted(data, key=lambda x: (x[col-1], -x[0]))
    # print(data_sorted)
    

    for i in range(row_begin, row_end + 1):
        row = data_sorted[i - 1]
        row_sum = sum(x % i for x in row)
        answer ^= row_sum
        
    return answer