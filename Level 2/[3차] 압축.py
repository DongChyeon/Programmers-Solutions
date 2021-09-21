def solution(msg):
    answer = []
    
    # 사전 초기화
    word_dict = dict()
    for i in range(26):
        word_dict[chr(65 + i)] = i + 1
    
    # 사전에 새길 색인 번호
    num = 27
    idx = 0
    while idx < len(msg):
        target = msg[idx]
        # target이 이미 사전에 있다면 찾고자 하는 글자 수의 범위를 늘림
        while target in word_dict.keys():
            idx += 1
            if idx == len(msg):
                break
            target += msg[idx]
        # target이 사전에 있는 단어라면 스킵
        if target in word_dict.keys():
            continue
        # 현재 글자에 해당하는 색인 번호 출력 후 다음 글자를 포함한 target을 사전에 등록
        answer.append(word_dict[target[:-1]])
        word_dict[target] = num
        num += 1
    answer.append(word_dict[target])
    
    return answer
