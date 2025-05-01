def solution(mats, park):
    answer =  -1
    mats.sort(reverse=True)                  # 내림차순 정렬
    row, col = len(park), len(park[0])     # 6, 8
    for s in mats:
        for i in range(row - s + 1):
            for j in range(col - s + 1):
                if check(park, i, j, s):    # s×s 영역이 모두 -1인지 검사
                    return s

    return answer

def check(park, x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if park[i][j] != "-1":
                return False
    return True