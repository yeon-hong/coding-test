def solution(num, total):
    # 가능한 시작 수 x를 탐색
    for x in range(-1000, 1000):  # 적절한 범위 설정
        seq = [x + i for i in range(num)]
        if sum(seq) == total:
            return seq