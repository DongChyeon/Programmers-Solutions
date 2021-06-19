import heapq

def solution(operations):
    heap = []
    
    for x in operations:
        oper = x.split()
        if oper[0] == 'I':
            heapq.heappush(heap, int(oper[1]))
        elif heap and oper[0] == 'D':
            # 최댓값 삭제
            if oper[1] == '1':
                heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
            # 최솟값 삭제
            elif oper[1] == '-1':
                heapq.heappop(heap)
                
    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]
    else:
        return [0, 0]
