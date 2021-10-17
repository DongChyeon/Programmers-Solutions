def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    # 영단어를 해당 숫자로 변환
    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
