def solution(rows, columns, queries):
    answer = []
    
    # rows x columsn 크기의 행렬 초기화
    matrix = []
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(i * columns + j + 1)
        matrix.append(temp)
    
    for query in queries:
        boundary = []
        temp1 = matrix[query[0]][query[1] - 1]
        boundary.append(temp1)
        
        # 왼쪽 -> 오른쪽 회전
        for x in range(query[1] - 1, query[3]):
            temp2 = matrix[query[0] - 1][x]
            matrix[query[0] - 1][x] = temp1
            temp1 = temp2
            boundary.append(temp1)
            
        # 위쪽 -> 아래쪽 회전
        for y in range(query[0], query[2]):
            temp2 = matrix[y][query[3] - 1]
            matrix[y][query[3] - 1] = temp1
            temp1 = temp2
            boundary.append(temp1)
        
        # 오른쪽 -> 왼쪽 회전
        for x in range(query[3] - 2, query[1] - 2, -1):
            temp2 = matrix[query[2] - 1][x]
            matrix[query[2] - 1][x] = temp1
            temp1 = temp2
            boundary.append(temp1)
            
        # 아래쪽 -> 위쪽 회전
        for y in range(query[2] - 2, query[0] - 2, -1):
            temp2 = matrix[y][query[1] - 1]
            matrix[y][query[1] - 1] = temp1
            temp1 = temp2
            boundary.append(temp1)
            
        # 회전한 테두리의 값 중 가장 작은 값을 answer에 추가
        answer.append(min(boundary))
        
    return answer
   
