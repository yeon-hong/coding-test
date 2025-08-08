import re
from datetime import datetime


def solution(m, musicinfos):
    m = convert_melody(m)
    candidates = []

    for idx, info in enumerate(musicinfos):
        start, end, name, melody = info.split(',')
        
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        
        time_gap = (end_time.hour * 60 + end_time.minute) - (start_time.hour * 60 + start_time.minute)

        melody = convert_melody(melody)
        full_melody = (melody * ((time_gap // len(melody)) + 1))[:time_gap]

        if m in full_melody:
            candidates.append((time_gap, idx, name))  
            
    if candidates:

        candidates.sort(key=lambda x: (-x[0], x[1]))
        return candidates[0][2]
    
    else:
        return "(None)"


def convert_melody(m):
    return re.sub(r'(C#|D#|F#|G#|A#|B#)', lambda x: x.group(0)[0].lower(), m)
         # re.sub(pattern, repl, string, count=0, flags=0)
                # pattern : 찾을 정규식 패턴 (문자열 또는 정규식 객체)
                # repl : 대체할 문자열 또는 함수
                # string : 검색 대상 문자열
                # count : 몇 번만 바꿀지 (기본 0은 모두 바꿈)
                # flags : 정규식 옵션 (대소문자 무시 등)
