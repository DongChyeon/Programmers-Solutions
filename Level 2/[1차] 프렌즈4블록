def solution(m, n, board):
    board = [list(board[i]) for i in range(m)]
    
    while True:
        dx = [0, 1, 0, 1]
        dy = [0, 0, 1, 1]

        # 지울 블록들의 목록
        remove_list = []
        
        for y in range(m):
            for x in range(n):
                remove_flag = True
                block = board[y][x]
                # 비어있는 블록일 경우 무시
                if block == '_':
                    continue
                for i in range(1, 4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= m or nx < 0 or nx >= n:
                        remove_flag = False
                        continue
                    # 인접한 2 x 2 블록이 서로 같지 않을 경우 flag룰 False로 설정
                    if block != board[ny][nx]:
                        remove_flag = False
                if remove_flag:
                    # 인접한 2 x 2 블록이 서로 같은 경우 지울 목록에 추가
                    for i in range(4):
                        if (y + dy[i], x + dx[i]) not in remove_list:
                            remove_list.append((y + dy[i], x + dx[i]))
                            
        if remove_list:
            end_flag = False
        else:
            end_flag = True
        
        # 지운 블록들에 대해 'X' 표시
        for i in remove_list:
            board[i[0]][i[1]] = '_'
        
        # 아래에서부터 탐색해서 빈자리에 블록을 당겨옴
        for x in range(n):
            for y in range(m - 1, 0, -1):
                while board[y][x] == '_' and board[y - 1][x] != '_':
                    end_flag = False
                    board[y][x] = board[y - 1][x]
                    board[y - 1][x] = '_'
                    # 당긴 지점으로 돌아가서 재탐색
                    if y < m - 1:
                        y += 1
        
        # 지운 블록이 있는 경우에만 계속 반복
        if not end_flag: 
            continue
        break
    
    return sum(x.count('_') for x in board)
