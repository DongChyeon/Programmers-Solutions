def dfs(k, count, dungeons):
    global answer, visited
    
    if count > answer:
        answer = count
        
    for i in range(len(dungeons)):
        # 최소 필요 피로도보다 현재 피로도가 높을 시 방문
        if k >= dungeons[i][0] and visited[i] == False:
            visited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons)
            visited[i] = False

def solution(k, dungeons):
    global answer, visited
    
    answer = -1
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons)
    
    return answer
