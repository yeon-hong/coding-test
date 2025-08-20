def solution(elements):
    n = len(elements)
    arr = elements * 2
    prefix = [0] * (2*n + 1)

    # 누적합
    for i in range(1, 2*n+1):
        prefix[i] = prefix[i-1] + arr[i-1]

    sums = set()
    for length in range(1, n+1):
        for start in range(n):
            part_sum = prefix[start+length] - prefix[start]
            sums.add(part_sum)

    return len(sums)
