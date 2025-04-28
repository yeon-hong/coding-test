def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    pos_mm, pos_ss = [int(x) for x in pos.split(":")]
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)
    
    for i in range(len(commands)):
        pos_mm, pos_ss = opening_skip(pos_mm, pos_ss, op_start, op_end)
        if commands[i] == 'next':
            pos_ss += 10
            pos_mm,pos_ss = normalize(pos_mm,pos_ss,video_len)
        elif commands[i] == 'prev':
            pos_ss -= 10
            pos_mm,pos_ss = normalize(pos_mm,pos_ss,video_len)
    
    pos_mm, pos_ss = opening_skip(pos_mm, pos_ss, op_start, op_end)
    answer = f"{pos_mm:02}:{pos_ss:02}"
    print(answer)
    return answer

def normalize(mm,ss,video_len):
    video_mm,video_ss= [int(x) for x in video_len.split(":")]
    
    if ss >=60:
        ss = ss%60
        mm += 1
    elif ss < 0:
        ss = 60 + ss
        mm -= 1
        
    if mm >=video_mm and ss > video_ss:
        mm,ss = video_mm,video_ss
    elif mm < 0:

        mm,ss = 0,0
        
    print(mm,ss)
    return mm,ss

def time_to_seconds(time):
    mm,ss= [int(x) for x in time.split(":")]
    return mm * 60 + ss

def opening_skip(pos_mm, pos_ss, op_start, op_end):
    pos = pos_mm * 60 + pos_ss
    if op_start <= pos <= op_end:
            pos = op_end
            
    mm = pos//60
    ss = pos%60

    return mm, ss

    

    
    
    
    