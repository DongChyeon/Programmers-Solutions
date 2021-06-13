from collections import deque

def solution(n, computers):
    answer = 0
    queue = deque([])
    
    for i in range(n):
        for j in range(n):
            # BFS
            if computers[i][j] == 1:
                queue.append(i)
                computers[i][j] = 0
                
                while queue:
                    y = queue.popleft()
                    for x in range(n):
                        if computers[y][x] == 1:
                            computers[y][x] = 0
                            queue.append(x)
                            
                # 연결된 부분의 개수를 하나 증가시켜줌            
                answer += 1
                
    return answer
