from collections import deque    

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    queue = deque([(0, 0, 1)])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 상대방 진영에 다다를 경우 이동 거리 리턴
        if x == m - 1 and y == n - 1:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위를 벗어난 경우 탐색 x
            if nx < 0 or nx >= m or ny < 0 or ny >= n or maps[ny][nx] == 0:
                continue
                
            if maps[ny][nx] == 1:
                # 다시 방문하지 못하도록 벽으로 표시
                maps[ny][nx] = 0
                queue.append((nx, ny, dist + 1))
       
    # 상대방 진영에 다다르지 못할 경우 -1 리턴
    return -1
