def solution(s):
    answer = ''
    
    sentence = s.split()
    spacing = []
    
    space = ''
    for char in s:
        if (char != ' '):
            if (space != ''):
                spacing.append(space)
                space = ''
        else:
            space += ' '
    spacing.append(space)
    
    for i in range(0, len(sentence)):
        answer += sentence[i].capitalize() + spacing[i]
    
    return answer