import math

def solution(brown, yellow):
    answer = []
    
    # 모든 타일의 수 = 넓이
    tiles = brown + yellow
    temp = []
    # 모든 가로, 세로 값의 경우의 수를 구함
    for i in range(3, int(math.sqrt(tiles)) + 1):
        if tiles % i == 0:
            if i > tiles / i:
                temp.append([i, int(tiles / i)])
            else:
                temp.append([int(tiles / i), i])
    # 정답의 타일과 일치할 때를 찾아냄
    for w, h in temp:
        if w * 2 + (h - 2) * 2 == brown:
            answer = [w, h]
            break
    
    return answer