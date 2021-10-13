def solution(new_id):
    answer = []
    
    for ch in new_id:
        # 모든 대문자를 소문자로 치환
        if ch.isalpha():
            answer.append(ch.lower())
        # 알파벳 소문자, 숫자, '-', '_', '.'를 제외한 모든 문자 제거
        elif ch.isdigit() or ch == '-' or ch == '_' or ch == '.':
            answer.append(ch)
    
    # 2번 이상 연속되는 '.'를 하나의 '.'로 치환
    idx = 0
    while idx < len(answer) - 1:
        prev_idx, next_idx = idx, idx + 1
        if answer[prev_idx] == '.' and answer[next_idx] == '.':
            answer.pop(prev_idx)
            idx = 0
        else:
            idx += 1
            
    # 처음이나 끝 부분의 "." 제거
    if answer and answer[0] == '.':
        answer.pop(0)
    if answer and answer[-1] == '.':
        answer.pop()
    
    # 빈 문자열이라면 "a" 대입
    if not answer:
        answer.append('a')
    
    # 길이가 16자 이상이라면 처음 15자를 제외한 나머지 문자 제거
    if len(answer) >= 16:
        while len(answer) > 15:
            answer.pop()
    # 제거 후 '.'가 끝에 위치한다면 끝에 위치한 '.' 제거
    while answer and answer[-1] == '.':
        answer.pop()
    
    # 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복        
    if len(answer) <= 2:
        while len(answer) < 3:
            answer.append(answer[-1])
    
    return ''.join(answer)
