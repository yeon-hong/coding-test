def solution(N, stages):
    from collections import Counter

    players = len(stages)
    stage_counts = Counter(stages)  # 각 스테이지 도전자 수
    challenger = players
    failure_rates = []

    for stage in range(1, N + 1):
        count = stage_counts.get(stage, 0)
        if challenger == 0:
            failure_rates.append((stage, 0))
        else:
            failure_rates.append((stage, count / challenger))
        challenger -= count  # 다음 스테이지 도전자 수 갱신

    # 실패율 내림차순 정렬, 실패율 같으면 스테이지 번호 오름차순
    failure_rates.sort(key=lambda x: (-x[1], x[0]))

    # 정답: 스테이지 번호만 추출
    return [stage for stage, _ in failure_rates]

