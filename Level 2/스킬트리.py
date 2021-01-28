from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        skill_length = len(skill)
        skill_order = deque(skill)
        
        # 유저들이 만든 스킬트리와 선행 스킬 순서의 공통된 스킬들을 구함
        common_skill = set(skill_order) & set(tree)
        
        # 유저의 스킬트리를 순회하며 선행 스킬 순서의 첫번째 스킬일 경우 pop
        for char in tree:
            if skill_order and char == skill_order[0]:
                skill_order.popleft()
        # 선행 스킬 순서의 길이가 본래의 스킬 순서 길이에서 공통 스킬을 뺀 것과 같으면 +1
        if len(skill_order) == skill_length - len(common_skill):
            answer += 1
        
    return answer