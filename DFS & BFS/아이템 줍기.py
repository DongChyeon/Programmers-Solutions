from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    field = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    field[y][x] = 0
                elif field[y][x] != 0:
                    field[y][x] = 1
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(characterY * 2, characterX * 2)])
    distance = [[1] * 102 for _ in range(102)]
    
    while queue:
        y, x = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = distance[y][x] // 2
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if field[ny][nx] == 1 and distance[ny][nx] == 1:
                queue.append((ny, nx))
                distance[ny][nx] = distance[y][x] + 1
    
    return answer
