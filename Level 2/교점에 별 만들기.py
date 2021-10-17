def solution(line):
    # 교점들을 나타내는 변수
    points = set()
    
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            # 두 직선이 평행 또는 일치
            if a * d == b * c:
                continue
            # 두 직선의 교점을 구함
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            # 정수로만 표현되는 좌표만 추가
            if x % 1 == 0 and y % 1 == 0:
                points.add((int(x), int(y)))     
    
    width = max(points, key = lambda x : x[0])[0] - min(points, key = lambda x : x[0])[0] + 1
    height = max(points, key = lambda x : x[1])[1] - min(points, key = lambda x : x[1])[1] + 1
    
    answer = [['.' for _ in range(width)] for _ in range(height)]
    
    for point in points:
        x, y = point
        # 음수로 표현되는 좌표를 양수로 전환
        dx = -min(points, key = lambda x : x[0])[0]
        dy = -min(points, key = lambda x : x[1])[1]
        # 교점들에 별을 그림
        answer[(height - 1) - (y + dy)][x + dx] = '*'
    
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    
    return answer
