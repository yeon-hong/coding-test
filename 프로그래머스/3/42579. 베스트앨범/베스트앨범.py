def solution(genres, plays):

    # 1. 정보를 종합하여 { 장르 : { 고유번호 : 재생 횟수 } } 형태로 만들기. 
    genre_dic = {}   

    for i in set(genres):
        genre_dic[i] = {}      

    for i in range(len(genres)):
        genre_dic[genres[i]][i] = plays[i]



    # 2. 중첩 딕셔너리 정렬 및 장르 우선순위 구하기

    sum_genre = []
    for k in genre_dic.keys():
        sum_genre += [[k,sum(genre_dic[k].values())]]
        genre_dic[k] = sorted(genre_dic[k].items() ,key=lambda x:(-x[1],x[0]))

    sum_genre.sort(key = lambda x:-x[1])

    # 3. 총 재생수가 많은 장르부터 재생 수가 많은 고유번호 2개씩 결과 리스트에 넣기.

    result =[]
    for i in sum_genre:
        genre = i[0]
        
        if len(genre_dic[genre]) >= 2:
            result += [genre_dic[genre][0][0]]
            result += [genre_dic[genre][1][0]]
        else:
            result += [genre_dic[genre][0][0]]

    return result