from itertools import permutations

# 연산자 우선순위가 높을수록 큰 수를 반환
def priority(perm, oper):
    return perm.index(oper)
    
def calc(exp, perm):    
    operand, operator = [], []
    
    if len(exp) == 1:
        return exp[0]
        
    for i in range(len(exp)):
        if str(exp[i]).isdigit():
            operand.append(exp[i])
        else:
            if not operator:
                operator.append(exp[i])
            # 우선순위가 더 높은 연산자가 들어올 경우 operator 스택에 추가
            elif operator and priority(perm, operator[-1]) < priority(perm, exp[i]):
                operator.append(exp[i])
            else:
                # 우선순위가 더 낮거나 같은 연산자가 들어올 경우 계산 후 계산 결과 operand 스택에 추가
                while operator and priority(perm, operator[-1]) >= priority(perm, exp[i]):
                    oper = operator.pop()
                    num2 = operand.pop()
                    num1 = operand.pop()
                    if oper == '*':
                        operand.append(num1 * num2)
                    elif oper == '+':
                        operand.append(num1 + num2)
                    elif oper == '-':
                        operand.append(num1 - num2)
                operator.append(exp[i])
    
    # operand 스택이 빌 때까지 계산 
    while operator:
        oper = operator.pop()
        num2 = operand.pop()
        num1 = operand.pop()
        if oper == '*':
            operand.append(num1 * num2)
        elif oper == '+':
            operand.append(num1 + num2)
        elif oper == '-':
            operand.append(num1 - num2)
    
    # 계산된 결과를 반환
    return operand[0]

def solution(expression):
    answer = 0
    
    exp, pool = [], []
    # exp 리스트에 연산자와 숫자를 분리
    temp = ''
    for ch in expression:
        if ch.isdigit():
            temp += ch
        else:
            exp.append(int(temp))
            exp.append(ch)
            if ch not in pool:
                pool.append(ch)
            temp = ''
    exp.append(int(temp))
    
    # 가능한 연산자 우선순위를 모두 구함
    perm = list(permutations(pool))
    
    # 각 연산자 우선순위에 대해 계산
    for x in perm:
        result = calc(exp, x)
        answer = max(abs(result), answer)
    
    return answer
