def solution(n,a,b):
    answer = 0
    
    # 이번 라운드에 참가하는 참가자 목록
    current_round = [x for x in range(1, n + 1)]
            
    while len(current_round) > 1:
        answer += 1
        # 다음 라운드에 진출하는 참가자 목록
        next_round = [0] * (len(current_round) // 2)
        idx = 0
        for i in range(0, len(current_round), 2):
            # a 참가자와 b 참가자가 만날 경우 라운드 수 리턴
            if (current_round[i] == a and current_round[i + 1] == b) or (current_round[i] == b and current_round[i + 1] == a):
                return answer
            
            # a 참가자나 b 참가자는 무조건 승리하도록 함
            if current_round[i] == a or current_round[i + 1] == a:
                next_round[idx] = a
                idx += 1
            elif current_round[i] == b or current_round[i + 1] == b:
                next_round[idx] = b
                idx += 1    
            else:
                next_round[idx] = current_round[i]
                idx += 1
        
        # 이번 라운드 참가자 목록 갱신
        current_round = next_round

    return answer
