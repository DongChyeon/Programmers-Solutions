import heapq

def solution(jobs):
    answer = 0
    end_time = 0
    idx = 0
    count = 0
    
    heap = []
    jobs.sort()
    
    while count < len(jobs):
        while idx < len(jobs) and jobs[idx][0] <= end_time:
            # [수행시간, 작업 요청 시간]
            heapq.heappush(heap, [jobs[idx][1], jobs[idx][0]])
            idx += 1
        if not heap:
            end_time = jobs[idx][0]
        else:
            # 현재 작업 종료 시간까지 요청된 작업 중 수행시간이 가장 적은 것부터 수행
            temp = heapq.heappop(heap)
            answer += end_time + temp[0] - temp[1]
            end_time += temp[0]
            count += 1
    
    # 소수점 이하는 버려줌
    return answer // len(jobs)
