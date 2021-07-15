from collections import Counter

def solution(s):
    answer = []
    
    # 문자열 파싱
    frequency = []
    flag = False
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            elem = ''
            flag = True
        elif s[i].isdigit() and flag:
            elem += s[i]
        elif s[i] == ',' and flag:
            frequency.append(elem)
            elem = ''
        elif s[i] == '}':
            frequency.append(elem)
            flag = False
    
    # 중복되는 빈도수가 높을수록 순서가 앞에 오게 됨
    frequency = Counter(frequency).most_common()
    for tup in frequency:
        answer.append(int(tup[0]))
    
    return answer
