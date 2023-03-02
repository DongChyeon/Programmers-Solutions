from collections import deque

def bfs(start_y, start_x, end_y, end_x, maps):
    queue = deque([[start_y, start_x, 0]])
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[start_y][start_x] = True
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while queue:
        y, x, time = queue.popleft()
        
        if y == end_y and x == end_x:
            return time
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] != 'X' and visited[ny][nx] == False:
                    queue.append([ny, nx, time + 1])
                    # 방문 처리 미리 해줘야 함
                    visited[ny][nx] = True
                    
    return -1

def solution(maps):
    # 맵의 구성요소 위치 파악
    s_x, s_y = 0, 0
    l_x, l_y = 0, 0
    
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'S':
                s_x, s_y = x, y
            elif maps[y][x] == 'L':
                l_x, l_y = x, y
            elif maps[y][x] == 'E':
                e_x, e_y = x, y
    
    
    s_to_l = bfs(s_y, s_x, l_y, l_x, maps)
    l_to_e = bfs(l_y, l_x, e_y, e_x, maps)
    
    # 입구 - 레버 - 출구 경로가 불가
    if s_to_l == -1 or l_to_e == -1:
        return -1
    else:
        return s_to_l + l_to_e
