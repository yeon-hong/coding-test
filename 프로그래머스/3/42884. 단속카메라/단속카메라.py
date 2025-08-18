def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[1])
    camera = routes[0][1]   # 첫 번째 차량의 진출 지점에 카메라 설치

    for i in range(1, len(routes)):
        if routes[i][0] > camera:  # 카메라 위치보다 뒤에서 진입 → 새로운 카메라 필요
            answer += 1
            camera = routes[i][1]  # 새 카메라 설치
            
    return answer