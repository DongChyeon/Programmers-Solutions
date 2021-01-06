from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    queue = deque([])
    truck_position = [0] * len(truck_weights)
    
    i = 0
    while i < len(truck_weights):
        total_weight = 0
        
        for truck in list(queue):
            truck_position[truck] += 1
        
        for truck in list(queue):
            total_weight += truck_weights[truck]
        
        if (queue):
            # 큐의 맨 앞 원소가 다리를 지나왔을 때
            if truck_position[queue[0]] > bridge_length:
                total_weight -= truck_weights[queue.popleft()]
                if total_weight + truck_weights[i] <= weight:
                    queue.append(i)
                    truck_position[i] = 1
                    i += 1
            else:
                if total_weight + truck_weights[i] <= weight:
                    queue.append(i)
                    truck_position[i] = 1
                    i += 1
                    
        else:
            # 큐가 비어있을 때
            if total_weight + truck_weights[i] <= weight:
                queue.append(i)
                truck_position[i] = 1
                i += 1
    
        answer += 1
        
    while (queue) :
        for truck in list(queue):
            truck_position[truck] += 1
        if truck_position[queue[0]] > bridge_length:
            queue.popleft()
        
        answer += 1
    
    return answer