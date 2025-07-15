from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)  # 무게별 개수 세기

    for i in range(100, 1001):  # 몸무게 범위: 100 ~ 1000
        if counter[i] > 0:  # 해당 무게가 존재할 때만 계산
            answer += (counter[i] * (counter[i] - 1)) / 2  # 같은 무게끼리 1:1 거리 짝 계산 (조합 nC2)
            answer += counter[i] * counter[i * 3 / 2]       # 2:3 거리 비율에 맞는 짝 수 계산
            answer += counter[i] * counter[i * 2]           # 2:4 거리 비율에 맞는 짝 수 계산
            answer += counter[i] * counter[i * 4 / 3]       # 3:4 거리 비율에 맞는 짝 수 계산

    return answer