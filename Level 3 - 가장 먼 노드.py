import heapq
import sys

def solution(n, edge):
    INF = int(5e4 + 1)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for x in edge:
        graph[x[0]].append((x[1], 1))
        graph[x[1]].append((x[0], 1))
              
    queue = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여 큐에 삽입
    heapq.heappush(queue, (0, 1))
    distance[1] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    
    max_dist = 0
    for x in distance:
        if x != INF and x > max_dist:
            max_dist = x
    
    answer = 0
    for x in distance:
        if x == max_dist:
            answer += 1
            
    return answer
