def solution(record):
    answer = []
    user_dict = {}
    
    for x in record:
        command = x.split()
        if command[0] == 'Enter' or command[0] == 'Change':
            user_dict[command[1]] = command[2]
        
    for x in record:
        command = x.split()
        temp = ''
        temp += user_dict[command[1]] + '님이 '
        
        if command[0] == 'Enter':
            temp += '들어왔습니다.'
            answer.append(temp)
        elif command[0] == 'Leave':
            temp += '나갔습니다.'
            answer.append(temp)
        
    return answer
