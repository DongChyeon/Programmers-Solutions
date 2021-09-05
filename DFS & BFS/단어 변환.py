from collections import deque

def isConvertable(a, b):
    count = 0
    
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
            
    if count == len(a) - 1:
        return True
    else:
        return False

def solution(begin, target, words):
    # 타겟 단어가 words에 없을 시 0 리턴
    if target not in words:
        return 0
    
    visited = [False] * (len(words) + 1)
    words.insert(0, begin)
    queue = deque([(0, 0)])
    
    while queue:
        pos, count = queue.popleft()
        visited[pos] = True
        
        if words[pos] == target:
            return count
        
        endFlag = True
        for i in range(len(words)):
            if isConvertable(words[pos], words[i]) and not visited[i]:
                queue.append((i, count + 1))
                endFlag = False
        
        # 변환할 수 있는 단어가 없을 경우 0 리턴
        if endFlag:
            return 0
