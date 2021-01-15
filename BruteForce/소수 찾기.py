from itertools import permutations
import math

def solution(numbers):
    answer = 0

    comb = []
    for i in range(1, len(numbers) + 1):
        comb.append(list(permutations(numbers,i)))

    numbers2 = []
    for i in range(len(comb)):
        for j in range(len(list(comb[i]))):
            temp = ''
            for k in range(len(list(comb[i][j]))):
                temp += comb[i][j][k]
            numbers2.append(int(temp))

    for num in set(numbers2):
        div_count = 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                div_count += 1
        if div_count == 0 and num > 1:
            answer += 1

    return answer