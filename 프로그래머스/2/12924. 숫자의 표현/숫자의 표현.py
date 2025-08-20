def solution(n):
    count = 0
    k = 1
    while k * (k - 1) // 2 < n:  # 항 개수 k가 너무 크면 종료
        if (n - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1
    return count