from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([])
    
    # 큐에 인쇄 요청의 순서를 넣음
    for i in range(0, len(priorities)):
        queue.append(i)
    
    next = 0
    while True:
        front = queue[0]
        next = priorities[front]
        
        for i in range(1, len(queue)):
            next = max(priorities[queue[i]], next)
            
        # 대기열보다 중요도가 높은 문서가 하나라도 있다면
        if next > priorities[front]:
            queue.popleft()
            queue.append(front)
        # 없다면 pop하고 위치 체크
        else:
            print_out = queue.popleft()
            answer += 1
            if print_out == location:
                break
    
    return answer