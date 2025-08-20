def solution(arr1, arr2):
    # arr1의 행 수, arr2의 열 수로 결과 행렬 크기 결정
    rows = len(arr1)
    cols = len(arr2[0])
    
    # 결과 행렬 초기화
    result = [[0] * cols for _ in range(rows)]
    
    # 행렬 곱셈 수행
    for i in range(rows):
        for j in range(cols):
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result