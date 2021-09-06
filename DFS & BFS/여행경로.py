def dfs(start, tickets, visited, count):
    global answer
    
    if count == len(tickets):
        return True
    
    for i in range(len(tickets)):
        if not visited[i] and start == tickets[i][0]:
            visited[i] = True
            answer.append(tickets[i][1])
            if dfs(tickets[i][1], tickets, visited, count + 1):
                return True
            visited[i] = False
    # 길이 끊겨 있으면 마지막으로 연결한 곳 제거
    answer.pop(-1)
    
    return False

def solution(tickets):
    global answer
    
    answer = ["ICN"]
    visited = [False] * len(tickets)
    # 알파벳 순으로 앞서는 경로를 탐색하기 위해 미리 정렬
    tickets.sort()

    dfs("ICN", tickets, visited, 0)
    
    return answer
