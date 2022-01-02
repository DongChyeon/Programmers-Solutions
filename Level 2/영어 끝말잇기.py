import math

def solution(n, words):
    answer = []
    spoken_words = [words[0]]

    for i in range(len(words) - 1):
        person = (i + 1) % n + 1
        count = math.ceil((i + 2) / n)
        last, start = words[i][-1], words[i + 1][0]
        # 앞단어의 끝글자와 뒷단어의 앞글자가 맞지 않거나 이미 말한 단어일 경우 탈락
        if last != start or words[i + 1] in spoken_words:
            answer.append(person)
            answer.append(count)
            break
        spoken_words.append(words[i + 1])
    
    if not answer:
        answer.append(0)
        answer.append(0)

    return answer
