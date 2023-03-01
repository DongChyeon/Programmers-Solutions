from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    field = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(characterX * 2, characterY * 2)])
    distance = [[1] * 102 for _ in range(102)]
    
    while queue:
        x, y = queue.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = distance[x][y] // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if field[nx][ny] == 1 and distance[nx][ny] == 1:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1
    
    return answer
