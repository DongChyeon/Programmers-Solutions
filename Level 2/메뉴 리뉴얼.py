from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for num in course:
        candidates = []
        for order in orders:
            for ch in combinations(order, num):
                candidates.append(''.join(sorted(ch)))
        # 가장 많이 주문된 단품메뉴 조합순으로 나열
        candidates = Counter(candidates).most_common()
        # 두 명 이상의 손님이 주문했고 가장 많이 주문된 단품메뉴 조합만 추가
        answer += [menu for menu, cnt in candidates if cnt > 1 and cnt == candidates[0][1]]
                
    return sorted(answer)
