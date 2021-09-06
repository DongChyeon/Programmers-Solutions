perm = []

# 중복 조합 구하기
def dfs(count, pool, end, result):
    global perm
    
    if count == end:
        perm.append(result)
        return
    for i in range(len(pool)):
        result += pool[i]
        dfs(count + 1, pool, end, result)
        result = result[:-1]

def solution(word):
    global perm
    
    pool = ['A', 'E', 'I', 'O', 'U']
    
    # perm에 중복 순열을 담음
    for i in range(1, 6):
        dfs(0, pool, i, '')
   
    # 사전순으로 정렬한 후 그 중 word의 순서를 리턴
    return sorted(perm).index(word) + 1
