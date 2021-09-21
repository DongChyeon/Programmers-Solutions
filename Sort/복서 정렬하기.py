def solution(weights, head2head):
    # 자기보다 몸무게가 무거운 복서를 이긴 횟수
    more_weight = [0] * len(head2head)
    for i in range(len(more_weight)):
        for j in range(len(head2head)):
            if i == j:
                continue
            if head2head[i][j] == 'W' and weights[j] > weights[i]:
                more_weight[i] += 1
    # 승률은 이긴 이긴 횟수 / 치른 라운드 수 로 처리
    for i in range(len(head2head)):
        # 치른 라운드 수가 0일 경우 승률 0으로 처리 (division by zero 오류를 방지하기 위함)
        if len(head2head[i]) == head2head[i].count('N'):
            head2head[i] = 0
            continue
        head2head[i] = head2head[i].count('W') / (len(head2head[i]) - head2head[i].count('N'))
    numbers = [num + 1 for num in range(len(weights))]
    
    # zip으로 묶은 뒤 자신의 승률, 자기보다 몸무게가 무거운 복서를 이긴 횟수, 자신의 몸무게, 자신의 번호 순으로 정렬
    result = sorted(list(zip(numbers, more_weight, weights, head2head)), key = lambda x : (-x[3], -x[1], -x[2], x[0]))
    
    # 정렬한 복서들의 번호를 반환
    return [x[0] for x in result]
