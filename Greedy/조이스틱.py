def solution(name):
    name = list(name)
    answer = 0
    idx = 0
    
    while True:
        # 상하 방향 조절
        answer += min(ord(name[idx]) - ord('A'), (ord('Z') + 1) - ord(name[idx]))
        name[idx] = 'A'
        if name.count('A') == len(name):
            return answer
        
        # 좌우 방향 조절
        left, right = 1, 1
        while name[idx - left] == 'A':
            left += 1
        while name[idx + right] == 'A':
            right += 1
            
        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right
