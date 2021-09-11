def solution(places):
    answer = []
    
    for place in places:
        is_keep_distance = True
        
        field = []
        for x in place:
            field.append(list(x))
            
        people = []
        for y in range(len(field)):
            for x in range(len(field[y])):
                if field[y][x] == 'P':
                    people.append((y, x))
            
        for i in range(len(people)):
            for j in range(len(people)):
                # 같은 사람을 비교할 경우 스킵
                if i == j:
                    continue
                manhattan_dist = abs(people[i][0] - people[j][0]) + abs(people[i][1] - people[j][1])
                if manhattan_dist == 1:
                    is_keep_distance = False
                    break
                elif manhattan_dist == 2:
                    # 가로로 같은 줄에 앉아있다면 사이에 패널이 있는지 검사
                    if people[i][0] == people[j][0]:
                        if field[people[i][0]][max(people[i][1], people[j][1]) - 1] != 'X':
                            is_keep_distance = False
                            break
                    # 세로로 같은 줄에 앉아있다면 사이에 패널이 있는지 검사
                    if people[i][1] == people[j][1]:
                        if field[max(people[i][0], people[j][0]) - 1][people[i][1]] != 'X':
                            is_keep_distance = False
                            break
                    # 대각선으로 앉아있다면 사이에 패널이 있는지 검사
                    if abs(people[i][0] - people[j][0]) == 1 and abs(people[i][1] - people[j][1]) == 1:
                        # 왼쪽 -> 아래쪽 대각선으로 앉아있을 때
                        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                            if field[people[i][0]][people[i][1] + 1] != 'X' or field[people[j][0]][people[j][1] - 1] != 'X':
                                is_keep_distance = False
                                break
                        elif people[j][0] < people[i][0] and people[j][1] < people[i][1]:
                            if field[people[j][0]][people[j][1] + 1] != 'X' or field[people[i][0]][people[i][1] - 1] != 'X':
                                is_keep_distance = False
                                break
                        # 오른쪽 -> 왼쪽 대각선으로 앉아있을 때
                        elif people[i][0] > people[j][0] and people[i][1] < people[j][1]:
                            if field[people[j][0]][people[j][1] - 1] != 'X' or field[people[i][0]][people[i][1] + 1] != 'X':
                                is_keep_distnace = False
                                break
                        elif people[j][0] > people[i][0] and people[j][1] < people[i][1]:
                            if field[people[i][0]][people[i][1] - 1] != 'X' or field[people[j][0]][people[j][1] + 1] != 'X':
                                is_keep_distance = False
                                break
                            
        if is_keep_distance:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
