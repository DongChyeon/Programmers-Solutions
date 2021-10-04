def solution(sizes):
    # 가로, 세로 길이
    width, length = [], []
    
    # 가로를 명함의 가장 긴 변, 세로를 명함의 가장 짧은 변으로 설정
    for card in sizes:
        width.append(max(card))
        length.append(min(card))
        
    return max(width) * max(length)
   
