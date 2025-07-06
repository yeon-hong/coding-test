def solution(new_id):
    answer = []

    # 1단계: 소문자 변환
    new_id = new_id.lower()

    # 2단계: 허용 문자만 추가
    for char in new_id:
        if char.isalnum() or char in ['-', '_', '.']:
            answer.append(char)

    # 3단계: 연속된 마침표 제거
    filtered = []
    prev = ''
    for ch in answer:
        if not (ch == '.' and prev == '.'):
            filtered.append(ch)
        prev = ch
    answer = filtered

    # 4단계: 처음이나 끝의 '.' 제거
    if answer and answer[0] == '.':
        answer.pop(0)
    if answer and answer[-1] == '.':
        answer.pop()

    # 5단계: 빈 문자열이면 'a' 추가
    if not answer:
        answer.append('a')

    # 6단계: 길이가 16자 이상이면 자르고 마지막이 '.'이면 제거
    answer = answer[:15]
    if answer[-1] == '.':
        answer.pop()

    # 7단계: 길이가 2자 이하라면 마지막 문자를 반복해서 길이 3까지 확장
    while len(answer) < 3:
        answer.append(answer[-1])

    return ''.join(answer)
