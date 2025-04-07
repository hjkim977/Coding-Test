def solution(genres, plays):
    genre_total = {} #장르별 총 재생 수
    genre_songs = {} #노래 목록

    # 1. 장르별로 총 재생 수, 노래 목록 만들기
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 총 재생 수
        if genre in genre_total:
            genre_total[genre] += play
        else:
            genre_total[genre] = play

        # 장르별 노래 목록
        if genre in genre_songs:
            genre_songs[genre].append((play, i))
        else:
            genre_songs[genre] = [(play, i)]

    # 2. 장르를 총 재생 수 기준으로 정렬
    sorted_genres = sorted(genre_total, key=lambda x: genre_total[x], reverse=True)

    result = []

    # 3. 각 장르별 노래 정렬 후 상위 2개 고르기
    for genre in sorted_genres:
        songs = genre_songs[genre]
        # 재생 수 내림차순, 고유번호 오름차순 정렬
        songs.sort(key=lambda x: (-x[0], x[1]))
        # 상위 2개 추출
        for song in songs[:2]:
            result.append(song[1])

    return result
