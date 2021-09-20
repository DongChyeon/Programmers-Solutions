from itertools import combinations

def solution(relation):
    pool = [x for x in range(len(relation[0]))]
    perm = []
    for x in range(len(relation[0])):
        perm.extend(list(combinations(pool, 1 + x)))
    
    # 유일성을 만족하는 키들을 구함
    keys = []
    for comb in perm:
        candidate = []
        for row in range(len(relation)):
            temp = []
            for col in range(len(relation[row])):
                if col in comb:
                    temp.append(relation[row][col])
            candidate.append(tuple(temp))
        
        # 중복을 제거했을 때 개수가 relation의 row 개수와 같을 시 유일성 만족
        if len(set(candidate)) == len(relation):
            keys.append(set(comb))
    
    # 부분집합 검사를 통해 최소성을 만족하는 키들을 구함
    for i in range(len(keys) - 1):
        j = i + 1
        while j < len(keys):
            if keys[i].issubset(keys[j]):
                del keys[j]
                j = i + 1
            else:
                j += 1
    
    return len(keys)
