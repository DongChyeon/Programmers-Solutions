from collections import deque

def solution(progresses, speeds):
    answer = []

    queue = deque(progresses)
    while (queue):
        for i in range (0, len(speeds)):
            queue[i] += speeds[i]    
        if queue[0] >= 100:
            count = 0
            for progress in list(queue):
                if progress < 100:
                    break
                queue.popleft()
                speeds.pop(0)
                count += 1
            answer.append(count)

    return answer