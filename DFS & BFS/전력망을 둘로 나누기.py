from collections import deque
import copy
    
def solution(n, wires):
    answer = 100
    
    for i in range(len(wires)):
        # 전선을 하나씩 끊어봄
        wires_cp = copy.deepcopy(wires)
        wires_cp.pop(i)
        
        # 인접 리스트 생성
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        
        for wire in wires_cp:
            v1, v2 = wire
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # BFS 탐색
        queue = deque([])
        
        # BFS 탐색의 시작점을 결정함
        for i in range(len(graph)):
            if graph[i]:
                queue.append(i)
                visited[i] = True
                break
        
        while queue:
            v = queue.popleft()
            visited[v] = True
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
        
        # 방문한 노드와 방문하지 않은 노드(0 제외)의 차이를 이용해 답을 구해냄
        answer = min(answer, abs((visited.count(False) - 1) - visited.count(True)))
    
    return answer
