from datetime import datetime, timedelta
import heapq

def solution(book_time):
    # 1. 예약 시간 시작 기준으로 정렬
    book_time.sort(key=lambda x: datetime.strptime(x[0], "%H:%M"))
    
    # 2. 각 객실의 퇴실 시간(청소 끝난 시간)을 관리하는 최소 힙
    rooms = []
    
    for start, end in book_time:
        start_time = datetime.strptime(start, "%H:%M") 
        end_time = datetime.strptime(end, "%H:%M") + timedelta(minutes=10)  # 청소시간 포함
        
        # 현재 예약 시작 시간이 가장 이른 퇴실(청소 완료) 시간보다 같거나 크면
        # 기존 객실을 재활용 가능 (힙에서 가장 빨리 비는 객실 pop)
        if rooms and rooms[0] <= start_time:
            heapq.heappop(rooms)
        
        # 이번 예약 객실 퇴실 시간(청소 완료 시간)을 힙에 추가
        heapq.heappush(rooms, end_time)
    
    # 힙에 남은 객실 수가 최소 객실 개수
    return len(rooms)
