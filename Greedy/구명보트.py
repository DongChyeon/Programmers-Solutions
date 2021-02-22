from collections import deque
import math

def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    people = deque(people)
    
    while people:
        # 첫 사람이 무게 제한의 절반 이하라면 ceil(남아있는 인원 / 2) 만큼의 보트가 필요
        if people[0] <= limit / 2:
            answer += math.ceil(len(people) / 2)
            break
        
        answer += 1
        # 첫 사람과 마지막 사람을 같이 태울 수 있으면 같이 보냄
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        # 아니면 첫 사람만 보냄
        else:
            people.popleft()
    
    return answer