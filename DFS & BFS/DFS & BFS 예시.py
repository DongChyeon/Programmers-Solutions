from collections import deque

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = False
    queue = deque([v])
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 4, 5],
    [1, 3],
    [2],
    [1],
    [1]
]

# 각 노드가 방문된 정보
visited = [False] * len(graph)
dfs(graph, 1, visited)

# 방문 정보 초기화
visited = [False] * len(graph)
bfs(graph, 1, visited)