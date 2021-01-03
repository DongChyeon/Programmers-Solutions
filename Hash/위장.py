def solution(clothes):
    a = {}
    for i in range (0, len(clothes)):
        if (clothes[i][1] not in a):
            a[clothes[i][1]] = 1
        else:
            a[clothes[i][1]] = a[clothes[i][1]] + 1
    
    answer = 0
    for i in a.values():
        if answer == 0:
            answer += (i + 1)
        else:
            answer *= (i + 1)
    answer -= 1
    
    return answer