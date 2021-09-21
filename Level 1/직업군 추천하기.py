def solution(table, languages, preference):
    answer = ''
    
    job_table = []
    for i in range(len(table)):
        job_table.append(table[i].split())

    lang_pref = list(zip(languages, preference))
    
    # 점수 총합표
    scores = dict()
    for i in range(len(job_table)):
        scores[job_table[i][0]] = 0
    for i in range(len(lang_pref)):
        for col in range(len(job_table)):
            for row in range(len(job_table[col])):
                if lang_pref[i][0] == job_table[col][row]:
                    # 선호도 * 직업군 언어 점수를 더해줌
                    scores[job_table[col][0]] += lang_pref[i][1] * (len(job_table) + 1 - row)           
    
    # 점수(값) 기준 내림차순 정렬, 직업군(키) 기준 오름차순 정렬 후 첫번째 키 반환
    return next(iter(sorted(scores.items(), key = lambda x: (-x[1], x[0]))))[0]
