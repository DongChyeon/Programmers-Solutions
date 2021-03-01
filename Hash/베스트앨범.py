def solution(genres, plays):
    answer = []
    
    total_plays = { x : 0 for x in genres }
    songs = []
    for i in range(len(genres)):
        total_plays[genres[i]] += plays[i]
        songs.append({'id': i, 'genre': genres[i], 'play': plays[i]})
    
    # 가장 많이 재생된 장르순으로 나열함
    total_plays = sorted(total_plays.items(), key = lambda x : x[1], reverse = True)
    for info in total_plays:
        temp = []
        for song in songs:
            if song['genre'] == info[0]:
                temp.append(song)
        # 가장 많이 재생된 노래, 고유 번호가 낮은 노래 순으로 수록
        temp.sort(key = lambda x : (-x['play'], x['id']))
        limit = min(2, len(temp))
        for i in range(limit):
            answer.append(temp[i]['id'])
            
    return answer