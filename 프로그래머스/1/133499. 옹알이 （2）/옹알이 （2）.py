def solution(babbling):
    answer = 0
    for word in babbling:
        if can_pronounce(word):
            answer += 1
    return answer

def can_pronounce(word):
    sounds = ["aya", "ye", "woo", "ma"]
    prev = ''
    while word:
        matched = False
        for sound in sounds:
            if word.startswith(sound) and sound != prev:
                word = word[len(sound):]
                prev = sound
                matched = True
                
        if not matched:
            return False
    return True

            
        