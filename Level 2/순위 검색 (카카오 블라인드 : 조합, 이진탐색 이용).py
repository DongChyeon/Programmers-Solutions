from itertools import combinations

def solution(info, query):
    answer = []
    
    db = {}
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        # 조건들에 '-'를 포함한 새로운 조건을 만들어내서 모든 경우의 수에 대해 딕셔너리 처리
        for n in range(5):   
            comb = list(combinations([0, 1, 2, 3], n))
            for c in comb:
                tc = conditions.copy()
                for v in c:
                    tc[v] = '-'
                new_tc = '/'.join(tc)
                if new_tc in db:
                    db[new_tc].append(score)
                else:
                    db[new_tc] = [score]
   
    # 이진 탐색을 이용하기 위해 value를 정렬
    for v in db.values():
        v.sort()
    
    for q in query:
        temp = [x for x in q.split() if x != 'and']
        condition = '/'.join(temp[:-1])
        score = int(temp[-1])
        if condition in db:
            data = db[condition]
            # lower bound 알고리즘을 통해 해당값 이상인 값이 처음으로 나오는 인덱스 탐색
            if len(data) > 0:
                start, end = 0, len(data)
                while start < end:
                    mid = (start + end) // 2
                    if data[mid] >= score:
                        end = mid
                    else:
                        start = mid + 1
                # 검색 결과가 몇 명인지 답에 추가
                answer.append(len(data) - start)
        else:
            answer.append(0)
        
    return answer
  
