def solution(arr):
    def compress(x, y, size):                                 # (x, y) 좌표에서 시작하는 size x size 영역 압축 함수
        initial = arr[x][y]                                    # 기준값: 영역의 첫 번째 값
        all_same = True                                        # 모든 값이 같은지 확인할 플래그

        for i in range(x, x + size):                           # 행 순회
            for j in range(y, y + size):                       # 열 순회
                if arr[i][j] != initial:                       # 하나라도 다르면
                    all_same = False                           # 플래그 False로 설정
                    break                                      # 내부 루프 탈출
            if not all_same:                                   # 바깥 루프도 탈출
                break

        if all_same:                                           # 모두 동일한 값이면
            if initial == 0:
                return [1, 0]                                  # 0이 1개
            else:
                return [0, 1]                                  # 1이 1개
        else:
            half = size // 2                                   # 사이즈 절반으로 나누기

            top_left     = compress(x, y, half)                # 좌상
            top_right    = compress(x, y + half, half)         # 우상
            bottom_left  = compress(x + half, y, half)         # 좌하
            bottom_right = compress(x + half, y + half, half)  # 우하

            # 각 결과를 더해서 반환
            return [
                top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0],   # 0의 개수 합
                top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]    # 1의 개수 합
            ]

    n = len(arr)                                               # 배열 크기
    return compress(0, 0, n)                                   # 전체 배열 압축 시작
