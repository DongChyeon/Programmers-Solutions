def isSameMelody(play_sound, listened):
    listened_last = len(listened) - 1
    for i in range(len(play_sound) - listened_last):
        if play_sound[i + listened_last] == listened[listened_last]:
            start = i
            k = 0
            while play_sound[start + k] == listened[k]:
                k += 1
                if k == len(listened):
                    return True
    return False

def solution(m, musicinfos):
    candidates = []
    
    for i in range(len(musicinfos)):
        info = musicinfos[i].split(",")
        start_time = info[0].split(":")
        end_time = info[1].split(":")
        play_time = (int(end_time[0]) * 60 + int(end_time[1]) - (int(start_time[0]) * 60 + int(start_time[1])))
        title = info[2]
        
        melody = []
        for j in range(len(info[3])):
            if info[3][j] == '#':
                melody[-1] += info[3][j]
            else:
                melody.append(info[3][j])
            
        play_sound = []
        for sound in range(play_time):
            play_sound.append(melody[sound % len(melody)])
            sound += 1
        
        listened = []
        for j in range(len(m)):
            if m[j] == '#':
                listened[-1] += m[j]
            else:
                listened.append(m[j])
        
        if isSameMelody(play_sound, listened):
            candidates.append([i, play_time, title])
    
    # 후보가 하나인 경우
    if len(candidates) == 1:
        return candidates[0][2]
    # 후보가 두 개 이상인 경우
    elif len(candidates) > 1:
        play_times = []
        for candidate in candidates:
            play_times.append(candidate[1])

        # 플레이 시간이 제일 긴 곡을 담음
        candidates2 = []
        max_play_time = max(play_times)
        for candidate in candidates:
            if max_play_time == candidate[1]:
                candidates2.append(candidate)
        # 플레이 시간이 제일 긴 곡 중 처음 곡을 반환
        return candidates2[0][2]
        
    return "(None)"