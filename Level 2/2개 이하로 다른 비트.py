def f(number):
    global answer
    
    # 짝수일 경우 1 큰 수 반환
    if number % 2 == 0:
        return number + 1
    
    # 홀수일 경우 맨끝부터 탐색해 0 이 처음 나오는 위치를 파악
    # 그 위치부터 '10'으로 바꿔줌
    bit = list(bin(number).lstrip('0b').zfill(54))
    idx = 53
    while bit[idx] == '1':
        idx -= 1
    bit[idx], bit[idx + 1] = '1', '0'
    bit = '0b' + ''.join(bit)
    
    return int(bit, 2)

def solution(numbers):
    global answer
    answer = []
    
    for number in numbers:
        answer.append(f(number))
    
    return answer
