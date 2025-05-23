def solution(s, skip, index):
    answer = ''
    for c in s:
        count = 0
        current = ord(c)

        while count < index:
            current += 1
            if current > ord('z'):
                current = ord('a')
            if chr(current) not in skip:
                count += 1

        answer += chr(current)
            
    return answer

