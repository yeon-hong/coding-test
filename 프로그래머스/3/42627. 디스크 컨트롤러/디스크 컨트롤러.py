import heapq

def solution(jobs):
    # 1. 진입 시간 기준 정렬
    jobs.sort(key=lambda x: x[0])
    
    hq = []
    time = 0          # 현재 시간
    answer = 0        # 총 대기 시간
    idx = 0           # jobs 리스트 인덱스
    n = len(jobs)
    
    while idx < n or hq:
        # 2. 현재 시간 <= job 진입 시간인 경우 힙에 추가
        while idx < n and jobs[idx][0] <= time:
            heapq.heappush(hq, (jobs[idx][1], jobs[idx][0]))  # (소요시간, 진입시간)
            idx += 1
        
        if hq:
            # 3. 소요시간이 가장 짧은 작업 실행
            duration, start = heapq.heappop(hq)
            time += duration
            answer += time - start   # 대기시간 = 종료시간 - 진입시간
        else:
            # 4. 힙이 비어있으면 시간 점프
            time = jobs[idx][0]
    
    return answer // n
