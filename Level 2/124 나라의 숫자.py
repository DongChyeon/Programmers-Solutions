def solution(n):
    answer = ''

    while n:
        remain = n % 3
        if remain == 0:
            answer = '4' + answer
            n = n // 3 - 1
        else:
            answer = str(remain) + answer
            n = n // 3
            
    return answer