def solution(number, k):
    number_len = len(number) - k
    
    maxNum = ''
    start = 0   # 검사 시작 위치
    end = len(number) - number_len + 1   # 검사 끝 위치
    
    while len(maxNum) != number_len:
        maxVal = '0'
        for i in range(start, end):
            if number[i] == '9':
                maxVal = number[i]
                start = i + 1
                break
            elif number[i] > maxVal:
                maxVal = number[i]
                start = i + 1
        maxNum += maxVal
        end += 1
        
    return str(maxNum)