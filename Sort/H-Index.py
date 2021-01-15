def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for cite in citations:
        if cite > answer:
            answer += 1
    
    return answer