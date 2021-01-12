def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i in range(0, len(answers)):
        if person1[i % (len(person1))] == answers[i]:
            scores[0] += 1
        if person2[i % (len(person2))] == answers[i]:
            scores[1] += 1
        if person3[i % (len(person3))] == answers[i]:
            scores[2] += 1
        
    answer = []    
    
    high_score = 0
    for i in range(0, len(scores)):
        if scores[i] > high_score:
            if answer:
                answer.pop()
            high_score = scores[i]
            answer.append(i + 1)
        elif scores[i] == high_score:
            answer.append(i + 1)
    
    return answer