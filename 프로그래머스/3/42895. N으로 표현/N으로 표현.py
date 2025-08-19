def solution(N, number):
    if N == number:                          # N 자체가 number면 바로 1 반환
        return 1

    dp = [set() for _ in range(9)]          # N 사용 횟수 1~8까지 저장할 집합 생성
    for i in range(1, 9):                   # 1~8번 N 사용
        dp[i].add(int(str(N) * i))          # N을 이어 붙여 만든 수 추가 (ex: 5, 55, 555)
        for j in range(1, i):               # i번 사용을 j와 i-j로 나누어 계산
            for x in dp[j]:                 # j번 사용해서 만든 수
                for y in dp[i-j]:           # i-j번 사용해서 만든 수
                    dp[i].add(x + y)        # 덧셈 결과 추가
                    dp[i].add(x - y)        # 뺄셈 결과 추가
                    dp[i].add(x * y)        # 곱셈 결과 추가
                    if y != 0:              # 나눗셈에서 0으로 나누기 방지
                        dp[i].add(x // y)   # 나눗셈 결과 추가 (몫만)
        if number in dp[i]:                 # i번 사용해서 number 만들 수 있는지 확인
            return i                        # 만들 수 있으면 최소 횟수 반환
    return -1                               # 8번 이상 사용해야 하면 -1 반환
