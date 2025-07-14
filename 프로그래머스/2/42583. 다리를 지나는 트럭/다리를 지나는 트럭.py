def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = []
    time = []
    while truck_weights or bridge:
        
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
            time.append(0)
            
        if time[0] >= bridge_length-1:
            bridge.pop(0)  
            time = time[1:]
            

        time = [x + 1 for x in time]  
        answer += 1
        
    return answer