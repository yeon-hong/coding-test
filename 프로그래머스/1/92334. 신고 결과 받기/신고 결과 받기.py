def solution(id_list, report, k):
    # 사용자별 신고 정보 초기화
    user_report = {
        'id': [],
        'report': [],   # 각 사용자가 신고한 사용자 리스트
        'count': []     # 각 사용자가 신고당한 횟수
    }

    # 기본 구조 세팅
    for user in id_list:
        user_report['id'].append(user)
        user_report['report'].append([])
        user_report['count'].append(0)

    # 중복 신고 제거
    set_report = set(report)

    # 신고 정보 채우기
    for r in set_report:
        reporter, reported = r.split()
        idx = user_report['id'].index(reporter)
        user_report['report'][idx].append(reported)

        reported_idx = user_report['id'].index(reported)
        user_report['count'][reported_idx] += 1

    # k번 이상 신고당한 사용자 리스트 추출
    banned_users = set()
    for i in range(len(user_report['id'])):
        if user_report['count'][i] >= k:
            banned_users.add(user_report['id'][i])

    # 각 사용자가 받은 알림 개수 계산
    answer = []
    for reports in user_report['report']:
        count = 0
        for reported_user in reports:
            if reported_user in banned_users:
                count += 1
        answer.append(count)

    return answer
