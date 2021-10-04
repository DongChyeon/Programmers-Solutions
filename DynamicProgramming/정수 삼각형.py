def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            # 가장 왼쪽에 위치했을 때
            if j == 0:
                triangle[i][j] += triangle[i - 1][0]
            # 가장 오른쪽에 위치했을 때
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][len(triangle[i - 1]) - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
                
    return max(triangle[-1])
