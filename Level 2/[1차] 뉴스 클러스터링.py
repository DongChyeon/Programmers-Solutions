def jarcard_index(a, b):
    if not a and not b:
        return 65536
    
    # 다중집합의 합집합
    a1 = a.copy()    
    union = a.copy()
    for ch in b:
        if ch not in a1:
            union.append(ch)
        else:
            a1.remove(ch)
            
    # 다중집합의 교집합
    intersection = []
    for ch in b:
        if ch in a:
            a.remove(ch)
            intersection.append(ch)
            
    return int((len(intersection) / len(union)) * 65536)    

def solution(str1, str2):
    a, b = [], []
    
    for i in range(len(str1) - 1):
        temp = str1[i] + str1[i + 1]
        if temp.isalpha():
            a.append(temp.lower())
            
    for i in range(len(str2) - 1):
        temp = str2[i] + str2[i + 1]
        if temp.isalpha():
            b.append(temp.lower())
    
    return jarcard_index(a, b)
