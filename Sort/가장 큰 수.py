def solution(numbers):
    answer = ''
    
    numStr = []
    
    for num in numbers:
        ns = ''
        for i in range(3):
            ns += str(num)
        numStr.append(ns)
            
    numStr.sort(reverse = True)
    if int(numStr[0]) == 0:
        return '0'
    
    for num in numStr:
        answer += num[0:int(len(num)/3)]
    
    return answer