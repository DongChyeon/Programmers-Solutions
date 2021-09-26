from collections import deque

# 스택을 이용해 올바른 괄호 문자열인지 판별
def is_right(string):
    stack = []
    
    for ch in string:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        else:
            if not stack:
                return False
            if ch == ')' and stack[-1] == '(':
                stack.pop()
            elif ch == ']' and stack[-1] == '[':
                stack.pop()
            elif ch == '}' and stack[-1] == '{':
                stack.pop()
                
    if stack:
        return False
    else:
        return True

def solution(s):
    answer = 0
    string = deque(list(s))
    
    # 문자열을 왼쪽으로 회전시킨 뒤 올바른 괄호 문자열인지 판별
    for x in range(len(s)):
        string = deque(list(s))
        string.rotate(-x)
        
        if is_right(string):
            answer += 1
        
    return answer
