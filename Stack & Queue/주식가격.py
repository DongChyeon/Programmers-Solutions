def solution(prices):
    answer = []
    
    for i in range(0, len(prices)):
        appendFlag = True
        period = 0
        for j in range(i + 1, len(prices)):
            period = j - i
            if prices[i] > prices[j]:
                answer.append(period)
                appendFlag = False
                break        
        if appendFlag:
            answer.append(period)
    
    return answer