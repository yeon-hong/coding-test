def solution(friends, gifts):
    n = len(friends)                    
    idx = {name: i for i, name in enumerate(friends)}

    given      = [0] * n                      # given[i]     : i가 총 몇 개 줬는지
    received   = [0] * n                      # received[i]  : i가 총 몇 개 받았는지
    gifts_cnt  = [[0] * n for _ in range(n)]  # gifts_cnt[i][j] : i가 j에게 준 선물 횟수 (대칭 X, 방향성 O)
    
    
    # gifts 배열 순회하며 통계 채우기
    for rec in gifts:                   
        giver, taker = rec.split()      # 문자열을 공백 기준으로 분리
        g, t = idx[giver], idx[taker]   # 이름을 인덱스로 변환

        # 전체 통계
        given[g]      += 1              # g가 선물 하나 줌
        received[t]   += 1              # t가 선물 하나 받음

        # 두 사람 간 방향성 있는 횟수
        gifts_cnt[g][t] += 1


    # 선물 지수(=준 개수 - 받은 개수) 계산
    score = [given[i] - received[i] for i in range(n)]


    # 다음 달에 받을 선물 수 계산용 배열
    next_recv = [0] * n                 # next_recv[i] : i가 다음 달 받을 개수

    # ---------------------------------------------------------
    # 6. 모든 “순서쌍” (i, j)를 검사 (i ≠ j)  ← 중요!
    # ---------------------------------------------------------
    #   - i가 j보다 많이 줬으면 ➜ j가 i에게서 1개 받는다.
    #   - 서로 준 개수가 같으면 ➜ 선물 지수가 높은 쪽이 1개 받는다.
    #   - 지수도 같으면 아무도 못 받는다.
    #   ※ (i, j)와 (j, i)를 모두 따로 계산해야 “대칭”이 완벽히 반영된다.
    # ---------------------------------------------------------
    for i in range(n):
        for j in range(n):
            if i == j:                  # 자기 자신과 비교는 스킵
                continue

            i_to_j = gifts_cnt[i][j]    # i → j 로 준 횟수
            j_to_i = gifts_cnt[j][i]    # j → i 로 준 횟수

            if i_to_j > j_to_i:         # i가 더 많이 줬다
                next_recv[i] += 1       # → i가 1개 “받음”(즉 j가 줌)
            elif i_to_j == j_to_i:      # 횟수가 같음
                if score[i] > score[j]:
                    next_recv[i] += 1   # 지수가 높은 i가 1개 받음
                                        # 지수까지 같으면 아무도 받지 못하므로 else 없음
                                        # (j_to_i > i_to_j) 인 경우는 for문에서 (j, i) 순서로 만나서 처리됨
    print(next_recv)
    return max(next_recv)


