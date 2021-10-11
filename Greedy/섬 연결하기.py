def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    if n == 1:
        return 0
    
    answer = 0
    parent = [x for x in range(n)]
    
    # 가장 낮은 비용부터 탐색할 수 있도록 정렬
    costs.sort(key = lambda x : x[2])
    for cost in costs:
        # 모두 같은 부모(0)을 가질 경우 하나로 연결됨
        if sum(parent) == 0:
            break
        a, b, cost = cost
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    
    return answer
  
