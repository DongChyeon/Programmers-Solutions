def solution(N, road, K):
    INF = int(10e9)
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    
    # 자기 자신으로 가는 거리는 0으로 초기화
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a == b:
                graph[a][b] = 0
                
    for i in range(len(road)):
        a, b, c = road[i]
        if graph[a][b] > c:
            graph[a][b] = c
        if graph[b][a] > c:
            graph[b][a] = c
    
    # k : 거쳐가는 마을
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    result = 0
    # 첫번째 마을 기준으로 최소 거리가 K 이하인 것을 셈
    for i in range(1, N + 1):
        if graph[1][i] != INF and graph[1][i] <= K:
            result += 1
    
    return result
