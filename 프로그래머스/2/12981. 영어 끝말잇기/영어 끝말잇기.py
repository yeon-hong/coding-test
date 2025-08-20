def solution(n, words):
    used = set()  # 이미 나온 단어 저장
    used.add(words[0])  # 첫 단어 추가

    for i in range(1, len(words)):
        prev = words[i - 1]
        curr = words[i]

        # 규칙 위반 검사
        if (curr in used) or (prev[-1] != curr[0]):
            player = (i % n) + 1       # 몇 번째 사람인지
            turn = (i // n) + 1        # 몇 번째 차례인지
            return [player, turn]

        used.add(curr)

    return [0, 0]  # 탈락자가 없을 경우
