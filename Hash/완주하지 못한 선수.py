import collections

def solution(participant, completion):
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    
    return list(a - b)[0]