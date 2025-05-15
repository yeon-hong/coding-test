def solution(players, callings):
    # 선수 이름 -> 현재 등수 인덱스 저장
    player_idx = {name: i for i, name in enumerate(players)}
    
    for call in callings:
        curr_idx = player_idx[call]         # 불린 선수의 현재 인덱스
        if curr_idx > 0:
            # 앞 사람과 자리 바꾸기
            front_player = players[curr_idx - 1]
            
            # 리스트에서 자리 바꾸기
            players[curr_idx - 1], players[curr_idx] = players[curr_idx], players[curr_idx - 1]
            
            # 딕셔너리에서도 인덱스 업데이트
            player_idx[call] = curr_idx - 1
            player_idx[front_player] = curr_idx
            
    return players
