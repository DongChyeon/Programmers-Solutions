def solution(routes):
    routes.sort()
    interval = [[routes[0][0], routes[0][1]]]
    routes.pop(0)
    
    while routes:
        flag = True
        for i in range(len(interval)):
            if interval[i][0] > routes[0][0] and interval[i][0] > routes[0][1]:
                continue
            elif interval[i][1] < routes[0][0] and interval[i][1] < routes[0][1]:
                continue
            else:
                # interval 업데이트
                interval[i][0] = max(interval[i][0], routes[0][0])
                interval[i][1] = min(interval[i][1], routes[0][1])
                flag = False
        # 해당 차량의 이동 경로가 interval 중에 없다면 추가
        if flag:
            interval.append([routes[0][0], routes[0][1]])
        routes.pop(0)
    
    return len(interval)
